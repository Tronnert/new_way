from ursina import *
from time import time
from response_to_meshes import create_meshes, load_objects


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


def update():
    global time_last_update
    camera_control()
    print("TIME TIME TIME TIME TIME TIME")
    if time() - time_last_update >= 1:  # Каждую секунду
        create_meshes(load_objects(open("responses/example_response_empty.json")))
        update_voxel_mesh("voxels.obj")  # Загружаем новый .obj файл
        time_last_update = time()
        print("MESH UPDATED")


def main_visualise():
    global time_last_update, sky
    app = Ursina()
    print(app._update)
    sky = Sky()
    time_last_update = time()
    update_voxel_mesh("voxels.obj")  # Загружаем начальную модель
    EditorCamera()  # Для удобного управления камерой
    app.run()


if __name__ == "__main__":
    main_visualise()