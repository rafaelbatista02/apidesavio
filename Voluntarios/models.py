from django.db import models
from smart_selects.db_fields import ManyToManyField, ChainedForeignKey, ForeignKey




class Voluntirio(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, null=False)
    bairro = models.CharField(max_length=50, null=False)
    cidade = models.CharField(max_length=50, null=False)
   
    def __str__(self):
        return self.nome 

class Estado(models.Model):
    Est = [(('SP', 'SÃO PAULO'),
    ('RJ', 'RIO DE JANEIRO'))]

    def __str__(self):
        return self.Est

class Cidade(models.Model):
    Cid1 = [(('SP', 'CAPITAL'),
    ('SP', 'BARUERI'))]

    OP = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Est

class Cidade2(models.Model):
    Cid2 = [(('RJ', 'CAPITAL'),
    ('RJ', 'COPACABANA'))]

    OP2 = models.ForeignKey(Estado, on_delete=models.CASCADE)
    RESUL = models.ManyToManyField(Cidade)

    def __str__(self):
        return self.Est



    


    

    

   
    
    
   
  