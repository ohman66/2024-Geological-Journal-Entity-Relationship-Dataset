import json

# 假设原始数据存储在json文件中
input_file = '黑龙江.jsonl'
output_file = 'annotations_cleaned.json'

# 读取原始数据
with open(input_file, 'r', encoding='utf-8') as file:
    # 读取整个文件内容
    data = file.read()

# 将文件内容分割成多个JSON对象
json_objects = data.split('\n')

# 存储唯一的三元组关系
unique_relations = {}

# 处理每个JSON对象
for json_obj in json_objects:
    if json_obj.strip():  # 确保JSON对象不为空
        item = json.loads(json_obj)
        
        text_id = item['id']
        entities = item['entities']
        relations = item['relations']
        
        # 存储当前文本的唯一关系
        unique_relations[text_id] = {}
        
        for relation in relations:
            key = (relation['from_id'], relation['to_id'], relation['type'])
            
            # 检查是否已经存在相同的三元组关系
            if key not in unique_relations[text_id]:
                unique_relations[text_id][key] = relation
            else:
                # 删除重复的三元组关系
                relations.remove(relation)

# 将处理后的数据写回文件
with open(output_file, 'w', encoding='utf-8') as file:
    for json_obj in json_objects:
        if json_obj.strip():  # 确保JSON对象不为空
            item = json.loads(json_obj)
            # 重新构建relations列表
            item['relations'] = list(unique_relations[item['id']].values())
            file.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f"Cleaned data has been written to {output_file}")