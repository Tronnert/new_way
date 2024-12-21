import threading
from main import main
from snake_ursina import main_visualise

counter = 0
lock = threading.Lock()
 

if __name__ == "__main__":
    response_thread = threading.Thread(target=main)
    visual_thread = threading.Thread(target=main_visualise) 
    # threads = [threading.Thread(target=increment_counter) for _ in range(10)]
    threads = [response_thread, visual_thread]

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
