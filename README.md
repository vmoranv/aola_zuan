# 奥拉星聊天封包生成工具

将聊天语料库转换为奥拉星聊天系统可用的封包格式。

## 使用说明

1. 准备好你的聊天语料库文件,文件应为纯文本格式,每句话占一行。

2. 双击运行 `aola_zuan.py` 脚本:
   ```bash
   python aola_zuan.py
   ```

3. 根据提示,输入以下信息:
   - 语料库文件的完整路径
   - 输出文件名(可选,默认为 `output.txt`)
   - 每句话后的暂停时间,单位为毫秒(可选,默认为1000)

4. 脚本运行完成后,会在同目录下生成转换后的输出文件。文件名为你指定的名称或默认的 `output.txt`。

## 输出格式

转换后的文件为文本格式,每行代表一个封包,格式如下:

```json
|#send={"id":1,"cmd":"extTalk","param":{"t":4,"msg":"这里是聊天内容"}}|
|#time=1000|
```

其中:
- `msg` 字段为聊天内容,如果原文包含引号,会被转义为 `\"`
- `time` 字段为这句话发送后的暂停时间,单位为毫秒

## 注意事项

- 语料库文件必须为UTF-8编码的纯文本格式
- 脚本运行过程中,如果出现错误,会输出错误信息,请根据信息提示进行处理
- 输出文件会覆盖同名文件(如果存在),请注意备份
