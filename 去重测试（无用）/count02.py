import json

# 读取 JSON 文件
def read_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# 统计三元组关系
def count_relationships(data):
    relationship_count = {}
    total_count = 0

    for group in data:
        triples = group.get("triples", [])
        for triple in triples:
            if len(triple) == 3:  # 确保是有效的三元组
                relationship = triple[1]  # 获取关系
                if relationship in relationship_count:
                    relationship_count[relationship] += 1
                else:
                    relationship_count[relationship] = 1
                total_count += 1

    return relationship_count, total_count

# 主函数
def main():
    file_path = "./新建文件夹/内蒙古三元组_output.json"  # 替换为你的 JSON 文件路径
    data = read_json_file(file_path)
    relationship_count, total_count = count_relationships(data)

    # 输出每种关系对应的三元组数量
    print("每种关系对应的三元组数量：")
    for relationship, count in relationship_count.items():
        print(f"关系 '{relationship}'：{count} 个三元组")

    # 输出总数量
    print(f"\n总三元组数量：{total_count}")

# 运行主函数
if __name__ == "__main__":
    main()