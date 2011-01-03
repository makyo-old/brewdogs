from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'brewdogs.usermgmt.views.front'),

    (r'^~(?P<username>.+)/$', 'brewdogs.usermgmt.views.show_user'),

    (r'^recipe/category/list/$', 'brewdogs.recipe.views.list_categories'),
    (r'^recipe/category/(?P<slug>[a-zA-Z0-9_-]+)/$', 'brewdogs.recipe.views.show_category'),
    (r'^recipe/category/(?P<slug>[a-zA-Z0-9_-]+)/edit/$', 'brewdogs.recipe.views.edit_category'),
    (r'^recipe/category/(?P<slug>[a-zA-Z0-9_-]+)/delete/$', 'brewdogs.recipe.views.delete_category'),
    (r'^recipe/category/create/$', 'brewdogs.recipe.views.create_category'),
    (r'^recipe/list/$', 'brewdogs.recipe.views.list_recipies'),
    (r'^recipe/(?P<id>\d+)/$', 'brewdogs.recipe.views.show_recipe'),
    (r'^recipe/(?P<id>\d+)/edit/', 'brewdogs.recipe.views.edit_recipe'),
    (r'^recipe/(?P<id>\d+)/delete/$', 'brewdogs.recipe.views.delete_recipe'),
    (r'^recipe/create/$', 'brewdogs.recipe.views.create_recipe'),

    (r'^brew/(?P<id>\d+)/$', 'brewdogs.brewsession.views.show_fermentation'),
    (r'^run/(?P<id>\d+)/$', 'brewdogs.brewsession.views.show_distillation'),
    (r'^brew/(?P<id>\d+)/edit/$', 'brewdogs.brewsession.views.edit_fermentation'),
    (r'^run/(?P<id>\d+)/edit/$', 'brewdogs.brewsession.views.edit_distillation'),
    (r'^brew/(?P<id>\d+)/delete/$', 'brewdogs.brewsession.views.delete_fermentation'),
    (r'^run/(?P<id>\d+)/delete/$', 'brewdogs.brewsession.views.delete_distillation'),
    (r'^brew/(?P<recipe_id>\d+)/$', 'brewdogs.brewsession.views.create_fermentation'),
    (r'^run/(?P<fermentation_id>\d+)/$', 'brewdogs.brewsession.views.create_distillation'),

    (r'^comment/create/$', 'brewdogs.threadedcomment.views.create_comment'),
    (r'^comment/(?P<id>\d+)/edit/$', 'brewdogs.threadedcomment.views.edit_comment'),
    (r'^comment/(?P<id>\d+)/flag/$', 'brewdogs.threadedcomment.views.flag_comment'),
    (r'^comment/(?P<id>\d+)/delete/$', 'brewdogs.threadedcomment.views.delete_comment'),

    (r'^ajax/add_fermentation_event/$', 'brewdogs.brewsession.views.add_fermentation_event'),
    (r'^ajax/add_distillation_event/$', 'brewdogs.brewsession.views.add_distillation_event'),
    (r'^ajax/add_ingredient/$', 'brewdogs.recipe.views.add_ingredient'),
    (r'^ajax/add_equipment_item/$', 'brewdogs.recipe.views.add_equipment_item'),
    (r'^ajax/add_step/$', 'brewdogs.recipe.views.add_step'),
    (r'^ajax/edit_fermentation_event/$', 'brewdogs.brewsession.views.edit_fermentation_event'),
    (r'^ajax/edit_distillation_event/$', 'brewdogs.brewsession.views.edit_distillation_event'),
    (r'^ajax/edit_ingredient/$', 'brewdogs.recipe.views.edit_ingredient'),
    (r'^ajax/edit_step/$', 'brewdogs.recipe.views.edit_step'),
    (r'^ajax/delete_fermentation_event/$', 'brewdogs.brewsession.views.delete_fermentation_event'),
    (r'^ajax/delete_distillation_event/$', 'brewdogs.brewsession.views.delete_distillation_event'),
    (r'^ajax/delete_ingredient/$', 'brewdogs.recipe.views.delete_ingredient'),
    (r'^ajax/delete_equipment_item/$', 'brewdogs.recipe.views.delete_equipment_item'),
    (r'^ajax/delete_step/$', 'brewdogs.recipe.views.delete_step'),
    (r'^ajax/add_recipe_to_docket/$', 'brewdogs.recipe.views.add_recipe_to_docket'),
    (r'^ajax/remove_recipe_from_docket/$', 'brewdogs.recipe.views.remove_recipe_from_docket'),
    (r'^ajax/add_fermentation_to_working/$', 'brewdogs.brewsession.views.add_fermentation_to_working'),
    (r'^ajax/add_distillation_to_working/$', 'brewdogs.brewsession.views.add_distillation_to_working'),
    (r'^ajax/add_fermentation_to_aging/$', 'brewdogs.brewsession.views.add_fermentation_to_aging'),
    (r'^ajax/add_distillation_to_aging/$', 'brewdogs.brewsession.views.add_distillation_to_aging'),
    (r'^ajax/add_fermentation_to_drinking/$', 'brewdogs.brewsession.views.add_fermentation_to_drinking'),
    (r'^ajax/add_distillation_to_drinking/$', 'brewdogs.brewsession.views.add_distillation_to_drinking'),
    (r'^ajax/remove_fermentation_from_lists/$', 'brewdogs.brewsession.views.remove_fermentation_from_lists'),
    (r'^ajax/remove_distillation_from_lists/$', 'brewdogs.brewsession.views.remove_distillation_from_lists'),

    # Example:
    # (r'^brewdogs/', include('brewdogs.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
