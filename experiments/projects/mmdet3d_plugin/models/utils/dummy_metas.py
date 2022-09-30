import numpy as np
import mmdet3d
from mmdet3d.core.bbox import Box3DMode
dummy_metas = {
            'filename':
                [
                    './data/nuscenes-mini/samples/CAM_FRONT/n008-2018-08-01-15-16-36-0400__CAM_FRONT__1533151606012404.jpg',
                    './data/nuscenes-mini/samples/CAM_FRONT_RIGHT/n008-2018-08-01-15-16-36-0400__CAM_FRONT_RIGHT__1533151606020482.jpg',
                    './data/nuscenes-mini/samples/CAM_FRONT_LEFT/n008-2018-08-01-15-16-36-0400__CAM_FRONT_LEFT__1533151606004803.jpg',
                    './data/nuscenes-mini/samples/CAM_BACK/n008-2018-08-01-15-16-36-0400__CAM_BACK__1533151606037558.jpg',
                    './data/nuscenes-mini/samples/CAM_BACK_LEFT/n008-2018-08-01-15-16-36-0400__CAM_BACK_LEFT__1533151606047405.jpg',
                    './data/nuscenes-mini/samples/CAM_BACK_RIGHT/n008-2018-08-01-15-16-36-0400__CAM_BACK_RIGHT__1533151606028113.jpg'],
            'ori_shape':
                [(900, 1600, 3), (900, 1600, 3), (900, 1600, 3), (900, 1600, 3), (900, 1600, 3), (900, 1600, 3)],
            'img_shape': [(928, 1600, 3), (928, 1600, 3), (928, 1600, 3), (928, 1600, 3), (928, 1600, 3),
                          (928, 1600, 3)],
            'lidar2img': np.array([
                np.array(
                    [
                        [1.24183874e+03, 8.42365994e+02, 3.23211705e+01,
                         -3.52298850e+02],
                        [-1.92578761e+01, 5.36598152e+02, -1.22560916e+03,
                         -6.59581084e+02],
                        [-1.30642598e-02, 9.98461783e-01, 5.38831438e-02,
                         -4.24425250e-01],
                        [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                         1.00000000e+00]
                    ]),
                np.array([[1.36556055e+03, -6.17901360e+02, -4.04668147e+01,
                           -4.62462275e+02],
                          [3.78974590e+02, 3.20574614e+02, -1.23987482e+03,
                           -7.03206488e+02],
                          [8.42873686e-01, 5.37159284e-01, 3.19977155e-02,
                           -6.07699093e-01],
                          [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                           1.00000000e+00]]),
                np.array([[2.97313754e+01, 1.50322419e+03, 7.73240387e+01,
                           -3.05834090e+02],
                          [-3.90347295e+02, 3.19513077e+02, -1.23736952e+03,
                           -6.98964459e+02],
                          [-8.24402853e-01, 5.64486082e-01, 4.14173854e-02,
                           -5.32066886e-01],
                          [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                           1.00000000e+00]]),
                np.array([[-8.03632921e+02, -8.51058636e+02, -2.62834362e+01,
                           -8.76737329e+02],
                          [-1.07101892e+01, -4.45371102e+02, -8.14852408e+02,
                           -7.15059864e+02],
                          [-7.92399222e-03, -9.99207668e-01, -3.90031504e-02,
                           -1.02323356e+00],
                          [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                           1.00000000e+00]]),
                np.array([[-1.18656110e+03, 9.23266341e+02, 5.32908945e+01,
                           -6.16919055e+02],
                          [-4.62619203e+02, -1.02492791e+02, -1.25248341e+03,
                           -5.63772051e+02],
                          [-9.47588605e-01, -3.19477534e-01, 3.15275544e-03,
                           -4.35088669e-01],
                          [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                           1.00000000e+00]]),
                np.array([[2.86267055e+02, -1.46907417e+03, -5.93838024e+01,
                           -2.79432728e+02],
                          [4.44726886e+02, -1.22670252e+02, -1.25041119e+03,
                           -5.97571116e+02],
                          [9.24334036e-01, -3.81566076e-01, -3.73090081e-03,
                           -4.65767734e-01],
                          [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                           1.00000000e+00]])]),
            'pad_shape': [(928, 1600, 3), (928, 1600, 3), (928, 1600, 3), (928, 1600, 3), (928, 1600, 3),
                          (928, 1600, 3)],
            'scale_factor': 1.0,
            'flip': False,
            'pcd_horizontal_flip': False,
            'pcd_vertical_flip': False,
            'box_mode_3d': Box3DMode.LIDAR,
            'box_type_3d': mmdet3d.core.bbox.structures.lidar_box3d.LiDARInstance3DBoxes,
            'img_norm_cfg': {'mean': np.array([103.53, 116.28, 123.675]), 'std': np.array([1., 1., 1.]),
                             'to_rgb': False},
            'sample_idx': 'f4f86af4da3b49e79497deda5c5f223a',
            'prev_idx': '747aa46b9a4641fe90db05d97db2acea',
            'next_idx': '6832e717621341568c759151b5974512',
            'pcd_scale_factor': 1.0,
            'pts_filename': './data/nuscenes-mini/samples/LIDAR_TOP/n008-2018-08-01-15-16-36-0400__LIDAR_TOP__1533151606048630.pcd.bin',
            'scene_token': 'fcbccedd61424f1b85dcbf8f897f9754',
            'can_bus': np.array([6.17934112e+02, 1.63616009e+03, 0.00000000e+00, -9.50877811e-01,
                                 -9.50877811e-01, -9.50877811e-01, -9.50877811e-01, -2.99478711e-01,
                                 -2.97542323e-01, 9.80294093e+00, -4.17617485e-02, -3.51809487e-02,
                                 -6.14407547e-02, 8.41988317e+00, 0.00000000e+00, 0.00000000e+00,
                                 5.65601091e+00, 3.24065554e+02])}
