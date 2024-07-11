def evaluate_review(dataset_object):
    review = dataset_object['text']
    response = llama_prompt(generate_prompt(input, review))
    dataset_object['Model Prediction'] = 1 if response == 'pos' else 0
    
    # AI failed to return a valid response
    if (response != 'pos' and response != 'neg'):
        #print(response)
        #print("AI DUMB")
        return dataset_object
    
    # AI returned a prediction that matches the true value    
    if ((response == 'pos' and dataset_object['label'] == 0) or
        (response == 'neg' and dataset_object['label'] == 1 )):
        #print(response)
        #print("AI RIGHT")
        return dataset_object
    
    # AI returned a prediction, but it was wrong
    #print("AI WRONG")
    #print(response)
    return dataset_object

results = IMDB_dataset.map(evaluate_review)
print(results)