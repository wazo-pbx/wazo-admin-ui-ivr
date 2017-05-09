# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.destination import register_destination_form, register_listing_url

from .service import IvrService
from .view import IvrView, IvrDestinationView
from .form import IvrDestinationForm

ivr = create_blueprint('ivr', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        IvrView.service = IvrService()
        IvrView.register(ivr, route_base='/ivrs')
        register_flaskview(ivr, IvrView)

        IvrDestinationView.service = IvrService()
        IvrDestinationView.register(ivr, route_base='/ivr_destination')

        register_destination_form('ivr', 'Ivr', IvrDestinationForm)
        register_listing_url('ivr', 'ivr.IvrDestinationView:list_json')

        core.register_blueprint(ivr)
