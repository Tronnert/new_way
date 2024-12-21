import json
import trimesh
import numpy as np
import pandas as pd
from main import make_food


def load_variables_objects(fences, snakes, enemies, food):
    voxels = []
    dx = dy = dz = 0
    for fence in fences:
        voxels.append((fence[0] + dx, fence[1] + dy, fence[2] + dz, "#000000"))
    for snake in snakes:
        snake_color = "#008000" if snake["status"] == "alive" else "#006400"
        for point in snake["geometry"]:
            voxels.append((point[0] + dx, point[1] + dy, point[2] + dz, snake_color))
    for snake in enemies:
        snake_color = "#FF0000" if snake["status"] == "alive" else "#8b0000"
        for point in snake["geometry"]:
            voxels.append((point[0] + dx, point[1] + dy, point[2] + dz, snake_color))
    for yummi in food:
        yummi_color = "#964B00" if yummi["type"] == "suspicious" else "FFFF00" if \
            yummi["type"] == "goolden" else "#FFA500"
        voxels.append((yummi["c"][0] + dx, yummi["c"][1] + dy, yummi["c"][2] + dz, yummi_color))
    return pd.DataFrame(voxels, columns=["x", "y", "z", "c"])


def load_objects(response):
    objects = json.load(response)
    dx = dz = dy = 0
    fences = objects["fences"]
    snakes = objects["snakes"]
    enemies = objects["enemies"]
    food = objects["food"]
    specialFood = objects["specialFood"]
    food = make_food(food, specialFood)
    voxels = []
    for fence in fences:
        voxels.append((fence[0] + dx, fence[1] + dy, fence[2] + dz, "#000000"))
    for snake in snakes:
        snake_color = "#008000" if snake["status"] == "alive" else "#006400"
        for point in snake["geometry"]:
            voxels.append((point[0] + dx, point[1] + dy, point[2] + dz, snake_color))
    for snake in enemies:
        snake_color = "#FF0000" if snake["status"] == "alive" else "#8b0000"
        for point in snake["geometry"]:
            voxels.append((point[0] + dx, point[1] + dy, point[2] + dz, snake_color))
    for yummi in food:
        yummi_color = "#964B00" if yummi["type"] == "suspicious" else "FFFF00" if \
            yummi["type"] == "goolden" else "#FFA500"
        voxels.append((yummi["c"][0] + dx, yummi["c"][1] + dy, yummi["c"][2] + dz, yummi_color))
    return pd.DataFrame(voxels, columns=["x", "y", "z", "c"])


def convert_hex_to_rgb(hex_color):
    """Конвертирует цвет из HEX в RGB."""
    return tuple(int(hex_color.strip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4))


def create_meshes(df):
    centers = df[["x", "y", "z"]].to_numpy() 
    colors = np.array([convert_hex_to_rgb(c) for c in df["c"]])
    voxel_size = 1.0

    meshes = []

    # Создание кубов для каждого вокселя
    for center, color in zip(centers, colors):
        # Создаём куб
        box = trimesh.creation.box(extents=(voxel_size, voxel_size, voxel_size), transform=trimesh.transformations.translation_matrix(center))
        # Добавляем цвет к кубу
        box.visual.vertex_colors = [color] * len(box.vertices)
        meshes.append(box)

    # Объединяем все кубы в один меш
    combined_mesh = trimesh.util.concatenate(meshes)

    # Сохраняем меш в файл
    combined_mesh.export("voxels.obj")
    print("MESH SAVED")


if __name__ == "__main__":
    data = open("example_response.json")
    voxels = load_objects(data)
    df = pd.DataFrame(voxels, columns=["x", "y", "z", "c"])
    df.to_csv("voxels.csv", index=False)