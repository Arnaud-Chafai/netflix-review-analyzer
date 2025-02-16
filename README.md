<p align="center">
  <img src="https://github.com/Arnaud-Chafai/netflix-review-analyzer/blob/main/Diagrams/Netflix_2015_logo.svg.png?raw=true" alt="Netflix Logo" width="600">
</p>

# Sistema de Recomendación de Películas y Series de Netflix con LLM y NLP.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2.3-darkblue?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.2.2-013243?style=flat-square&logo=numpy&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.28.1-43B02A?style=flat-square&logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12.3-3B5A9A?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.0-black?style=flat-square&logo=flask&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=flat-square&logo=fastapi&logoColor=white)

---

## 🎬 Descripción del Proyecto

Este sistema permite **recomendar series y películas de Netflix de manera inteligente**, combinando **web scraping de reseñas reales**, **procesamiento de lenguaje natural con LLM** y **algoritmos de clustering**.  

El valor diferencial radica en su capacidad para analizar **miles de comentarios auténticos de usuarios**, extrayendo **opiniones reales** en lugar de basarse en sinopsis o puntuaciones generales. Gracias al modelo **LLM**, genera un **resumen con consenso inteligente**, identificando **aspectos positivos y negativos** sobre cada título recomendado.  

A través de **clustering con KMeans**, el sistema agrupa películas y series en función de sus características, permitiendo generar recomendaciones **personalizadas y precisas** según las preferencias del usuario.  

Además, cuenta con una **interfaz web interactiva**, que facilita el acceso a las recomendaciones y permite conocer la percepción real del público sobre cada título.  

---


### 🔍 Web Scraping de reseñas y Proceso ETL

- Se implementó **web scraping en batch** con **Selenium** y **BeautifulSoup**, iterando de manera programada para extraer información clave de películas y series en **IMDb**.
- Se recopilaron más de **80,000 comentarios reales**, asegurando una base de datos rica y representativa.
- Para optimizar el proceso, se identificaron **títulos faltantes** mediante la comparación entre los títulos ya scrapeados y los presentes en el dataset principal utilizado para el clustering. Esto permitió planificar nuevas rondas de scraping en **bloques iterativos**.

---

### 🔄 Proceso ETL: Extracción, Transformación y Carga  

#### 1. Extracción  
- ✔ Recolección de datos estructurados y no estructurados desde IMDb en múltiples lotes.  
- ✔ Control iterativo para garantizar la cobertura completa de títulos relevantes.  

#### 2. Transformación  
- ✔ Limpieza profunda de datos, eliminación de valores faltantes y normalización de la información.  
- ✔ Homogeneización del formato de comentarios y establecimiento de reglas para películas con pocas reseñas.  

#### 3. Carga  
- ✔ Almacenamiento de los datos procesados en **DataFrames de Pandas** para su posterior análisis y generación de recomendaciones.  

---

Este enfoque iterativo permitió una **recolección eficiente, escalable y precisa**, asegurando una base sólida para el sistema de recomendación.  



<img src="https://github.com/Arnaud-Chafai/netflix-review-analyzer/blob/main/Diagrams/ETL.jpg?raw=true" alt="Diagrama ETL" width="425" height="470">
</p>

---

### 🎯 Algoritmo de Recomendación con Clustering

- Se utilizó **KMeans** para agrupar películas y series en **clusters de características similares**, basándose en:
  - Género
  - Popularidad
  - Puntuaciones de usuarios y otras muchas variables.
- Gracias a este modelo, el sistema **no solo recomienda títulos basados en similitud de géneros, sino también en preferencias más profundas del usuario**.

---

### 🔄 Flujo de Interacción del Usuario

#### 1. Ingreso de Preferencias  
- ✔ El usuario introduce **dos títulos** de series o películas de su elección.  

#### 2. Recomendación Personalizada  
- ✔ El algoritmo de **clustering (KMeans)** analiza las características de los títulos ingresados y sugiere **una opción dentro del mismo clúster**.  

#### 3. Análisis de Opiniones Reales  
- ✔ Se extraen **comentarios auténticos de usuarios** desde IMDb, asociados al título recomendado.  

#### 4. Síntesis con LLM  
- El modelo **LLM** procesa las reseñas y genera un **resumen inteligente**, destacando:  
   - 📢 **Opinión general del público**.  
   - 😀 **Aspectos positivos más relevantes**.  
   - ❌ **Aspectos negativos más destacados**.  


<img src="https://github.com/Arnaud-Chafai/netflix-review-analyzer/blob/main/Diagrams/Deployment.jpg?raw=true" alt="Interfaz Web" width="425">
</p>


---

## 🌐 Despliegue del Sistema

- Se desarrolló una **interfaz web interactiva** utilizando **Flask**, priorizando la experiencia del usuario.
- Funcionalidades principales:
  - **Entrada de preferencias:** Selección de dos títulos favoritos.
  - **Salida de recomendación:** Un título sugerido basado en clustering.
  - **Análisis de reseñas:** Resumen generado por el modelo **LLM** con un consenso de opiniones.



<img src="https://github.com/Arnaud-Chafai/netflix-review-analyzer/blob/main/Diagrams/Demostración.gif?raw=true" 
     alt="Demostración del Proyecto" width="450" />
</p>


---

###🎓 Trabajo de Fin de Máster  

Este proyecto es el **Trabajo de Fin de Máster en Data Science e Inteligencia Artificial de Immune Technology Institute**, desarrollado en colaboración con:  

#### 🤝 Colaboradores  
- **Alfonso Gragera** → Desarrollo del modelo de **clustering KMeans**.  
- **Miguel Ángel Rojo** → Análisis exploratorio de datos (**EDA**) en **Power BI**.  
