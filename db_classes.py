from typing import Tuple, Dict, Optional, List
from dataclasses import dataclass
from sampiclyser.sensor_hitmaps import SensorSpec

@dataclass
class RunInformation:
    name: str
    trigger_mode: str
    data_format: str
    trigger_channels: Optional[Tuple] = None
    thresholds: Optional[Dict[int, float]] = None
    comment: Optional[str] = None

@dataclass
class ConfigInformation:
    name: str
    sampic_to_board: Dict[str, Dict[int, int]]
    bias_voltage: Dict[str, float]
    power: Dict[str, float]
    power_connections: Dict[str, Tuple]
    sampic_amplifiers: Dict[int, str]
    board_order: List[str]
    sensor_channels: Dict[int, List[Tuple]]

    rotation_units: int = 2
    flip: bool = False

    def __post_init__(self):
        self.board_spec = {}

        for board in self.sampic_to_board:
            self.board_spec[board] = SensorSpec(
                name=board,
                sampic_map=self.sampic_to_board[board],
                geometry=("grouped",
                        self.sensor_channels,
                        5, 5),
                global_rotation_units=self.rotation_units,
                global_flip=self.flip,
            )