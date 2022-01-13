import numpy as np
import open3d as o3d


print("Recompute the normal of the downsampled point cloud")
pcd = o3d.io.read_point_cloud("../../Open3D/examples/test_data/fragment.ply")
downpcd = pcd.voxel_down_sample(voxel_size=0.05)
downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([downpcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024],
                                  point_show_normal=True)