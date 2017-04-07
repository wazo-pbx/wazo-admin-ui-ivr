# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_wtf import FlaskForm

from wtforms.fields import (SubmitField,
                            StringField,
                            IntegerField,
                            FormField,
                            FieldList,
                            SelectField)
from wtforms.validators import (InputRequired,
                                DataRequired,
                                Optional)

from wazo_admin_ui.helpers.destination import DestinationHiddenField, DestinationField


class IvrChoiceForm(FlaskForm):
    exten = StringField()
    destination = DestinationField(destination_label='')


class IvrForm(FlaskForm):
    name = StringField('Name', [InputRequired()])
    abort_destination = DestinationField(destination_label='Abort destination')
    abort_sound = StringField('Abort sound')
    choices = FieldList(FormField(IvrChoiceForm))
    description = StringField('Description')
    greeting_sound = StringField('Greeting sound')
    invalid_destination = DestinationField(destination_label='Invalid destination')
    invalid_sound = StringField('Invalid sound')
    max_tries = IntegerField('Max tries', default=3, validators=[Optional()])
    menu_sound = StringField('Menu sound', validators=[DataRequired()])
    timeout = IntegerField('Timeout', default=0, validators=[Optional()])
    timeout_destination = DestinationField(destination_label='Timeout destination')
    submit = SubmitField('Submit')


class IvrDestinationForm(FlaskForm):
    setted_value_template = u'{ivr_name}'

    ivr_id = SelectField('IVR', choices=[])
    ivr_name = DestinationHiddenField()
