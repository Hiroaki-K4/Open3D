from math import dist
import numpy as np
import open3d as o3d


pcd = o3d.io.read_point_cloud("../../Open3D/examples/test_data/fragment.ply")
vol = o3d.visualization.read_selection_polygon_volume("../../Open3D/examples/test_data/Crop/cropped.json")
chair = vol.crop_point_cloud(pcd)

dists = pcd.compute_point_cloud_distance(chair)
dists = np.asarray(dists)
ind = np.where(dists > 0.01)[0]
pcd_without_chair = pcd.select_by_index(ind)
o3d.visualization.draw_geometries([pcd_without_chair],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])