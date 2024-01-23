from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length = 100, null = False, blank = True)
    data_criacao = models.DateTimeField(auto_now_add = True )
    data_entrega = models.DateField(null = False, blank = True)
    data_fim = models.DateField(null = True, blank = True)
   
    def __str__(self):
        return self.titulo