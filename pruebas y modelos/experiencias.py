import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Simular dataset
np.random.seed(42)
n = 200
df = pd.DataFrame({
    "experiencia_TI": np.random.choice(["Sí", "No"], n),
    "nivel_ingles": np.random.choice(["Básico", "Intermedio", "Avanzado"], n),
    "acceso_internet": np.random.choice(["Sí", "No"], n),
    "tipo_programa": np.random.choice(["Ingeniería", "Tecnología", "Técnico"], n),
    "interes_proyectos": np.random.choice(["Sí", "No"], n),
    "empleabilidad": np.random.choice(["Alta", "Media", "Baja"], n)
})

# Preprocesamiento
df_encoded = pd.get_dummies(df.drop("empleabilidad", axis=1))
y = df["empleabilidad"]
X_train, X_test, y_train, y_test = train_test_split(df_encoded, y, test_size=0.3, random_state=42)

# Modelo
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Resultados
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()

# Gráfica de Matriz de Confusión
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d",
            xticklabels=["Alta", "Media", "Baja"],
            yticklabels=["Alta", "Media", "Baja"])
plt.title("Matriz de Confusión - Empleabilidad IU Jobly")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.tight_layout()
plt.savefig("/mnt/data/iu_jobly_matriz_confusion.png")
plt.show()