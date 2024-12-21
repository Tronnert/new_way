from ursina import *
from time import time

def update_voxel_mesh(file_path):
    """Обновляем модель, загружая новый .obj файл."""
    if hasattr(update_voxel_mesh, 'voxel_entity'):
        update_voxel_mesh.voxel_entity.remove_node()  # Удаляем старую модель, если она существует

    update_voxel_mesh.voxel_entity = Entity(
        model=file_path,
        color=color.white,
        collider='mesh'
    )


def camera_control():
    camera.z += held_keys["u"]# * 10# * time.dt
    camera.z -= held_keys["j"]# * 10# * time.dt
    camera.x -= held_keys["h"]# * 10# * time.dt
    camera.x += held_keys["k"]# * 10# * time.dt
    camera.y += held_keys["y"]# * 10# * time.dt
    camera.y -= held_keys["i"]# * 10# * time.dt


def main_visualise():
    app = Ursina()

    sky = Sky()

    time_last_update = time()

    def update():
        global time_last_update
        camera_control()
        if time() - time_last_update >= 2:  # Каждую секунду
            update_voxel_mesh("voxels.obj")  # Загружаем новый .obj файл
            time_last_update = time()

    update_voxel_mesh("voxels.obj")  # Загружаем начальную модель

    EditorCamera()  # Для удобного управления камерой

    app.run()
