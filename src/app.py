from http import server
import db
from models.admin import Admin
from models.classroom import Classroom
from models.server import Server
import os

class Application:
    def __init__(self):
        db.init_db()
        self.session = db.Session()

    def create_classroom(self):
        name = input("Nom de la salle : ")
        classroom = Classroom(name=name)
        self.session.add(classroom)
        self.session.commit()
        print("Salle créée avec succès.")

    def get_classrooms(self):
        classrooms = self.session.query(Classroom).all()
        if not classrooms: 
            print("Aucune classe enregistrée.")
            return
        for classroom in classrooms:
            print(classroom)

    def create_admin(self):
        name = input("Nom de l'administrateur : ")
        admin = Admin(name = name)
        self.session.add(admin)
        self.session.commit()
        print("Administrateur créé.")

    def get_admins(self):
        admins = self.session.query(Admin).all()
        if not admins: 
            print("Aucun Administrateur enregistré.")
            return
        for admin in admins:
            print(admin)

    def create_server(self):
        name = input("Nom du serveur : ")
        server = Server(name=name)
        self.session.add(server)
        self.session.commit()
        print(f"Serveur '{name}' créé avec succès.")
    
    def get_servers(self):
        servers = self.session.query(Server).all()
        if not servers: 
            print("Aucun Serveur enregistrée.")
            return
        for server in servers:
            print(server)

    def link_server_to_classroom(self):
        servers = self.session.query(Server).filter(Server.classroom_id == None).all()
        if not servers:
            print("Aucun serveur non attribué à une salle.")
            return
        print("Serveurs disponibles :")
        for srv in servers:
            print(f"{srv.id}. {srv.name}")
        server_id = int(input("ID du serveur à lier : "))
        server = self.session.get(Server, server_id)
        if not server:
            print("Serveur non trouvé.")
            return

        self.get_classrooms()
        classroom_id = int(input("ID de la salle : "))
        classroom = self.session.get(Classroom, classroom_id)
        if not classroom:
            print("Salle non trouvée.")
            return
        server.classroom = classroom
        server.classroom_id = classroom_id
        self.session.commit()
        print(f"Serveur '{server.name}' assigné à la salle '{classroom.name}'.")

    def link_server_to_admin(self):
        servers = self.session.query(Server).filter(Server.admin_id == None).all()
        if not servers:
            print("Aucun serveur non attrbué.")
            return
        print("Serveurs disponibles :")
        for server in servers:
            print(f"{server.id}. {server.name}")

        server_id = int(input("ID du server : "))
        server = self.session.get(Server, server_id)
        if not server:
            print("Serveur non trouvé.")
            return
        
        self.get_admins()
        admin_id = int(input("ID de l’administrateur : "))
        admin = self.session.get(Admin, admin_id)
        if not admin:
            print("Administrateur non trouvé.")
            return
        server.admin = admin
        server.admin_id = admin_id
        self.session.commit()
        print(f"Serveur '{server.name}' assigné à l'administrateur '{admin.name}'.")
            
    def get_server_by_admin(self):
        admins = self.session.query(Admin).all()
        if not admins: 
            print("Aucune Administrateur enregistré.")
            return
        for admin in admins:
            print(f"\nAdministrateur: {admin.name}")
            servers = self.session.query(Server).filter_by(id=admin.id).all()
            if not servers:
                print("Aucun serveur géré.")
            else:
                for server in servers:
                    print(f" - {server.name} (Salle: {server.classroom.name if server.classroom else 'Non attribuée'})")

    def get_classroom_servers(self):
        classrooms = self.session.query(Classroom).all()
        if not classrooms:
            print("Aucune salle disponible.")
            return
        print("Salles existantes :")
        for classroom in classrooms:
            print(f"{classroom.id}. {classroom.name}")
        self.get_classrooms()
        try:
            classroom_id = int(input("ID de la salle à consulter : "))
            classroom = self.session.get(Classroom, classroom_id)
            if not classroom:
                print("Salle introuvable.")
                return
            servers = self.session.query(Server).filter_by(id=classroom_id).all()
            print(f"\nServeurs dans la salle '{classroom.name}':")
            if not servers:
                print("  Aucun serveur dans cette salle.")
            else:
                for srv in servers:
                    admin_name = srv.admin.name if srv.admin else "Aucun"
                    print(f"  - {srv.name} (Administrateur: {admin_name})")
        except ValueError:
            print("Entrée invalide.")

    def menu(self):
        cols = os.get_terminal_size().columns

        while True:
            print("")
            print("=== MENU PRINCIPAL ===".center(cols))
            print("1. Créer une salle".center(cols))
            print("2. Créer un administrateur".center(cols))
            print("3. Créer un serveur".center(cols))
            print("4. Lister les salles".center(cols))
            print("5. Lister les administrateurs".center(cols))
            print("6. Lister les Serveurs".center(cols))
            print("7. Rattacher un serveur à une salle".center(cols))
            print("8. Rattacher un serveur à un administrateur".center(cols))
            print("9. Lister pour chaque admin les serveurs gérés".center(cols))
            print("10. Lister les serveurs d'une salle".center(cols))
            print("0. Quitter".center(cols))
            print("--- END MENU ---".center(cols))
            print()

            choice = input(">>> Votre choix : ").strip()
            match choice:
                case "1": self.create_classroom()
                case "2": self.create_admin()
                case "3": self.create_server()
                case "4": self.get_classrooms()
                case "5": self.get_admins()
                case "6": self.get_servers()
                case "7": self.link_server_to_classroom()
                case "8": self.link_server_to_admin()
                case "9": self.get_server_by_admin()
                case "10": self.get_classroom_servers()
                case "0": break
                case _ : print("Choix invalide. Essayez encore.")