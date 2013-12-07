# Copyright (C) 2012 Daniil Egorov <datsideofthemoon@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, url, include
from django.conf import settings

#OpenBTS:
from webgui.views import main, advanced, status, actions, addparam
#Smqueue
from webgui.views import smqadvanced, smqactions
#SubscriberRegistry
from webgui.views import sbrdialdata, sbractions, sbradvanced

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Media static files:
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    url(r'^$', main),
    #OpenBTS:
    url(r'^openbts/main/', main),
    url(r'^openbts/advanced/', advanced),
    url(r'^openbts/status/', status),
    url(r'^openbts/actions/', actions),
    url(r'^openbts/addparam/', addparam),
    #Smqueue:
    url(r'^smqueue/actions/', smqactions),
    url(r'^smqueue/configuration/', smqadvanced),
    #SubscriberRegistry
    url(r'^subscriberregistry/actions/', sbractions),
    url(r'^subscriberregistry/configuration/', sbradvanced),
    url(r'^subscriberregistry/subscribers/', sbrdialdata),
)
