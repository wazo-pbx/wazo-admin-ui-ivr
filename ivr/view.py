# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields

from wazo_admin_ui.helpers.classful import BaseView, BaseDestinationView
from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema, extract_form_fields

from .form import IvrForm


class IvrSchema(BaseSchema):

    class Meta:
        fields = extract_form_fields(IvrForm)


class AggregatorSchema(BaseAggregatorSchema):
    _main_resource = 'ivr'

    ivr = fields.Nested(IvrSchema)


class IvrView(BaseView):

    form = IvrForm
    resource = 'ivr'
    schema = AggregatorSchema

    @classy_menu_item('.ivr', 'Ivr', order=4, icon="navicon")
    def index(self):
        return super(IvrView, self).index()

class IvrDestinationView(BaseDestinationView):

    def list_json(self):
        params = self._extract_params()
        ivrs = self.service.list(**params)
        results = [{'id': ivr['id'], 'text': ivr['name']} for ivr in ivrs['items']]
        return self._select2_response(results, ivr['total'], params)
