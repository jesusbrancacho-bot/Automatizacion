import pandas as pd


/* Leer data frame */
df=pd.read_csv("datos.csv")

/* Imprimimos la cantidad de filas que nos muestra el df*/
print("Filas iniciales:", len(df))

/* Elimina todos los registros nulos del df*/
df = df.dropna()


/*Transforma las columnas en minuscula y borra los espacios q pueden haber*/
df.columns = df.columns.str.lower().str.strip()


/*creamos un archivo csv con el df limpio*/
df.to_csv("datos_limpios.csv", index=False)

/*imprimimos las lines finales*/
print("Filas finales:", len(df))
print("Archivo generado correctamente")
