# Copyright The Caikit Authors
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
"""Data structures for text object detection in images."""

# Standard
from typing import List

# Third Party
from py_to_proto.dataclass_to_proto import Annotated, FieldNumber

# First Party
from caikit.core import DataObjectBase, dataobject
from caikit.interfaces.common.data_model import ProducerId
import alog

# Local
from .image_segmentation import ObjectSegment

log = alog.use_channel("DATAM")

# Image coordinates - TODO: Probably should standardize what we use for these...
@dataobject(package="caikit_data_model.caikit_computer_vision")
class Point2f(DataObjectBase):
    x: Annotated[float, FieldNumber(1)]
    y: Annotated[float, FieldNumber(2)]


@dataobject(package="caikit_data_model.caikit_computer_vision")
class Point2d(DataObjectBase):
    x: Annotated[int, FieldNumber(1)]
    y: Annotated[int, FieldNumber(2)]


@dataobject(package="caikit_data_model.caikit_computer_vision")
class BoundingBox(DataObjectBase):
    xmin: Annotated[int, FieldNumber(1)]
    xmax: Annotated[int, FieldNumber(2)]
    ymin: Annotated[int, FieldNumber(3)]
    ymax: Annotated[int, FieldNumber(4)]


@dataobject(package="caikit_data_model.caikit_computer_vision")
class AnomalyRegion(DataObjectBase):
    score: Annotated[float, FieldNumber(1)]
    # Bounding box and primary focus area of the detected anomaly;
    # note that these coordinates are relative to the detected object.
    box: Annotated[BoundingBox, FieldNumber(2)]
    anomaly_hotspot: Annotated[Point2d, FieldNumber(3)]


@dataobject(package="caikit_data_model.caikit_computer_vision")
class Anomaly(DataObjectBase):
    score: Annotated[float, FieldNumber(1)]
    anomaly_threshold: Annotated[float, FieldNumber(2)]
    detail_data: Annotated[str, FieldNumber(3)]
    regions: Annotated[List[AnomalyRegion], FieldNumber(4)]


@dataobject(package="caikit_data_model.caikit_computer_vision")
class DetectedObject(DataObjectBase):
    score: Annotated[float, FieldNumber(1)]
    label: Annotated[str, FieldNumber(2)]
    box: Annotated[BoundingBox, FieldNumber(3)]
    ### Optional segmentation information
    # list of pixel coordinates representing the segmentation mask of the object.
    object_segments: Annotated[List[Point2f], FieldNumber(4)]
    # Optional run-length encoding of the object being described.
    rle: Annotated[str, FieldNumber(5)]
    ### Optional anomaly detection information
    anomaly: Annotated[Anomaly, FieldNumber(6)]


@dataobject(package="caikit_data_model.caikit_computer_vision")
class ObjectDetectionResult(DataObjectBase):
    detected_objects: Annotated[List[DetectedObject], FieldNumber(1)]
    producer_id: Annotated[ProducerId, FieldNumber(2)]


@dataobject(package="caikit_data_model.caikit_computer_vision")
class ObjectDetectionTrainSet(DataObjectBase):
    img_dir_path: str
    labels_file: str
