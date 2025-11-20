# codigo principal
from codigo_hija import Botella_contenido

# Crear un objeto
# codigo hija
botella1 = Botella_contenido("plastico", "600ml", "cilíndrica", "transparente con etiqueta", True, "Marca Pesi")
botella2 = Botella_contenido("vidreo", "500ml", "cilindrica", "transparente sin etiqueta", True, "Marca Cocacola")

# Mostrar información y usar métodos

# botella 1
print("contebido de botella 1 🍾")
botella1.mostrar_info()
botella1.contener_liquidos()
botella1.cierre_hermetico()
botella1.compatibilidad_bebidas("fría")
botella1.reutilizar()
print("")
#botella 2
print("contebido de botella 2 🍾")
botella2.mostrar_info()
botella2.contener_liquidos()
botella2.cierre_hermetico()
botella2.compatibilidad_bebidas("fría")
botella2.reutilizar()