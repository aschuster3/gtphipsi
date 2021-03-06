"""URL configuration for the gtphipsi.brothers package.

All URIs beginning with '/brothers/' are routed to this URL configuration.

"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('gtphipsi.brothers.views',
    ## ============================================= ##
    ##                 Public Pages                  ##
    ## ============================================= ##
    url(r'^$', 'list', name='brothers_list'),
    url(r'^(?P<badge>\d+)/$', 'show', name='view_profile'),
    url(r'^email/$', 'change_email', name='change_email'),
    url(r'^email/success/$', 'change_email_success', name='change_email_success'),

    ## ============================================= ##
    ##              Authenticated Pages              ##
    ## ============================================= ##
    url(r'^profile/$', 'my_profile', name='my_profile'),
    url(r'^manage/$', 'manage', name='manage_users'),
    url(r'^add/$', 'add', name='add_user'),
    url(r'^edit/$', 'edit', name='edit_profile'),
    url(r'^account/$', 'edit_account', name='edit_my_account'),
    url(r'^(?P<badge>\d+)/account/$', 'edit_account', name='edit_account'),
    url(r'^(?P<badge>\d+)/unlock/$', 'unlock', name='unlock_account'),
    url(r'^password/$', 'change_password', name='change_password'),
    url(r'^password/success/$', 'change_password_success', name='change_password_success'),
    url(r'^groups/$', 'manage_groups', name='manage_groups'),
    url(r'^groups/add/$', 'add_group', name='add_group'),
    url(r'^groups/(?P<id>\d+)/$', 'show_group', name='view_group'),
    url(r'^groups/(?P<id>\d+)/perms/$', 'edit_group_perms', name='edit_group_perms'),
    url(r'^groups/(?P<id>\d+)/members/$', 'edit_group_members', name='edit_group_members'),
    url(r'^groups/(?P<id>\d+)/delete/$', 'delete_group', name='delete_group'),
    url(r'^privacy/$', 'visibility', name='visibility'),
    url(r'^privacy/public/$', 'edit_public_visibility', name='edit_public_visibility'),
    url(r'^privacy/chapter/$', 'edit_chapter_visibility', name='edit_chapter_visibility'),
    url(r'^notifications/$', 'edit_notification_settings', name='notification_settings'),
)