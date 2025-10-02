nomes=[
    {"nome":"victor","idade":33},
    {"nome":"larissa","idade":44}
]
procurar=[p['nome'].upper() for p in nomes if p['idade']==33]
print(procurar)
