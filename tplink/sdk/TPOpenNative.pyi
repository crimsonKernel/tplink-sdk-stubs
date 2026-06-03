from ctypes import Structure
from typing import Any, Callable, ClassVar, Optional

class SDKIPCReqResponse(Structure):
    mReqID: int
    mError: int
    mRval: int
    def __init__(self) -> None: ...

SDKReqCallback = Callable[[int, SDKIPCReqResponse, int, int], None]
SDKPlayerChangeQualityCallback = Callable[[int, int], None]
SDKPlayerPlayPausedCallback = Callable[[int], None]
SDKPlayerPlayStartCallback = Callable[[int], None]
SDKPlayerPlayStopCallback = Callable[[int, int], None]
SDKPlayerPlayTimeCallback = Callable[[int, int], None]
SDKPlayerReceiveDataCallback = Callable[[int, Any, int], None]
SDKPlayerRecordDurationCallback = Callable[[int, int], None]
SDKPlayerRecordStartCallback = Callable[[int], None]
SDKPlayerRecordStopCallback = Callable[[int, int, Any], None]
SDKPlayerSnapshotCallback = Callable[[int, int, Any], None]

DEFAULT_MODE: int

class SDKPlayerCallbackContext:
    def __init__(self) -> None: ...

class TPOpenNative:
    IPC_DEF_MEDIA_EVENT_MOTION: ClassVar[int]
    IPC_DEF_MEDIA_EVENT_TIME: ClassVar[int]
    IPC_DEV_LIST_TYPE_ALL: ClassVar[int]
    IPC_DEV_LIST_TYPE_DIRECT: ClassVar[int]
    IPC_DEV_LIST_TYPE_INVALID: ClassVar[int]
    IPC_DEV_LIST_TYPE_LOCAL: ClassVar[int]
    IPC_DEV_LIST_TYPE_ONBOARD: ClassVar[int]
    IPC_DEV_LIST_TYPE_REMOTE: ClassVar[int]
    IPC_DEV_TYPE_IPC: ClassVar[int]
    IPC_DEV_TYPE_NONE: ClassVar[int]
    IPC_DEV_TYPE_NVR: ClassVar[int]
    IPC_DOWNLOAD_STATUS_COMPLETED: ClassVar[int]
    IPC_DOWNLOAD_STATUS_FAILED: ClassVar[int]
    IPC_DOWNLOAD_STATUS_INITED: ClassVar[int]
    IPC_DOWNLOAD_STATUS_QUEUED: ClassVar[int]
    IPC_DOWNLOAD_STATUS_REMOVED: ClassVar[int]
    IPC_DOWNLOAD_STATUS_RUNNING: ClassVar[int]
    IPC_DOWNLOAD_STATUS_STOPPED: ClassVar[int]
    IPC_DOWNLOAD_STATUS_STOPPING: ClassVar[int]
    IPC_EC_AGAIN: ClassVar[int]
    IPC_EC_CANCELED: ClassVar[int]
    IPC_EC_CERTIFICATE_INVALID: ClassVar[int]
    IPC_EC_DEV_NOT_FOUND: ClassVar[int]
    IPC_EC_EXIT: ClassVar[int]
    IPC_EC_GENERAL: ClassVar[int]
    IPC_EC_INSUFFICIENT_SPACE: ClassVar[int]
    IPC_EC_NET_ERROR: ClassVar[int]
    IPC_EC_NOT_IMPLEMENTED: ClassVar[int]
    IPC_EC_NOT_SUPPORTED: ClassVar[int]
    IPC_EC_OK: ClassVar[int]
    IPC_EC_PERMISSION: ClassVar[int]
    IPC_EC_REJECTED: ClassVar[int]
    IPC_EC_RVAL: ClassVar[int]
    IPC_EC_TIMEOUT: ClassVar[int]
    TPPLAYER_DISPLAY_MODE_FISHEYE_180D: ClassVar[int]
    TPPLAYER_DISPLAY_MODE_FISHEYE_360D: ClassVar[int]
    TPPLAYER_DISPLAY_MODE_FISHEYE_CALIB: ClassVar[int]
    TPPLAYER_DISPLAY_MODE_FISHEYE_CYLINDER: ClassVar[int]
    TPPLAYER_DISPLAY_MODE_FISHEYE_LONGITUDE: ClassVar[int]
    TPPLAYER_DISPLAY_MODE_FISHEYE_WIN_PLANE_TOP: ClassVar[int]
    TPPLAYER_DISPLAY_MODE_FISHEYE_WIN_PLANE_TOP_QUAD: ClassVar[int]
    TPPLAYER_DISPLAY_MODE_FISHEYE_WIN_PLANE_WALL: ClassVar[int]
    TPPLAYER_DISPLAY_MODE_ORIGIN: ClassVar[int]
    TPPLAYER_DISPLAY_MOUSEEVENT_CLICK: ClassVar[int]
    TPPLAYER_DISPLAY_MOUSEEVENT_DOUBLE_CLICK: ClassVar[int]
    TPPLAYER_DISPLAY_MOUSEEVENT_MOVE: ClassVar[int]
    TPPLAYER_DISPLAY_MOUSEEVENT_PRESS: ClassVar[int]
    TPPLAYER_DISPLAY_MOUSEEVENT_RELEASE: ClassVar[int]
    TPPLAYER_DISPLAY_MOUSEEVENT_WHEEL: ClassVar[int]
    TPPLAYER_DISPLAY_MOUSE_LEFTBUTTON: ClassVar[int]
    TPPLAYER_DISPLAY_MOUSE_MIDDLEBUTTON: ClassVar[int]
    TPPLAYER_DISPLAY_MOUSE_RIGHTBUTTON: ClassVar[int]
    TPPLAYER_PLAYBACK_EVENT_MOTION: ClassVar[int]
    TPPLAYER_PLAYBACK_EVENT_TIMING: ClassVar[int]
    TPPLAYER_PLAY_AUTH_FAILED: ClassVar[int]
    TPPLAYER_PLAY_DEIVCE_EXCEPTION: ClassVar[int]
    TPPLAYER_PLAY_DEVICE_ID_NOT_EXIST: ClassVar[int]
    TPPLAYER_PLAY_DEVICE_OFFLINE: ClassVar[int]
    TPPLAYER_PLAY_DEVICE_PERMISSION_DENIED: ClassVar[int]
    TPPLAYER_PLAY_DEVICE_UNBIND: ClassVar[int]
    TPPLAYER_PLAY_ERROR: ClassVar[int]
    TPPLAYER_PLAY_FINISHED: ClassVar[int]
    TPPLAYER_PLAY_FREQUENT_REQUEST: ClassVar[int]
    TPPLAYER_PLAY_INSUFFICIENT_BANDWIDTH: ClassVar[int]
    TPPLAYER_PLAY_INVALID_CHANNEL: ClassVar[int]
    TPPLAYER_PLAY_NO_INTERNET_CONNECTION: ClassVar[int]
    TPPLAYER_PLAY_OK: ClassVar[int]
    TPPLAYER_PLAY_OVER_TIME_LIMIT: ClassVar[int]
    TPPLAYER_PLAY_PARAMETER_ERROR: ClassVar[int]
    TPPLAYER_PLAY_QUALITY_HD: ClassVar[int]
    TPPLAYER_PLAY_QUALITY_NONE: ClassVar[int]
    TPPLAYER_PLAY_QUALITY_VGA: ClassVar[int]
    TPPLAYER_PLAY_RANGE_EXCEEDED: ClassVar[int]
    TPPLAYER_PLAY_REQUEST_TIMEOUT: ClassVar[int]
    TPPLAYER_PLAY_SEARCHVIDEO_STORAGEERROR: ClassVar[int]
    TPPLAYER_PLAY_SERVER_INTERNAL_ERROR: ClassVar[int]
    TPPLAYER_PLAY_SERVER_PERMISSION_DENIED: ClassVar[int]
    TPPLAYER_PLAY_SERVICE_UNAVAILABLE: ClassVar[int]
    TPPLAYER_PLAY_SESSION_UNAVAILABLE: ClassVar[int]
    TPPLAYER_PLAY_SHARE_EXPIRED: ClassVar[int]
    TPPLAYER_PLAY_STORAGE_ERRORS: ClassVar[int]
    TPPLAYER_PLAY_SUPPORT_QUALITY_NUM: ClassVar[int]
    TPPLAYER_PLAY_SYSLOCKED: ClassVar[int]
    TPPLAYER_PLAY_TIME_OUT: ClassVar[int]
    TPPLAYER_PLAY_TOKEN_EXPIRED: ClassVar[int]
    TPPLAYER_PLAY_TOO_MANY_CLIENT: ClassVar[int]
    TPPLAYER_PLAY_TOO_MANY_REQUESTS: ClassVar[int]
    TPPLAYER_PLAY_UNSUPPORT_FORMAT: ClassVar[int]
    TPPLAYER_PLAY_UNSUPPORT_VIDEO_CODEC_TYPE: ClassVar[int]
    TPPLAYER_RECORD_END_WITH_FULL_DISK: ClassVar[int]
    TPPLAYER_RECORD_ERROR: ClassVar[int]
    TPPLAYER_RECORD_FULL_DISK: ClassVar[int]
    TPPLAYER_RECORD_IO_ERROR: ClassVar[int]
    TPPLAYER_RECORD_OK: ClassVar[int]
    TPPLAYER_RECORD_TOO_SHORT: ClassVar[int]
    TPPLAYER_RECORD_UNSUPPORT_FORMAT: ClassVar[int]
    TPPLAYER_SNAPSHOT_FAIL: ClassVar[int]
    TPPLAYER_SNAPSHOT_OK: ClassVar[int]
    TPPLAYER_TALK_FULL_DUPLEX: ClassVar[int]
    TPPLAYER_TALK_HALF_DUPLEX: ClassVar[int]

    @staticmethod
    def SDKAppReqStart(pCallback: Optional[SDKReqCallback] = None, pContext: int = 0, bSync: int = 1) -> int: ...
    @staticmethod
    def SDKAppReqStop(pCallback: Optional[SDKReqCallback] = None, pContext: int = 0, bSync: int = 0) -> int: ...
    @staticmethod
    def SDKCreateDevice() -> int: ...
    @staticmethod
    def SDKCreatePlayer(ctx: SDKPlayerCallbackContext) -> int: ...
    @staticmethod
    def SDKDeleteDevice(pDevHandle: int) -> None: ...
    @staticmethod
    def SDKDeletePlayer(pPlayerHandle: int) -> None: ...
    @staticmethod
    def SDKDevGetAlias(pDevHandle: int) -> int: ...
    @staticmethod
    def SDKDevGetHardwareVersion(pDevHandle: int) -> int: ...
    @staticmethod
    def SDKDevGetModel(pDevHandle: int) -> int: ...
    @staticmethod
    def SDKDevGetSoftwareVersion(pDevHandle: int) -> int: ...
    @staticmethod
    def SDKDevGetType(pDevHandle: int) -> int: ...
    @staticmethod
    def SDKDevGetVideoPort(pDevHandle: int) -> int: ...
    @staticmethod
    def SDKDevIsSupportCalibrate(pDevHandle: int, iListType: int = 1, iChannel: int = -1) -> int: ...
    @staticmethod
    def SDKDevIsSupportLensMask(pDevHandle: int, iListType: int = 1, iChannel: int = -1) -> int: ...
    @staticmethod
    def SDKDevIsSupportManualAlarm(pDevHandle: int, iListType: int = 1, iChannel: int = -1) -> int: ...
    @staticmethod
    def SDKDevIsSupportMotor(pDevHandle: int, iListType: int = 1, iChannel: int = -1) -> int: ...
    @staticmethod
    def SDKDevIsSupportPTZ(pDevHandle: int, iListType: int = 1, iChannel: int = -1) -> int: ...
    @staticmethod
    def SDKInitDevice(pDevHandle: int, pcAddress: str, iHttpPort: int) -> int: ...
    @staticmethod
    def SDKPlayerChangeQuality(pPlayerHandle: int, iQuality: int = 1) -> int: ...
    @staticmethod
    def SDKPlayerPause(pPlayerHandle: int) -> int: ...
    @staticmethod
    def SDKPlayerResize(pPlayerHandle: int) -> int: ...
    @staticmethod
    def SDKPlayerResume(pPlayerHandle: int) -> int: ...
    @staticmethod
    def SDKPlayerSeek(pPlayerHandle: int, lSeekTime: int) -> int: ...
    @staticmethod
    def SDKPlayerSnapshot(pPlayerHandle: int, pcFilePath: str) -> int: ...
    @staticmethod
    def SDKPlayerStartPlayback(
        pPlayerHandle: int,
        pDevHandle: int,
        iClientID: int,
        iChannel: int,
        iEventType: int,
        llStartTime: int,
        llEndTime: int,
        hWnd: int,
    ) -> int: ...
    @staticmethod
    def SDKPlayerStartPreview(pPlayerHandle: int, pDevHandle: int, iChannel: int, iQuality: int, hWnd: int) -> int: ...
    @staticmethod
    def SDKPlayerStartRecord(pPlayerHandle: int, pcFilePath: str) -> int: ...
    @staticmethod
    def SDKPlayerStopPlayback(pPlayerHandle: int) -> int: ...
    @staticmethod
    def SDKPlayerStopPreview(pPlayerHandle: int) -> int: ...
    @staticmethod
    def SDKPlayerStopRecord(pPlayerHandle: int) -> int: ...
    @staticmethod
    def SDKReqConnectDev(pDevHandle: int, pCallback: Optional[SDKReqCallback], pContext: int) -> int: ...
    @staticmethod
    def SDKReqGetClientID(pDevHandle: int, pCallback: Optional[SDKReqCallback], pContext: int) -> int: ...
    @staticmethod
    def SDKReqGetVideoPort(pDevHandle: int, pCallback: Optional[SDKReqCallback], pContext: int) -> int: ...
    @staticmethod
    def SDKReqLogin(pDevHandle: int, pCallback: Optional[SDKReqCallback], pContext: int, pcUser: str, pcPwd: str) -> int: ...
    @staticmethod
    def SDKReqMotorMoveBy(
        pDevHandle: int,
        pCallback: Optional[SDKReqCallback],
        pContext: int,
        iXCoord: int,
        iYCoord: int,
        iChannelID: int = -1,
    ) -> int: ...
    @staticmethod
    def SDKReqMotorMoveStep(
        pDevHandle: int,
        pCallback: Optional[SDKReqCallback],
        pContext: int,
        iDirection: int,
        iChannelID: int = -1,
    ) -> int: ...
    @staticmethod
    def SDKReqMotorMoveStop(
        pDevHandle: int,
        pCallback: Optional[SDKReqCallback],
        pContext: int,
        iChannelID: int = -1,
    ) -> int: ...
    @staticmethod
    def SDKReqMotorMoveTo(
        pDevHandle: int,
        pCallback: Optional[SDKReqCallback],
        pContext: int,
        iXCoord: int,
        iYCoord: int,
        iChannelID: int = -1,
    ) -> int: ...
    @staticmethod
    def SDKReqMotorMoveZoom(
        pDevHandle: int,
        pCallback: Optional[SDKReqCallback],
        pContext: int,
        iDirection: int,
        iChannelID: int = -1,
    ) -> int: ...
    @staticmethod
    def SDKReqMotorMoveZoomTo(
        pDevHandle: int,
        pCallback: Optional[SDKReqCallback],
        pContext: int,
        fMultiple: int,
        iChannelID: int = -1,
    ) -> int: ...
    @staticmethod
    def SDKReqMotorStatus(
        pDevHandle: int,
        pCallback: Optional[SDKReqCallback],
        pContext: int,
        iChannelID: int = -1,
    ) -> int: ...
