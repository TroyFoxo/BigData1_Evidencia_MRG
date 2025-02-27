import pandas as padalustro


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Importe un excel diferente al de la actividad ya que el dataset de canva parece no existir en la pagina
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#Los dataset a importar son archivos CSV, por lo que se va a usar la funcion de pandas (read_csv) 

df_operators = padalustro.read_csv("operators.csv")

df_weapons = padalustro.read_csv("weapons.csv")



#Impresion del csv operators impreso

print("\n\nOPERATORS\n\n" + str(df_operators.head(1)) )


#Impresion del csv weapons impreso

print("\n\nWEAPONS\n\n" + str(df_weapons.head(10)) )