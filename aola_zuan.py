import os

def process_corpus(input_file, output_file, pause_time):
    """
    读取语料库并按指定格式输出，保留原始文本格式
    
    Args:
        input_file: 输入的语料库文件路径
        output_file: 输出文件路径
        pause_time: 每句话后的暂停时间(毫秒)
    """
    try:
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 处理每一行并写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in lines:
                line = line.strip()  # 移除行首尾空白字符
                if not line:  # 跳过空行
                    continue
                
                # 处理文本中的引号，避免JSON格式错误
                line = line.replace('"', '\\"')
                
                # 构建输出格式
                output_line = f'|#send={{"id":1,"cmd":"extTalk","param":{{"t":4,"msg":"{line}"}}}}|\n|#time={pause_time}|\n'
                f.write(output_line)
                
        print(f"处理完成！共处理了 {len([l for l in lines if l.strip()])} 行语料")
        print(f"输出文件: {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"处理过程中出现错误: {e}")

def main():
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 通过交互方式获取输入文件路径
    input_file = input("请输入语料库文件的完整路径: ").strip()
    
    # 获取输出文件名
    output_filename = input("请输入输出文件名 (默认为 output.txt): ").strip()
    if not output_filename:
        output_filename = "output.txt"
    
    # 获取暂停时间
    pause_time = input("请输入每句话后的暂停时间(毫秒，默认为1000): ").strip()
    if not pause_time or not pause_time.isdigit():
        pause_time = "1000"
    
    # 构建输出文件的完整路径（保存在脚本目录下）
    output_file = os.path.join(script_dir, output_filename)
    
    # 处理文件
    process_corpus(input_file, output_file, pause_time)

if __name__ == "__main__":
    main()