# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint

from .service import IvrService
from .view import IvrView

ivr = create_blueprint('ivr', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']
        config = dependencies['config']

        IvrView.service = IvrService(config['confd'])
        IvrView.register(ivr, route_base='/ivrs')
        register_flaskview(ivr, IvrView)

        core.register_blueprint(ivr)
