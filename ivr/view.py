# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import jsonify, request
from flask_menu.classy import classy_menu_item
from marshmallow import fields

from wazo_admin_ui.helpers.classful import BaseView, NewViewMixin, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response
from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema, extract_form_fields
from wazo_admin_ui.helpers.destination import DestinationSchema

from .form import IvrForm, IvrChoiceForm


class IvrChoices(BaseSchema):

    destination = fields.Nested(DestinationSchema)

    class Meta:
        fields = extract_form_fields(IvrChoiceForm)


class IvrSchema(BaseSchema):

    timeout_destination = fields.Nested(DestinationSchema)
    abort_destination = fields.Nested(DestinationSchema)
    invalid_destination = fields.Nested(DestinationSchema)
    choices = fields.List(fields.Nested(IvrChoices))

    class Meta:
        fields = extract_form_fields(IvrForm)


class AggregatorSchema(BaseAggregatorSchema):
    _main_resource = 'ivr'

    ivr = fields.Nested(IvrSchema)


class IvrView(NewViewMixin, BaseView):

    form = IvrForm
    resource = 'ivr'
    schema = AggregatorSchema

    @classy_menu_item('.ivr', 'Ivr', order=4, icon="navicon")
    def index(self):
        return super(IvrView, self).index()


class IvrDestinationView(LoginRequiredView):

    def list_json(self):
        params = extract_select2_params(request.args)
        ivrs = self.service.list(**params)
        results = [{'id': ivr['id'], 'text': ivr['name']} for ivr in ivrs['items']]
        return jsonify(build_select2_response(results, ivrs['total'], params))
