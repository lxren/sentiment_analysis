from transformers import BertTokenizer
from array import array 
import os

def tokenize():

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    TRUNCATE_LENGTH = 200

    def tocken_func (dataset_obj):
        return tokenizer(dataset_obj['text'], padding = 'max_length', max_length = TRUNCATE_LENGTH, truncation = True)

    train_dataset = df.map(tocken_func, batched = True)
    
    folder_path = 'data/interim'
    bert_dataset_export = os.path.join(folder_path, 'tokenized_data.csv')
    df.to_csv(bert_dataset_export, index=False)
    
    print(f"Data exported to {bert_dataset_export}")

    
if __name__ == '__main__':
    tokenize()