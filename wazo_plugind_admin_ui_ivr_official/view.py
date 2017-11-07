# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import jsonify, request
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, NewViewMixin, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response

from .form import IvrForm


class IvrView(NewViewMixin, BaseView):

    form = IvrForm
    resource = 'ivr'

    @classy_menu_item('.ivr', 'Ivr', order=4, icon="navicon")
    def index(self):
        return super(IvrView, self).index()

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('ivr', {}))
        return form


class IvrDestinationView(LoginRequiredView):

    def list_json(self):
        params = extract_select2_params(request.args)
        ivrs = self.service.list(**params)
        results = [{'id': ivr['id'], 'text': ivr['name']} for ivr in ivrs['items']]
        return jsonify(build_select2_response(results, ivrs['total'], params))
