import threading
from main import main
from snake_ursina import main_visualise

# lock = threading.Lock()


from multiprocessing import Process
from ursina import Ursina, Entity

# def run_ursina():
#     app = Ursina()
#     Entity(model='cube', color=color.orange, scale=(2, 2, 2))
#     app.run()

if __name__ == "__main__":
    # ursina_process = Process(target=main_visualise)
    response_process = Process(target=main)
    # ursina_process.start()
    response_process.start()

    # Здесь можно выполнять другие задачи
    # ursina_process.join()
    # main_visualise()
    # response_process.join()

 

# if __name__ == "__main__":
#     # response_thread = threading.Thread(target=main)
#     visual_thread = threading.Thread(target=main_visualise) 
#     # threads = [threading.Thread(target=increment_counter) for _ in range(10)]
#     # threads = [response_thread, visual_thread]
#     #threads = [response_thread]
#     threads = [visual_thread]

#     for thread in threads:
#         thread.start()
    
    # for thread in threads:
    #     thread.join()
