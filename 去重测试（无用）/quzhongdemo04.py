import json

# 读取 JSON 文件
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# 删除重复的三元组
def remove_duplicate_triples(data):
    seen_triples = set()  # 用于存储已经出现过的三元组
    result = []  # 用于存储处理后的数据

    for group in data:
        unique_triples = []
        for triple in group["triples"]:
            triple_tuple = tuple(triple)  # 将三元组转换为元组，方便比较
            if triple_tuple not in seen_triples:
                seen_triples.add(triple_tuple)
                unique_triples.append(triple)
        result.append({"triples": unique_triples})

    return result

# 写入 JSON 文件
def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 主函数
def main():
    input_file_path = './新建文件夹/内蒙古三元组.json'  # 输入文件路径
    output_file_path = './新建文件夹/内蒙古三元组_output.json'  # 输出文件路径

    # 读取 JSON 文件
    data = read_json_file(input_file_path)

    # 删除重复的三元组
    processed_data = remove_duplicate_triples(data)

    # 写入处理后的数据到新的 JSON 文件
    write_json_file(output_file_path, processed_data)

    print(f"处理完成，结果已保存到 {output_file_path}")

# 运行主函数
if __name__ == "__main__":
    main()