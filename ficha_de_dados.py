def espaco():
  print(' ');

nome = 'Arian Weslley';
sobrenome = 'dos Santos do Carmo';
idade = 20;
ano_nascimento = 2001;
maior_de_idade = idade >= 18;
resultado_maior_de_idade_portugues = 0;

if(maior_de_idade == True):
  resultado_maior_de_idade_portugues = 'Sim';
else:
  resultado_maior_de_idade_portugues = 'Não';


espaco();
print('Nome Completo:', nome, sobrenome);
espaco();
print('Idade:', idade);
espaco();
print('Nascimento:', ano_nascimento);
espaco();
print('É maior de idade:',  resultado_maior_de_idade_portugues);