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
from webapp2_extras import jinja2
import config
import logging

logging.getLogger().setLevel(logging.DEBUG)


class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def template(self, template, **kwargs):
        rendered_template = self.jinja2.render_template(
            template + '.html',
            **kwargs)
        return self.response.write(rendered_template)


class Main(BaseHandler):
    def get(self, page):
        page = "index" if page == "" else page
        logging.info(page)
        self.template(page)


app = webapp2.WSGIApplication([
                                  (r'/(\w*)', Main)
                              ], config=config.CONFIG, debug=config.CONFIG['debug'])