import torch

lss_dummy_metas = [
    torch.tensor([[[ 5.6848e-03, -5.6367e-03,  9.9997e-01],
         [-9.9998e-01, -8.3712e-04,  5.6801e-03],
         [ 8.0507e-04, -9.9998e-01, -5.6413e-03]],

        [[-8.3293e-01, -9.9460e-06,  5.5338e-01],
         [-5.5330e-01,  1.6379e-02, -8.3282e-01],
         [-9.0554e-03, -9.9987e-01, -1.3648e-02]],

        [[ 8.2076e-01, -3.4144e-04,  5.7128e-01],
         [-5.7127e-01,  3.2195e-03,  8.2075e-01],
         [-2.1195e-03, -9.9999e-01,  2.4474e-03]],

        [[ 2.4217e-03, -1.6754e-02, -9.9986e-01],
         [ 9.9999e-01, -3.9591e-03,  2.4884e-03],
         [-4.0002e-03, -9.9985e-01,  1.6744e-02]],

        [[ 9.4776e-01,  8.6657e-03, -3.1887e-01],
         [ 3.1896e-01, -1.3976e-02,  9.4766e-01],
         [ 3.7556e-03, -9.9986e-01, -1.6010e-02]],

        [[-9.3478e-01,  1.5876e-02, -3.5488e-01],
         [ 3.5507e-01,  1.1370e-02, -9.3477e-01],
         [-1.0805e-02, -9.9981e-01, -1.6266e-02]]]),
    torch.tensor([[ 1.7008,  0.0159,  1.5110],
        [ 1.5508, -0.4934,  1.4957],
        [ 1.5239,  0.4946,  1.5093],
        [ 0.0283,  0.0035,  1.5791],
        [ 1.0357,  0.4848,  1.5910],
        [ 1.0149, -0.4806,  1.5624]]),
    torch.tensor([[[1.2664e+03, 0.0000e+00, 8.1627e+02],
         [0.0000e+00, 1.2664e+03, 4.9151e+02],
         [0.0000e+00, 0.0000e+00, 1.0000e+00]],

        [[1.2608e+03, 0.0000e+00, 8.0797e+02],
         [0.0000e+00, 1.2608e+03, 4.9533e+02],
         [0.0000e+00, 0.0000e+00, 1.0000e+00]],

        [[1.2726e+03, 0.0000e+00, 8.2662e+02],
         [0.0000e+00, 1.2726e+03, 4.7975e+02],
         [0.0000e+00, 0.0000e+00, 1.0000e+00]],

        [[8.0922e+02, 0.0000e+00, 8.2922e+02],
         [0.0000e+00, 8.0922e+02, 4.8178e+02],
         [0.0000e+00, 0.0000e+00, 1.0000e+00]],

        [[1.2567e+03, 0.0000e+00, 7.9211e+02],
         [0.0000e+00, 1.2567e+03, 4.9278e+02],
         [0.0000e+00, 0.0000e+00, 1.0000e+00]],

        [[1.2595e+03, 0.0000e+00, 8.0725e+02],
         [0.0000e+00, 1.2595e+03, 5.0120e+02],
         [0.0000e+00, 0.0000e+00, 1.0000e+00]]]),
    torch.tensor([[[ 0.0020,  0.9997,  0.0242],
         [-1.0000,  0.0022, -0.0058],
         [-0.0059, -0.0242,  0.9997]],

        [[ 0.0020,  0.9997,  0.0242],
         [-1.0000,  0.0022, -0.0058],
         [-0.0059, -0.0242,  0.9997]],

        [[ 0.0020,  0.9997,  0.0242],
         [-1.0000,  0.0022, -0.0058],
         [-0.0059, -0.0242,  0.9997]],

        [[ 0.0020,  0.9997,  0.0242],
         [-1.0000,  0.0022, -0.0058],
         [-0.0059, -0.0242,  0.9997]],

        [[ 0.0020,  0.9997,  0.0242],
         [-1.0000,  0.0022, -0.0058],
         [-0.0059, -0.0242,  0.9997]],

        [[ 0.0020,  0.9997,  0.0242],
         [-1.0000,  0.0022, -0.0058],
         [-0.0059, -0.0242,  0.9997]]]),
    torch.tensor([[0.9437, 0.0000, 1.8402],
        [0.9437, 0.0000, 1.8402],
        [0.9437, 0.0000, 1.8402],
        [0.9437, 0.0000, 1.8402],
        [0.9437, 0.0000, 1.8402],
        [0.9437, 0.0000, 1.8402]])

]

