from main.models import Profile


def profile(request):
    return {"profile": Profile.objects.first()}
