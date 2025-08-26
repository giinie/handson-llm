from transformers import pipeline

pipe = pipeline("text-generation", model="openai-community/gpt2", device="cpu")
# device="cpu" --> CPU 사용 (혹은 -1)
# device="mps" --> Mac Apple GPU
# device=0 --> GPU 0번 사용 (혹은 "cuda:0")
# device="cuda" --> GPU 사용

print(pipe("A rectangle has a perimeter of 20 cm. If the length is 6 cm, what is the width?", max_new_tokens=200))