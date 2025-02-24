import json

# 打开并加载 JSON 文件
def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# 统计三元组数量
def count_triples(data):
    total_triples = 0
    for item in data:
        triples = item.get("triples", [])
        total_triples += len(triples)
    return total_triples

# 主程序
if __name__ == "__main__":
    # 替换为你的 JSON 文件路径
    file_path = "./新建文件夹/黑龙江._quchong.json"
    
    # 加载 JSON 数据
    try:
        data = load_json_file(file_path)
        # 统计三元组数量
        total_triples = count_triples(data)
        print(f"总三元组数量: {total_triples}")
    except FileNotFoundError:
        print(f"文件未找到，请检查路径是否正确: {file_path}")
    except json.JSONDecodeError:
        print("JSON 文件格式错误，请检查文件内容是否正确。")