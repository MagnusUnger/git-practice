import threading
import time

list_for_websites = ["https://minecraft.com", "https://google.com", "https://crunchyroll.com"]

def navigating_to(website_link, delay= 3):
    print(f"Navigating to {website_link}")
    time.sleep(delay)
    print(f"Navigation to {website_link} endet")


threads = []
for link in list_for_websites:
    single_thread = threading.Thread(target=navigating_to, args=(link,), kwargs={"delay": 2})
    threads.append(single_thread)


for t in threads:
    t.start()

for t in threads:
    t.join()    


