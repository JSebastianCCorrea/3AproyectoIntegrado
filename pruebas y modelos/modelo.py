import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from bs4 import BeautifulSoup
import io
import requests

# ---------------------------
# 1. ingestion de la data
# ---------------------------
def obtener_departamentos():
    url = "https://api-colombia.com/api/v1/Department"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for departamento in data:
            print(f"{departamento['id']}: {departamento['name']}")

        return data

    except requests.exceptions.HTTPError as errh:
        print("Error HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error de conexión:", errc)
    except requests.exceptions.Timeout as errt:
        print("Tiempo de espera agotado:", errt)
    except requests.exceptions.RequestException as err:
        print("Error inesperado:", err)
    if __name__ == "__main__":
        obtener_departamentos()
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            return df
        else:
            print(f"Error al obtener datos: {response.status_code}")
            return pd.DataFrame()
    
# traemos datos externos para cotejar la información
data_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv'
df = pd.read_csv(data_url)

# reestructuramos para consistencia
df.columns = ['id', 'height', 'weight']

# web scrapping para indicadores socioeconomicos
response = requests.get('https://www.indexmundi.com/g/g.aspx?v=67&c=xx&l=en')
soup = BeautifulSoup(response.content, 'html.parser')
data_table = soup.find_all('table')[1]  
scraped_data = []

for row in data_table.find_all('tr')[1:6]:  #primeras 5 filas
    cols = row.find_all('td')
    if len(cols) > 1:
        country = cols[0].text.strip()
        internet_penetration = cols[1].text.strip()
        scraped_data.append((country, internet_penetration))

scraped_df = pd.DataFrame(scraped_data, columns=['Country', 'Internet_Penetration'])

# ---------------------------
# 2. procesado de la data
# ---------------------------

#corremos Demo
np.random.seed(42)
df_students = pd.DataFrame({
    'id': range(1, 501),
    'exp_years': np.random.choice([0, 1, 2, 3, 5], 500),
    'english_level': np.random.choice(['Básico', 'Intermedio', 'Avanzado'], 500),
    'access_internet': np.random.choice([1, 0], 500, p=[0.85, 0.15]),
    'academic_link': np.random.choice(['Estudiante activo', 'Egresado', 'Graduado'], 500),
    'pref_tech': np.random.choice(['Datos', 'Frontend', 'Backend', 'QA', 'IA'], 500)
})


df_model = pd.get_dummies(df_students, columns=['english_level', 'academic_link', 'pref_tech'], drop_first=True)

# ---------------------------
# 3. entrenamiento del Modelo MML
# ---------------------------

df_model['empleabilidad'] = np.where((df_model['exp_years'] > 1) & (df_model['access_internet'] == 1), 1, 0)

X = df_model.drop(columns=['id', 'empleabilidad'])
y = df_model['empleabilidad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# ---------------------------
# 4. evaluación
# ---------------------------

conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()

# ---------------------------
# 5. salida POR consola
# ---------------------------

plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Baja', 'Alta'], yticklabels=['Baja', 'Alta'])
plt.title('Matriz de Confusión - Empleabilidad')
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.tight_layout()
plt.savefig('E:/Tatan/Iudigital/Ingenieria/Proyecto Integrado I/Tercera Actividad/Exportes/matriz_confusion_empleabilidad.png')
plt.close()

# exportamos
report_df.to_csv('E:/Tatan/Iudigital/Ingenieria/Proyecto Integrado I/Tercera Actividad/Exportes/reporte_modelo_empleabilidad.csv')

df_model.head(3)  
