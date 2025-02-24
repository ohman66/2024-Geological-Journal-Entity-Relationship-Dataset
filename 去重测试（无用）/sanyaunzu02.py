import os
import json

def process_jsonl_file(file_path):
    results = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            text = data['text']
            entities = data['entities']
            relations = data['relations']
            
            # 构建从实体ID到具体名称的映射
            entity_id_to_name = {entity['id']: text[entity['start_offset']:entity['end_offset']] for entity in entities}
            
            # 构建三元组列表
            triples = []
            for relation in relations:
                from_id = relation['from_id']
                to_id = relation['to_id']
                relation_type = relation['type']
                
                # 检查实体ID是否存在于映射中
                if from_id in entity_id_to_name and to_id in entity_id_to_name:
                    triple = [entity_id_to_name[from_id], relation_type, entity_id_to_name[to_id]]
                    triples.append(triple)
                else:
                    print(f"Warning: Missing entity ID in {file_path} - from_id: {from_id}, to_id: {to_id}")
            
            # 将文本内容和三元组添加到结果列表
            results.append({
                "input": text,
                "output": triples
            })
    
    return results

def process_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.jsonl'):
            file_path = os.path.join(directory_path, filename)
            results = process_jsonl_file(file_path)
            
            # 创建输出文件名
            output_filename = filename[:-6] + '_output.json'  # 修改输出文件名格式
            output_file_path = os.path.join(directory_path, output_filename)
            
            # 将处理结果写入输出文件
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                json.dump(results, output_file, ensure_ascii=False, indent=4)
                print(f"Processed {file_path} and saved to {output_file_path}")

# 指定目录路径
directory_path = './新建文件夹/'
process_directory(directory_path)