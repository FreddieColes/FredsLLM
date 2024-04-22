import openai



with open('input2.txt', 'r', encoding = 'utf-8') as f:
    training_data = f.read()


model = openai.Model.create(
  model="gpt-3.5-turbo",
  dataset="training_data",
  max_tokens=1000,
  n_epochs=3,
  train_data=training_data  
)

response = openai.Completion.create(
  model="your_model_id",
  prompt="write a romantic conversation",
)