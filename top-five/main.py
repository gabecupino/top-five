#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
from google.appengine.ext import ndb

temp_place = ['name', 'Kyo-Chon', 'bgImage',
         'kyochonlogo.jpg', 'iconImage', 'chicken.png']


DEFAULT_LIST_NAME = 'cool_list'


def list_key(list_name=DEFAULT_LIST_NAME):
    ''' Constructs a Datastore key for a list entity. '''
    return ndb.Key('List', list_name)

class Place(ndb.Model):
    ''' Main model representing a place '''
    name = ndb.StringProperty('Name')
    bgImage = ndb.StringProperty('Background Image')
    icon = ndb.StringProperty('Icon')


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class ListHandler(webapp2.RequestHandler):
    def get(self):
        places_query = Place.query().order()
        places = places_query.fetch(5)

        self.response.write(json.dumps([place.to_dict() for place in places]))

class PutHandler(webapp2.RequestHandler):
    def get(self):
        list_name=DEFAULT_LIST_NAME
        
        place = Place(parent=list_key(list_name))
        place.name = 'Halal Guys'
        place.bgImage = 'halalguyslogo.png'
        place.icon = 'chickenrice.jpg'

        place.put()


    



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/list/123', ListHandler),
    ('/put', PutHandler)
], debug=True)





