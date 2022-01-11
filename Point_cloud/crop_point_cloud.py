import numpy as np
import open3d as o3d


print("Load a polygon volume and use it to crop the original point cloud")
pcd = o3d.io.read_point_cloud("../../Open3D/examples/test_data/fragment.ply")
vol = o3d.visualization.read_selection_polygon_volume("../../Open3D/examples/test_data/Crop/cropped.json")
chair = vol.crop_point_cloud(pcd)
o3d.visualization.draw_geometries([chair],
                                  zoom=0.7,
                                  front=[0.5439, -0.2333, -0.8060],
                                  lookat=[2.4615, 2.1331, 1.338],
                                  up=[-0.1781, -0.9708, 0.1608])