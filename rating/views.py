from django.shortcuts import render
from .choices import rating_choices
from .models import  Listing, Rating

# Create your views here.
def rating(request, listing_id):
    if request.method == "POST":
        name = request.POST['name']
        message = request.POST['message']
        proid = listing_id

        query = Rating(message = message, name = name)
        query.proid_id = proid
        query.save()


    ratings = Rating.objects.all().filter(proid = listing_id)

    context = {
        'ratings' : rating,
        'rating_choices':rating_choices
    }
    return render(request,'listings/listing.html',context)
