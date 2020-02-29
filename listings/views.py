from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from listings.choices import state_choices, price_choices, bedroom_choices


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)
    per_page = 6
    paginator = Paginator(listings, per_page)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    qs = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            qs = Listing.objects.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            qs = Listing.objects.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            qs = Listing.objects.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            qs = Listing.objects.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            qs = Listing.objects.filter(price__lte=price)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': qs,
        'search_value': request.GET
    }
    return render(request, 'listings/search.html', context)
