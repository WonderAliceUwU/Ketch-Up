import base64
import os.path

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods

from app.models import Users, UserRelations


@require_http_methods('GET')
def view(request):  # noqa
    # Temporary code for testing purposes, the intended
    # behaviour is to filter by the users that has been added
    users_models_list = Users.objects.all()
    username_query = None
    if 'query' not in request.GET:
        return HttpResponse(status=400)

    username_query = request.GET["query"]

    users_list = []

    image_path = os.path.join(settings.BASE_DIR, 'testlogo.png')

    # Reads the image from disk
    with open(image_path, 'rb') as image_reader:
        image_data = image_reader.read()

    # Placeholder image codified to base64, applied to every user for testing
    image_data = base64.b64encode(image_data).decode('utf-8')
    users_models_list = Users.objects.filter(username=username_query)

    # Checks if user exits in database
    if len(users_models_list) == 0:
        return HttpResponse(status=404)

    UserRelations
    for user in users_models_list:
        users_list.append({"username": user.username,
                           "picture": image_data,
                           "id": user.user_id})

    return JsonResponse({'users': users_list})
