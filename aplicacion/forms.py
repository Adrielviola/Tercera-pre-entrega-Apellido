from django import forms

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar', max_length=100)    
#class notebookform(forms.Form):
# usuario_id = models.ForeignKey(usuario)
 #   marca = forms.CharField()
  #  modelo = forms.CharField()
   # serie = forms.CharField()
    #nombre= forms.CharField()
   # apellido= forms.CharField()
  #  emai=forms.EmailField()

#class BuscanotebookForm(forms.Form):
  #  notebook = forms.CharField()    

#class desktopform(forms.Form):
 #   #usuario_id = models.ForeignKey(usuario)
 #   marca = forms.CharField()
 #   modelo = forms.CharField()
  #  serie = forms.CharField()
  #  nombre= forms.CharField()
  #  apellido= forms.CharField()
  #  emai=forms.EmailField()

#class BuscadesktopForm(forms.Form):
#    desktop = forms.CharField()    

#class aioform(forms.Form):
 #   #usuario_id = models.ForeignKey(usuario)
  #  marca = forms.CharField()
  #  modelo = forms.CharField()
  #  serie = forms.CharField()
  #  nombre= forms.CharField()
  #  apellido= forms.CharField()
  #  emai=forms.EmailField()

#class BuscaaioForm(forms.Form):
#    aio = forms.CharField()

#class celularesform(forms.Form):
 #   marca = forms.CharField()
  #  modelo = forms.CharField()
  #  serie = forms.CharField()
  #  nombre= forms.CharField()
  #  apellido= forms.CharField()
  #  imei=forms.DecimalField()

#class BuscacelularesForm(forms.Form):
#    celulares = forms.CharField()

