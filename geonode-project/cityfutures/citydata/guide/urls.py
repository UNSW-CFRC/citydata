# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 City Futures Research Centre
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    'geonode.guide.views',
    url(r'^user/$', TemplateView.as_view(template_name='guide/user_guide.html'), name='user_guide'),

    url(r'^admin/$', TemplateView.as_view(template_name='guide/admin_guide.html'), name='admin_guide'),

    url(r'^lib/$', TemplateView.as_view(template_name='guide/lib_guide.html'), name='lib'),
    
    # PDF Guide views
    url(r'^pdf/(?P<role>[A-Za-z]+)$', 'PdfGuideView', name='PdfGuideView'),
)
