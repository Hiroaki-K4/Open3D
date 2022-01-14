import open3d as o3d


print("Testing IO for point cloud ...")
pcd = o3d.io.read_point_cloud("../../Open3D/examples/test_data/fragment.pcd")
print(pcd)
o3d.io.write_point_cloud("copy_of_fragment.pcd", pcd)

print("Testing IO for meshes ...")
mesh = o3d.io.read_triangle_mesh("../../Open3D/examples/test_data/knot.ply")
print(mesh)
o3d.io.write_triangle_mesh("copy_of_knot.ply", mesh)

print("Testing IO for images ...")
img = o3d.io.read_image("../../Open3D/examples/test_data/lena_color.jpg")
print(img)
o3d.io.write_image("copy_of_lena_color.jpg", img)