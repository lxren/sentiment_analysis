import evaluate
import numpy as np
test_dataset = load_dataset('IMDB', split='test[0:1000]')
test_dataset = test_dataset.shuffle()

test_dataset = test_dataset.map(tocken_func, batched = True)
print(test_dataset[0])

metric = evaluate.load('accuracy')

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    print(eval_pred)
    return metric.compute(predictions = predictions, references = labels)

training_args = TrainingArguments(
    output_dir = './evaluation',
    evaluation_strategy = 'epoch', 
    num_train_epochs = 2, #total number of training epochs
    per_device_train_batch_size = 16, #batch size per device during training
    per_device_eval_batch_size = 64, #batch size for evaluation
    warmup_steps = 500, # number of warmup steps for learning rates scheduler
    weight_decay = 0.01, #strength of weight decay
)

trainer = Trainer(
    model = model, 
    args = training_args, 
    train_dataset = train_dataset, 
    eval_dataset = test_dataset, 
    compute_metrics = compute_metrics,
)

trainer.train()