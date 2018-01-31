# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.confd import confd
from wazo_admin_ui.helpers.service import BaseConfdService


class IvrService(BaseConfdService):

    resource_confd = 'ivr'

    def list_sound(self):
        return confd.sounds.list()

    def list_sound_filename(self, sound_name):
        return confd.sounds.get(sound_name)

    def find_sound_by_path(self, sound_path):
        sounds = self.list_sound()['items']
        for sound in sounds:
            for file_ in sound['files']:
                for format_ in file_['formats']:
                    if sound['name'] == 'system':
                        if file_['name'] == sound_path:
                            return file_, format_
                    else:
                        if format_['path'] == sound_path:
                            return file_, format_
        return None, None
