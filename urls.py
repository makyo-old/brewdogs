from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^recipe/category/list/$', 'brewdogs.recipe.views.list_categories'),
    (r'^recipe/category/(?P<slug>[a-zA-Z0-9_-]+)/$', 'brewdogs.recipe.views.show_category'),
    (r'^recipe/list/$', 'brewdogs.recipe.views.list_recipies'),
    (r'^recipe/(?P<id>\d+)/$', 'brewdogs.recipe.views.show_recipe'),
    (r'^recipe/(?P<id>\d+)/edit/', 'brewdogs.recipe.views.edit_recipe'),
    (r'^recipe/(?P<id>\d+)/delete/$', 'brewdogs.recipe.views.delete_recipe'),
    (r'^recipe/create/$', 'brewdogs.recipe.views.create_recipe'),
    # Example:
    # (r'^brewdogs/', include('brewdogs.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
