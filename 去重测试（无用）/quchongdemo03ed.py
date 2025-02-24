import json
import os

def process_json_file(file_path):
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"文件 {file_path} 不存在，请检查路径是否正确！")
        return

    # 尝试读取 JSON 文件
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except UnicodeDecodeError:
        print("检测到文件编码可能不是 UTF-8，尝试使用 GBK 编码读取...")
        try:
            with open(file_path, 'r', encoding='gbk') as file:
                data = json.load(file)
        except UnicodeDecodeError as e:
            print(f"读取文件时出错：{e}")
            print("无法确定文件编码，请检查文件编码格式！")
            return
    except json.JSONDecodeError as e:
        print(f"读取 JSON 文件时出错：{e}")
        return
    except Exception as e:
        print(f"读取文件时出错：{e}")
        return

    # 提取所有三元组并记录首次出现的位置
    all_triples = []
    first_occurrence = {}
    for group in data:
        for triple in group["triples"]:
            triple_tuple = tuple(triple)
            if triple_tuple not in first_occurrence:
                first_occurrence[triple_tuple] = len(all_triples)
            all_triples.append(triple_tuple)

    # 分离保留的三元组和删除的三元组
    retained_triples = set(first_occurrence.keys())
    deleted_triples = [list(triple) for triple in all_triples if triple not in retained_triples]

    # 重新构建处理后的数据结构
    processed_data = []
    for group in data:
        new_group = {"triples": []}
        for triple in group["triples"]:
            triple_tuple = tuple(triple)
            if triple_tuple in retained_triples:
                new_group["triples"].append(triple)
        if new_group["triples"]:  # 如果组内没有三元组，则不保留该组
            processed_data.append(new_group)

    # 保存处理后的数据到新文件
    output_file_name = os.path.basename(file_path).replace(".json", "_quchong.json")
    output_file_path = os.path.join(os.path.dirname(file_path), output_file_name)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(processed_data, output_file, ensure_ascii=False, indent=4)
    print(f"处理后的数据已保存到 {output_file_path}")

    # 保存删除的三元组到新文件
    delete_file_name = "delete.json"
    delete_file_path = os.path.join(os.path.dirname(file_path), delete_file_name)
    delete_data = [{"triples": deleted_triples}]
    with open(delete_file_path, 'w', encoding='utf-8') as delete_file:
        json.dump(delete_data, delete_file, ensure_ascii=False, indent=4)
    print(f"被删除的三元组已保存到 {delete_file_path}")

# 指定 JSON 文件路径
file_path = "./新建文件夹/黑龙江三元组.json"  # 修改为你的文件路径
process_json_file(file_path)