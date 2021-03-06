# Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

NEED_TO_FIX_OP_LIST = [
    'elementwise_mul',
    'elementwise_div',
    'fused_elemwise_activation',
    'bilinear_tensor_product',
    'conv2d_transpose',
    'depthwise_conv2d_transpose',
    'grid_sampler',
    'hierarchical_sigmoid',
    'lstmp',
    'margin_rank_loss',
    'matmul',
    'mul',
    'scatter',
    'smooth_l1_loss',
    'soft_relu',
    'squared_l2_distance',
    'tree_conv',
    'cvm',
]
