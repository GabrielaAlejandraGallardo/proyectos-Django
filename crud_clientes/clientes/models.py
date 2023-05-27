from django.db import models


# Create your models here.
class Clientes(models.Model):
    id=models.AutoField(primary_key=True)
    nom= models.CharField(max_length=40,verbose_name='Nombre')
    ap= models.CharField(max_length=40,verbose_name='Apellido')
    dir= models.TextField(null=True,max_length=40,verbose_name='Dirección')
    foto=models.ImageField(upload_to='imagenes/',verbose_name='foto',null=True)
    
    def __str__(self):
        fila="Id:"+str(self.id)+"-"+"Nombre:"+self.nom+"-"+"Apellido:"+self.ap
        return fila
        return super().__str__()
    def delete(self, using=None,keep_parent=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()