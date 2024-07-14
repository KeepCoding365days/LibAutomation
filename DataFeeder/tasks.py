from DataFeeder.queu import get_first_from_queue

from celery import shared_task


def write_data_to_file():
    first = get_first_from_queue()
    if first == None:
        print("empty queue")
        return
    # Path to the file
    with open("/Users/affan/Documents/AI-ML/NLP/LibAutomation/ordered_book.txt", "a") as file:
        file.write(f"{first}\n")
    file.close()


