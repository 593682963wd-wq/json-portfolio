# 显式内容作品集

保留原注册表统计，个人履历/照片与构建产物全部去除；新增独立参数化页面，按调用方JSON渲染且自动转义。

## 使用

Python 3.11+。在本目录建立独立虚拟环境：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python cli.py example.json
.venv/bin/python -m unittest discover -v
```

`example.json`从零编写，仅含虚构输入。可以显式提供自己的同结构JSON文件。输出默认为终端；`--output result.json`使用独占创建，避免覆盖已有结果。CLI失败退出码2。

## 数据与边界

不发现本机账号、不读取环境中的模型密钥、不发送消息、不请求远端数据。只处理调用方明确传入的文件、记录或参数。合成示例不代表任何实际业务结果。页面为通用重写版，不是个人履历的直接公开；没有原照片、视频、私人项目列表和工具启动地址。启动Web预览：`PORT=8091 python3 app.py`。

## 发布状态

本项目源码采用 MIT 许可证，见 LICENSE。依赖按各自上游许可使用，安装的依赖/模型/字体/媒体不随此源码目录分发。

## 2026-11-08 候选修订

- 统计函数显式接收当前请求tools，不修改全局注册表。
- 内容文件明确UTF-8读取。

使用包内合成样例复跑；发布集合根目录的 `verify_release.py --project personal-portfolio` 会依次执行测试和首次使用命令。原有版本的测试计数属于当时记录，本轮汇总以集合验证报告为准。

Docker默认只向 `127.0.0.1` 发布端口；扩大监听需在显式环境中设置 `BIND_ADDRESS`，并按真实入口设置 `PUBLIC_ORIGIN` 和访问保护。脚本不自动提供认证。
