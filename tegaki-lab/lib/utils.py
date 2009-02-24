# -*- coding: utf-8 -*-

# Copyright (C) 2008 Mathieu Blondel
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from tegaki.character import *

def writing_to_xml(writing):
    character = Character()
    character.set_utf8("?")
    character.set_writing(writing)
    return character.to_xml()

def writing_to_json(writing):
    character = Character()
    character.set_utf8("?")
    character.set_writing(writing)
    return character.to_json() 

def xml_to_writing(xml):
    character = Character()
    character.read_string(xml)
    return character.get_writing()
