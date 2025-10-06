# geometric_validation.py
import open3d as o3d
import numpy as np

def hausdorff_distance(ref_path, model_path):
    ref = np.asarray(o3d.io.read_point_cloud(ref_path).points)
    model = np.asarray(o3d.io.read_point_cloud(model_path).points)
    dist_ref = np.min(np.linalg.norm(ref[:, None, :] - model[None, :, :], axis=2), axis=1)
    dist_model = np.min(np.linalg.norm(model[:, None, :] - ref[None, :, :], axis=2), axis=1)
    return max(np.max(dist_ref), np.max(dist_model))

if __name__ == "__main__":
    print("Hausdorff distance:", hausdorff_distance("reference.ply", "ai_model.ply"))
