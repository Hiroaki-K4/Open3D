import numpy as np
import open3d as o3d


print("Downsample the point cloud with a voxel of 0.05")
pcd = o3d.io.read_point_cloud("../Open3D/examples/test_data/fragment.ply")
downpcd = pcd.voxel_down_sample(voxel_size=0.05)
o3d.visualization.draw_geometries([downpcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])