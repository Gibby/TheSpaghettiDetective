from django.urls import path, re_path
from django.views.generic.base import RedirectView

from .views import web_views
from .views import mobile_views

from .views import tunnel_views
from .views import tunnelv2_views

urlpatterns = [
    path('', web_views.index, name='index'),
    path('accounts/login/', web_views.SocialAccountAwareLoginView.as_view(), name="account_login"),
    path('media/<path:file_path>', web_views.serve_jpg_file),  # semi hacky solution to serve image files
    path('printers/', web_views.printers, name='printers'),
    path('printers/<pk>/', web_views.edit_printer),
    path('printers/<int:pk>/delete/', web_views.delete_printer),
    path('printers/<int:pk>/control/', web_views.printer_control),
    path('printers/share_token/<share_token>/', web_views.printer_shared, name='printer_shared'),
    path('user_preferences/', web_views.user_preferences),
    path('test_telegram', web_views.test_telegram),
    path('unsubscribe_email/', web_views.unsubscribe_email),
    path('prints/<int:pk>/cancel/', web_views.cancel_print),
    path('prints/<int:pk>/resume/', web_views.resume_print),
    path('prints/', web_views.prints, name='prints'),
    path('prints/upload/', web_views.upload_print),
    path('prints/<pk>/', web_views.print),
    path('prints/shot-feedback/<pk>/', web_views.print_shot_feedback),
    path('gcodes/', web_views.gcodes),
    path('gcodes/upload/', web_views.upload_gcode_file,),
    path('hc/', web_views.health_check,),
    path('publictimelapses/', RedirectView.as_view(url='/ent_pub/publictimelapses/', permanent=True), name='publictimelapse_list'),

    # tunnel v1 http endpoint
    re_path(
        r'^octoprint/(?P<pk>\d+)',
        web_views.octoprint_http_tunnel,
        name='octoprint_http_tunnel'),

    # tunnel v1/v2 page with iframe
    path('tunnel/<int:pk>/', tunnel_views.tunnel),
    path('tunnels/<int:pk>/', tunnel_views.tunnel),
    path('tunnels/new/', tunnelv2_views.new_octoprinttunnel, name='new_octoprinttunnel'),
    path('tunnels/succeeded/', tunnelv2_views.new_octoprinttunnel_succeeded, name='new_octoprinttunnel_succeeded'),

    # Shown only in mobile apps
    path('mobile/auth/login/', mobile_views.MobileLoginView.as_view(), name='mobile_auth_login'),
    path('mobile/auth/signup/', mobile_views.MobileSignupView.as_view(), name='mobile_auth_signup'),
    path('mobile/auth/apple/', mobile_views.apple_login),
    path('mobile/auth/fetch/', mobile_views.fetch_session),
    path('mobile/auth/oauth_callback/', mobile_views.oauth_callback),
    path('mobile/user_preferences/', web_views.user_preferences),
    path('mobile/prints/', web_views.prints),
    path('mobile/gcodes/', web_views.gcodes, {"template_dir": "mobile"}),
    path('mobile/gcodes/upload/', web_views.upload_gcode_file),
    path('mobile/printers/<pk>/', web_views.edit_printer),
    path('mobile/printers/<int:pk>/delete/', web_views.delete_printer),
]
