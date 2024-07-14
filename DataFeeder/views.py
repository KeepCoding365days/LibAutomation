from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from DataFeeder.queu import append_to_queue


@api_view(['POST'])
def ordered_book(request):
    if request.method == "POST":
        book_id = request.query_params.get("book_id")
        station_id = request.query_params.get("station_id")
        if len(book_id) == 16 and len(station_id) == 1:

            with open("/Users/affan/Documents/AI-ML/NLP/LibAutomation/ordered_book.txt", "a") as file:
                file.write(f"{book_id}{station_id}\n")
                file.close()

            return HttpResponse("success", status=200)
        else:
            return HttpResponse("Bad Request", status=400)


@api_view(['POST'])
def ordered_book_delay(request):
    if request.method == "POST":
        book_id = request.query_params.get("book_id")
        station_id = request.query_params.get("station_id")
        if len(book_id) == 16 and len(station_id) == 1:

            append_to_queue(book_id + station_id)
            print("appended")

            return HttpResponse("success", status=200)
        else:
            return HttpResponse("Bad Request", status=400)
