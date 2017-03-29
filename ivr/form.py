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

from wazo_admin_ui.helpers.destination import DestinationHiddenField


class IVRDestinationForm(FlaskForm):
    type = SelectField('Destination', choices=[], validators=[DataRequired()])
    result = SelectField('Result', choices=[], validators=[DataRequired()])


class IVRChoicesForm(FlaskForm):
    exten = StringField('Extension', validators=[DataRequired()])
    destination = FieldList(FormField(IVRDestinationForm), min_entries=1)


class IvrForm(FlaskForm):
    name = StringField('Name', [InputRequired()])
    abort_destination = FieldList(FormField(IVRDestinationForm), min_entries=1)
    abort_sound = StringField('Abort sound')
    choices = FieldList(FormField(IVRChoicesForm), min_entries=1)
    description = StringField('Description')
    greeting_sound = StringField('Greeting sound')
    invalid_destination = FieldList(FormField(IVRDestinationForm), min_entries=1)
    invalid_sound = StringField('Invalid sound')
    max_tries = IntegerField('Max tries', validators=[Optional()])
    menu_sound = StringField('Menu sound', validators=[DataRequired()])
    timeout = IntegerField('Timeout', validators=[Optional()])
    timeout_destination = FieldList(FormField(IVRDestinationForm), min_entries=1)
    submit = SubmitField('Submit')


class IvrDestinationForm(FlaskForm):
    setted_value_template = '{ivr_name}'

    ivr_id = SelectField('IVR', choices=[])
    ivr_name = DestinationHiddenField()

