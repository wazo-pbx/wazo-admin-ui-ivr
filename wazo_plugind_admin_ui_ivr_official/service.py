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
        for sound in self.list_sound()['items']:
            if sound['name'] == 'system':
                for file in sound['files']:
                    for format in file['formats']:
                        if file['name'] == sound_path:
                            return file, format
            else:
                for file in sound['files']:
                    for format in file['formats']:
                        if format['path'] == sound_path:
                            return file, format
        return None, None
