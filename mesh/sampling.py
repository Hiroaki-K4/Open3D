import numpy as np
import open3d as o3d
import copy
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
from Open3D.examples.python import open3d_example as o3dtut


mesh = o3d.geometry.TriangleMesh.create_sphere()
mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh])
pcd = mesh.sample_points_uniformly(number_of_points=500)
o3d.visualization.draw_geometries([pcd])

mesh = o3dtut.get_bunny_mesh()
mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh])
pcd = mesh.sample_points_uniformly(number_of_points=500)
o3d.visualization.draw_geometries([pcd])