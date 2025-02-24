import json
import os

def check_duplicates_in_json(file_path):
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"文件 {file_path} 不存在，请检查路径是否正确！")
        return
    
    data = json.dumps(open(file_path, 'r',encoding='utf-8').read(),ensure_ascii=False)
    # with open(file_path, 'r',encoding='utf-8') as file:
    #         data = json.load(file)
    # 尝试读取 JSON 文件
    # try:
    #     with open(file_path, 'r', encoding='utf-8') as file:
    #         data = json.load(file)
    # except UnicodeDecodeError:
    #     print("检测到文件编码可能不是 UTF-8，尝试使用 GBK 编码读取...")
    #     try:
    #         with open(file_path, 'r', encoding='gbk') as file:
    #             data = json.load(file)
    #     except UnicodeDecodeError as e:
    #         print(f"读取文件时出错：{e}")
    #         print("无法确定文件编码，请检查文件编码格式！")
    #         return
    # except json.JSONDecodeError as e:
    #     print(f"读取 JSON 文件时出错：{e}")
    #     return
    # except Exception as e:
    #     print(f"读取文件时出错：{e}")
    #     return

    # 提取所有三元组
    print(data)
    exit()
    all_triples = []
    for group in data:
        all_triples.extend(group["triples"])

    # 转换为不可变集合（元组）并去重
    unique_triples = set(tuple(triple) for triple in all_triples)

    # 检查是否有重复
    if len(all_triples) == len(unique_triples):
        print("没有重复的三元组。")
    else:
        print("存在重复的三元组。")
        print("重复的三元组如下：")
        # 找出重复的三元组
        duplicate_triples = [list(triple) for triple in unique_triples if all_triples.count(list(triple)) > 1]
        for triple in duplicate_triples:
            print(triple)

# 指定 JSON 文件路径
file_path = "d:/CUGB/Dataset/2024-Geological-Journal-Entity-Relationship-Dataset/全局去重20250219/xxx.json"  # 修改为你的文件路径
check_duplicates_in_json(file_path)

# 指定 JSON 文件路径
file_path = "./新建文件夹/黑龙江..json"  # 修改为你的文件路径
check_duplicates_in_json(file_path)