# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import (SubmitField,
                            StringField,
                            FormField,
                            FieldList,
                            SelectField)
from wtforms.fields.html5 import IntegerField
from wtforms.validators import (InputRequired,
                                Length,
                                NumberRange)

from wazo_admin_ui.helpers.destination import DestinationHiddenField, DestinationField
from wazo_admin_ui.helpers.form import BaseForm


class IvrChoiceForm(BaseForm):
    exten = StringField(validators=[InputRequired(), Length(max=40)])
    destination = DestinationField(destination_label='')


class IvrForm(BaseForm):
    name = StringField('Name', [InputRequired(), Length(max=128)])
    abort_destination = DestinationField(destination_label='Abort destination')
    abort_sound = StringField('Abort sound', [Length(max=255)])
    choices = FieldList(FormField(IvrChoiceForm))
    description = StringField('Description')
    greeting_sound = StringField('Greeting sound', [Length(max=255)])
    invalid_destination = DestinationField(destination_label='Invalid destination')
    invalid_sound = StringField('Invalid sound', [Length(max=255)])
    max_tries = IntegerField('Max tries', default=3, validators=[NumberRange(min=1)])
    menu_sound = StringField('Menu sound', validators=[InputRequired(), Length(max=255)])
    timeout = IntegerField('Timeout', default=0, validators=[NumberRange(min=0)])
    timeout_destination = DestinationField(destination_label='Timeout destination')
    submit = SubmitField('Submit')


class IvrDestinationForm(BaseForm):
    setted_value_template = u'{ivr_name}'

    ivr_id = SelectField('IVR', [InputRequired()], choices=[])
    ivr_name = DestinationHiddenField()
