TP-Link SDK 类型标注补丁

如果你已经有 TP-Link SDK 的运行库，但缺少类型提示，可以直接用这里的文件补上。

怎么用：
把当前目录里的 `tplink` 文件夹覆盖到现有 SDK 的根目录。

这些文件不会改动原本的运行时代码，
只是往 `tplink/sdk` 下面补充 `.pyi` 和 `py.typed`，
这样 IDE 补全、跳转和类型检查会正常很多。

覆盖后目录大致如下：

tplink/
  sdk/
    __init__.pyi
    IPCDevice.pyi
    IPCDeviceContext.pyi
    TPOpenNative.pyi
    TPOpenSDK.pyi
    TPPlayer.pyi
    TPSDKContext.pyi
    py.typed

说明：
适配 Python 3.6.8 的 typing 语法。
