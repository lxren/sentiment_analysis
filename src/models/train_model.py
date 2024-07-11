
from transformers import BertForSequenceClassification, Trainer, TrainingArguments

def train_model():

    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

    training_args = TrainingArguments(
        output_dir = './results',
        num_train_epochs=2, #total number of training epochs
        per_device_train_batch_size = 16, #batch size per device during training
        warmup_steps = 500, # number of warmup steps for learning rates scheduler
        weight_decay = 0.01, #strength of weight decay
    )

    trainer = Trainer(
        model = model, 
        args = training_args, 
        train_dataset = train_dataset, 
    )

    trainer.train()