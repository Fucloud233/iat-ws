# 科大讯飞 语音转文字
> kdxf sound-to-text

本项目使用科大讯飞的[语音转写](https://www.xfyun.cn/doc/asr/voicedictation/API.html)功能，实现语音转文字功能。

## 使用方法

1. 在科大讯飞的开放平台获得APPID和Key，保存在`config.json`中

2. 使用以下命令安装项目依赖（注意使用python3.7版本）

   `pip install -r requirement.txt`

3. 在 `output/sound`中以文件为单位放入wav格式音频
4. 运行`text/main.py`代码

## 文件结构

* output: 输出目录，不同文件类型的输出目录
* test: 测试代码
* text: 语音转文字代码
* video: 视频处理代码
* utils: 一些使用工具（不是核心功能）

```lua
├───output
│   ├───sound
│   │   └───example
│   ├───text
│   └───video
├───test
├───text
├───utils
└───video
```

## 语音转文字

语音转文字是使用在`main.py`中管理核心业务，主要包括一下3个部分

1. `text_transcription.py`: 语音转写，通过科大讯飞的API实现语音转写功能
2. `json_paser`: 对API返回的结果进行解析
3. `text_save`: 保存解析结果

> 注意：`text_dictation`是语音听写部分的代码，由于工作项目没有使用，仅保留没有维护

## 视频处理

本项目使用ffmepg对视频进行处理，如果本机未安装该工具，则无法使用对应功能。

该模块分为两个功能：

1. `sound_convert.py`: 视频与语音转换
2. `sound_spilt.py`: 语音切片