from typing import Optional

from tplink.sdk.IPCDevice import IPCDevice
from tplink.sdk.TPOpenNative import SDKReqCallback

class IPCDeviceContext:
    def __init__(self) -> None: ...
    def destroyDev(self, dev: IPCDevice) -> None: ...
    def initDev(self, ip: str, port: int) -> int: ...
    def reqConnectDev(self, dev: IPCDevice, callback: Optional[SDKReqCallback]) -> int: ...
    def reqGetVideoPort(self, dev: IPCDevice, callback: Optional[SDKReqCallback]) -> int: ...
    def reqLogin(self, dev: IPCDevice, user: str, pwd: str, callback: Optional[SDKReqCallback]) -> int: ...
    def reqMotorMoveBy(
        self,
        dev: IPCDevice,
        callback: Optional[SDKReqCallback],
        iXCoord: int,
        iYCoord: int,
        iChannelID: int,
    ) -> int: ...
    def reqMotorMoveTo(
        self,
        dev: IPCDevice,
        callback: Optional[SDKReqCallback],
        iXCoord: int,
        iYCoord: int,
        iChannelID: int,
    ) -> int: ...
    def reqMotorMoveZoom(
        self,
        dev: IPCDevice,
        callback: Optional[SDKReqCallback],
        iDirection: int,
        iChannelID: int,
    ) -> int: ...
    def reqMotorMoveZoomTo(
        self,
        dev: IPCDevice,
        callback: Optional[SDKReqCallback],
        fMultiple: int,
        iChannelID: int,
    ) -> int: ...
    def reqMotorStatus(self, dev: IPCDevice, callback: Optional[SDKReqCallback], iChannelID: int) -> int: ...
