# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
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

from dataclasses import dataclass, field

from lerobot.common.cameras import CameraConfig

from ..config import RobotConfig


@RobotConfig.register_subclass("bi_so100_follower")
@dataclass
class BiSO100FollowerConfig(RobotConfig):
    # Port to connect to the left arm
    left_port: str = "/dev/ttyACM2"

    # Port to connect to the right arm
    right_port: str = "/dev/ttyACM3"

    # ID for the left arm (used to load calibration)
    left_id: str = "left_follower"

    # ID for the right arm (used to load calibration)
    right_id: str = "right_follower"

    disable_torque_on_disconnect: bool = True

    # `max_relative_target` limits the magnitude of the relative positional target vector for safety purposes.
    # Set this to a positive scalar to have the same value for all motors, or a list that is the same length as
    # the number of motors in your follower arms.
    max_relative_target: int | None = None

    # cameras
    cameras: dict[str, CameraConfig] = field(default_factory=dict)

    # Set to `True` for backward compatibility with previous policies/dataset
    use_degrees: bool = False
