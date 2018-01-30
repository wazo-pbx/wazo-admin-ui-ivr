# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from flask import jsonify, request
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, NewViewMixin, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response

from .form import IvrForm


class IvrView(NewViewMixin, BaseView):
    form = IvrForm
    resource = 'ivr'

    @classy_menu_item('.ivr', l_('IVR'), order=4, icon="navicon")
    def index(self):
        return super().index()

    def _map_resources_to_form(self, resource):
        self._build_ivr_choices_sound(resource)
        form = self.form(data=resource)
        return form

    def _build_ivr_choices_sound(self, resource):
        for choice in resource['choices']:
            if choice['destination']['type'] == 'sound':
                file_, format_ = self.service.find_sound_by_path(choice['destination']['filename'])
                if file_:
                    choice['destination']['name'] = file_['name']
                    choice['destination']['format'] = self._prepare_sound_format(format_['format'])
                    choice['destination']['language'] = self._prepare_sound_language(format_['language'])

    def _populate_form(self, form):
        sounds = self.service.list_sound()
        form.menu_sound.choices = self._build_set_choices_sound(sounds)
        form.invalid_sound.choices = self._build_set_choices_sound(sounds)
        form.greeting_sound.choices = self._build_set_choices_sound(sounds)
        form.abort_sound.choices = self._build_set_choices_sound(sounds)
        return form

    def _build_set_choices_sound(self, sounds):
        yield (None, l_('None'))
        for sound in sounds['items']:
            for file_ in sound['files']:
                for format_ in file_['formats']:
                    if sound['name'] == 'system':
                        yield (file_['name'], self._prepare_sound_filename_infos(file_, format_))
                    else:
                        yield (format_['path'], self._prepare_sound_filename_infos(file_, format_))

    def _prepare_sound_filename_infos(self, file_, format_):
        return '{}.{} ({})'.format(file_['name'],
                                   self._prepare_sound_format(format_['format']),
                                   self._prepare_sound_language(format_['language']))

    def _prepare_sound_language(self, language):
        if not language:
            return l_('Unknown language')
        return language

    def _prepare_sound_format(self, format_):
        if not format_:
            return l_('Unknown format')
        return format_

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('ivr', {}))
        return form


class IvrDestinationView(LoginRequiredView):

    def list_json(self):
        params = extract_select2_params(request.args)
        ivrs = self.service.list(**params)
        results = [{'id': ivr['id'], 'text': ivr['name']} for ivr in ivrs['items']]
        return jsonify(build_select2_response(results, ivrs['total'], params))
