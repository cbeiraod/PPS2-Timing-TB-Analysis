from typing import Tuple, Dict, Optional, List, Union
from dataclasses import dataclass
from sampiclyser.sensor_hitmaps import SensorSpec

@dataclass
class RunInformation:
    name: str
    trigger_mode: str
    data_format: str
    trigger_channels: Optional[Union[Tuple, int]] = None
    thresholds: Optional[Dict[int, float]] = None
    comment: Optional[str] = None
    metadata: Optional[dict] = None

    def __post_init__(self):
        if self.trigger_channels is not None:
            if type(self.trigger_channels) == int:
                tmp = self.trigger_channels
                self.trigger_channels = tuple(i for i in range(tmp.bit_length()) if (tmp & (1 << i)))
                print(self.trigger_channels)

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


lgad_board_10ch_connections = {
    1:[(4,0)],
    2:[(4,1), (4,2), (3,1), (3,2)],
    3:[(2,0), (2,1)],
    4:[(1,1)],
    5:[(0,0)],
    6:[(0,3), (1,3), (2,3)],
    7:[(0,4), (1,4), (2,4), (3,4)],
    8:[(2,2)],
    9:[(3,3)],
    10:[(4,4)],
}