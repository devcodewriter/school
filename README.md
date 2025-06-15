# school
Assignment at ESTM

# 🖥️ Gestion d'Infrastructure – Projet Python (ORM + SQLite)

Ce projet est une application console permettant de gérer :
- des **salles** (classrooms),
- des **administrateurs**,
- des **serveurs**,
avec des relations entre eux, le tout structuré avec **SQLAlchemy** et **SQLite**.

---

## 📚 Fonctionnalités

✅ Créer et lister des salles  
✅ Créer et lister des administrateurs  
✅ Créer des serveurs  
✅ Lier un serveur à une salle  
✅ Lier un serveur à un administrateur  
✅ Lister tous les serveurs d’une salle donnée  
✅ Lister les serveurs gérés par chaque administrateur  

---

## 🧱 Architecture du projet

```
school/
│
├── .gitignore 
|-─ README.md 
├── requirements.txt
├── school.db # Fichier SQLite généré automatiquement
├── src/ 
│ ├── app.py # Logique des opérations métiers
│ ├── db.py
│ ├── main.py # Point d'entrée avec menu interactif
│ ├── models/
| │     ├── admin.py
│ │     ├── classroom.py
│ │     ├── server.py
│ ├── repository/
│       ├── base.py # Base SQLAlchemy
```

### Crée un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows
```
### Installe les dépendances

```bash
pip install -r requirements.txt
```

## ▶️ Utilisation

Exécute l'application avec :

```bash
python src/main.py
```
Un menu interactif s'affichera avec les différentes options.

## 📝 Licence
Ce projet est libre d’usage dans un cadre pédagogique.