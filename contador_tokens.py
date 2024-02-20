import tiktoken

modelo1="gpt-4"
modelo2="gpt-3.5-turbo-1106"

codificador1 = tiktoken.encoding_for_model(modelo1)
lista_tokens = codificador1.encode("Você é um categorizador de produtos.")

codificador2 = tiktoken.encoding_for_model(modelo2)
lista_tokens = codificador2.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))

print(f"Custo para o modelo {modelo1} é de ${(len(lista_tokens)/1000) * 0.3}")
print(f"Custo para o modelo {modelo2} é de ${(len(lista_tokens)/1000) * 0.1}")

print(f"\nO custo do GPT-4 é de {0.03/0.001} vezes maior que o do GPT-3.5 Turbo")
