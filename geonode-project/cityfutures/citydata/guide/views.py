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

from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from geonode import settings

# Allow authenticated users to see User PDF, and admins users to see the others
def PdfGuideView(request,role):
    if  request.user.is_superuser or request.user.is_authenticated() and role == 'User':
        with open(settings.MEDIA_ROOT + '/guides/CityData_' + role + '_Guide.pdf', 'r') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=CityData_' + role + '_Guide.pdf'
            return response
    else:
        return TemplateResponse(request, '401.html', {}, status=401).render()
