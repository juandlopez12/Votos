n = int(input())
candidatos= {}
votos=1
for i in range(n):
  nombres=input()
  if nombres in candidatos: 
    candidatos[nombres]=candidatos[nombres]+1
    
  else:
    candidatos[nombres]=votos


valor_votos=0

for ind,vot in candidatos.items():
  if vot>valor_votos:
    ganador=ind
    valor_votos=vot

  elif vot==valor_votos:
    ganador="Empate"

print(ganador) 