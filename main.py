import datetime
import time
import db
from passlib.context import CryptContext
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
password_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
dico = {
    "The Last of Us Part II": "https://www.youtube.com/embed/eaaQ17YY4NA",          
    "God of War": "https://www.youtube.com/embed/8O4uT214kak",
    "Spider-Man Miles Morales": "https://www.youtube.com/embed/3Ywq3PIKAYo",
    "Uncharted 4 A Thief's End": "https://www.youtube.com/embed/hh5HV4iic1Y",
    "Ghost of Tsushima": "https://www.youtube.com/embed/VIaTAJxtS3Q",
    "Horizon Zero Dawn": "https://www.youtube.com/embed/wzx96gYA8ek",
    "Spider-Man": "https://www.youtube.com/embed/3R2uvJqWeVg",
    "The Last of Us": "https://www.youtube.com/embed/OQpdSVF_k_w",
    "God of War Ragnarok": "https://www.youtube.com/embed/Ut7FkcpYL74",
    "Halo Master Chief Collection": "https://www.youtube.com/embed/ZDvYJGquXgE",
    "Forza Motorsport 7": "https://www.youtube.com/embed/9aAr5blVy0g",
    "Fable III": "https://www.youtube.com/embed/QJnT3u01k18",
    "Ori and the Blind Forest": "https://www.youtube.com/embed/cklw-Yu3moE",
    "Sea of Thieves": "https://www.youtube.com/embed/1z48qvGsA_0",
    "Quantum Break": "https://www.youtube.com/embed/ruY1eT9bXiw",
    "State of Decay 2": "https://www.youtube.com/embed/qjLOFZjGClY", 
    "Cuphead": "https://www.youtube.com/embed/4TjUPXAn2Rg",
    "Sunset Overdrive": "https://www.youtube.com/embed/W5ddpEO1CK4", 
    "Microsoft Flight Simulator": "https://www.youtube.com/embed/TYqJALPVn0Y",
    "Battlefield V": "https://www.youtube.com/embed/fb1MR85XFOc", 
    "Star Wars Jedi Fallen ORDER": "https://www.youtube.com/embed/0GLbwkfhYZk",
    "The Sims 4": "https://www.youtube.com/embed/DyNv44QR14g", 
    "FIFA23": "https://www.youtube.com/embed/0tIW1X2dv0c",
    "Assassins Creed Valhalla": "https://www.youtube.com/embed/rKjUAWlbTJk",
    "Far Cry 6": "https://www.youtube.com/embed/-IJuKT1mHO8",
    "Watch Dogs Legion": "https://www.youtube.com/embed/qxkM9ddLkl8",
    "Rainbow Six Siege": "https://www.youtube.com/embed/YlVf0XCybmg",
    "Call of Duty Warzone": "https://www.youtube.com/embed/0E44DClsX5Q",
    "World of Warcraft Shadowlands": "https://www.youtube.com/embed/LxBcOfgPeZs",
    "Overwatch": "https://www.youtube.com/embed/FqnKB22pOC0",
    "Diablo III Reaper of Souls": "https://www.youtube.com/embed/rbL-7SKeB6E", 
    "Half-Life 2": "https://www.youtube.com/embed/ID1dWN3n7q4", 
    "Counter-Strike Global Offensive": "https://www.youtube.com/embed/RzZ2bWZ_8Ho",
    "Portal 2": "https://www.youtube.com/embed/0qcED35LL8I",
    "Left 4 Dead 2": "https://www.youtube.com/embed/9XIle_kLHKU",
    "Team Fortress 2": "https://www.youtube.com/embed/N7ZafWA2jd8",
    "Dota 2": "https://www.youtube.com/embed/-cSFPIwMEq4",
    "Half-Life Alyx": "https://www.youtube.com/embed/O2W0N3uKXmo",
    "Artifact": "https://www.youtube.com/embed/cjK81DW0kkw",
    "Counter-Strike Source": "https://www.youtube.com/embed/bvI62FUDpKA",
    "Half-Life": "https://www.youtube.com/embed/5Wavn29LMrs",
    "Gears of War 5": "https://www.youtube.com/embed/q_Qi14S4Djw", 
    "Bulletstorm": "https://www.youtube.com/embed/Tb4uMreeeEo",
    "Shadow Complex": "https://www.youtube.com/embed/j_29XW-eibQ",
    "Infinity Blade": "https://www.youtube.com/embed/I9xNssza4pk",
    "Jazz Jackrabbit": "https://www.youtube.com/embed/1J6TQ_4dSzo",
    "NBA 2K22": "https://www.youtube.com/embed/va83v7wzyHc",
    "BioShock Infinite": "https://www.youtube.com/embed/T9CcbwO9LFk",
    "BORDERlands 3": "https://www.youtube.com/embed/gjLQ2Uj4OPw", 
    "Mafia III": "https://www.youtube.com/embed/kmKOLvnullE",
    "Civilization VI": "https://www.youtube.com/embed/5KdE0p2joJw",
    "Evolve": "https://www.youtube.com/embed/695Z76yw-28", 
    "WWE 2K22": "https://www.youtube.com/embed/NYzxYzM3Rj8",
    "Resident Evil Village": "https://www.youtube.com/embed/tjfTxFzGh3Q",
    "Resident Evil 3 Remake": "https://www.youtube.com/embed/F4Ix4eyNYps",
    "Resident Evil 2 Remake": "https://www.youtube.com/embed/u3wS-Q2KBpk",
    "Resident Evil 7 Biohazard": "https://www.youtube.com/embed/RgYqQsbKn6w",
    "Resident Evil 6": "https://www.youtube.com/embed/8SlXT8JtYSM",
    "Resident Evil 5": "https://www.youtube.com/embed/EUI48f4iWPc",
    "Resident Evil 4": "https://www.youtube.com/embed/2ORc25vZo54",
    "Resident Evil Outbreak": "https://www.youtube.com/embed/bTMurb3xcC8",
    "Resident Evil Code Veronica": "https://www.youtube.com/embed/UgM3q1IJA0c",
    "Resident Evil 3 Nemesis": "https://www.youtube.com/embed/gun-MVEWg40&t=23s",
    "Resident Evil 2": "https://www.youtube.com/embed/kUjLG8ZxuHQ",
    "Resident Evil": "https://www.youtube.com/embed/IjxFtFwY6jk", 
    "Street Fighter V": "https://www.youtube.com/embed/0nFd7Iylj5A",
    "Monster Hunter World": "https://www.youtube.com/embed/SE_FnuD9zJc",
    "Dark Souls III": "https://www.youtube.com/embed/cWBwFhUv1-8",
    "Dragon Ball Z Kakarot": "https://www.youtube.com/embed/mw40u02Ks60",
    "Elden Ring": "https://www.youtube.com/embed/E3Huy2cdih0",
    "Sonic Mania": "https://www.youtube.com/embed/eI4hsOTQZME",
    "Yakuza Like a Dragon": "https://www.youtube.com/embed/cTOAd2fq740",
    "Total War Three Kingdoms": "https://www.youtube.com/embed/4UhSsPhIpqM",
    "Persona 5": "https://www.youtube.com/embed/SKpSpvFCZRw",
    "DOOM (2016)": "https://www.youtube.com/embed/SgSrpnW0EmU",  
    "DOOM Eternal": "https://www.youtube.com/embed/qzp8wZ-HMKk",
    "DOOM 3 BFG Edition": " https://www.youtube.com/embed/bLbFJpVal3M",
    "DOOM (1993)": "https://www.youtube.com/embed/BkaC1-QoraY",
    "DOOM II Hell on Earth": "https://www.youtube.com/embed/p-KIS4Sk76c", 
    "Starfield": "https://www.youtube.com/embed/RDEU8SOtHAI",
    "The Elder Scrolls V Skyrim": "https://www.youtube.com/embed/JSRtYpNRoN0",
    "Fallout 4": "https://www.youtube.com/embed/X5aJfebzkrM",
    "The Evil Within": "https://www.youtube.com/embed/H2qITQHud2I",
    "The Witcher 3 Wild Hunt": "https://www.youtube.com/embed/1-l29HlKkXU", 
    "Cyberpunk 2077": "https://www.youtube.com/embed/UnA7tepsc7s", 
    "The Witcher 2 Assassins of Kings": "https://www.youtube.com/embed/HedLjjlSy3Y",
    "Metal Gear Solid V The Phantom Pain": "https://www.youtube.com/embed/A9JV0EvCkMI",
    "Silent Hill 2": "https://www.youtube.com/embed/dk7JkSArEdQ",
    "Castlevania Symphony of the Night": "https://www.youtube.com/embed/w-x0HgqxdGk", 
    "Metal Gear Solid": "https://www.youtube.com/embed/z7fhvnjo-Hs",
    "Suikoden II": "https://www.youtube.com/embed/NVu_2ydeJzA",
    "Contra Hard Corps": "https://www.youtube.com/embed/qv0Qrl18bVg",
    "Grand Theft Auto V": "https://www.youtube.com/embed/QkkoHAzjnUs",
    "Red Dead Redemption 2": "https://www.youtube.com/embed/eaW0tYpxyp0",
    "Max Payne 3": "https://www.youtube.com/embed/4Uc_dbG7MR8",
    "Bully Scholarship Edition": "https://www.youtube.com/embed/yqkynwFs9Hs",
    "L.A. Noire": "https://www.youtube.com/embed/ZbPxNGh7dto",
    "Grand Theft Auto San Andreas": "https://www.youtube.com/embed/yOzcbtsw_pQ", 
    "Grand Theft Auto IV": "https://www.youtube.com/embed/M80K51DosFo",
    "Star Citizen": "https://www.youtube.com/embed/M7jgxJ_4TJs",
    "Grand Theft Auto VI": "https://www.youtube.com/embed/QdBZY2fkU-0",
    "Baldur's Gate III": "https://www.youtube.com/embed/1T22wNvoNiU"
}

@app.route("/")
def fct_default():
    return redirect(url_for('fct_home'))

@app.route("/home",methods = ['get'])
def fct_home():
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT titre FROM jeu")
            resultat = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT description FROM jeu")
            description_jeu = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT prix FROM jeu")
            description_prix = cur.fetchall()
    return render_template("/home.html", jeu = resultat,description=description_jeu,prix=description_prix)


@app.route("/boutique_date_recente")
def boutique_date_recente():
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT titre FROM jeu ORDER BY date_sortie DESC")
            resultat = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT description FROM jeu ORDER BY date_sortie DESC")
            description_jeu = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT prix FROM jeu ORDER BY date_sortie DESC")
            description_prix = cur.fetchall()
    return render_template("/home.html", jeu = resultat,description=description_jeu,prix=description_prix)

@app.route("/boutique_date_ancienne")
def boutique_date_ancienne():
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT titre FROM jeu ORDER BY date_sortie ")
            resultat = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT description FROM jeu ORDER BY date_sortie ")
            description_jeu = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT prix FROM jeu ORDER BY date_sortie ")
            description_prix = cur.fetchall()
    return render_template("/home.html", jeu = resultat,description=description_jeu,prix=description_prix)

@app.route("/boutique_plus_vente")
def boutique_plus_vente():
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(jeu.id_jeu) as nbr, jeu.titre FROM jeu LEFT JOIN achete ON jeu.id_jeu = achete.id_jeu GROUP BY jeu.id_jeu ORDER BY nbr DESC ")
            resultat = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(jeu.id_jeu) as nbr, jeu.description FROM jeu LEFT JOIN achete ON jeu.id_jeu = achete.id_jeu GROUP BY jeu.id_jeu ORDER BY nbr DESC ")
            description_jeu = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(jeu.id_jeu) as nbr, jeu.prix FROM jeu LEFT JOIN achete ON jeu.id_jeu = achete.id_jeu GROUP BY jeu.id_jeu ORDER BY nbr DESC ")
            description_prix = cur.fetchall()
    return render_template("/home.html", jeu = resultat,description=description_jeu,prix=description_prix)

@app.route("/boutique_moins_vente")
def boutique_moins_vente():
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(jeu.id_jeu) as nbr, jeu.titre FROM jeu LEFT JOIN achete ON jeu.id_jeu = achete.id_jeu GROUP BY jeu.id_jeu ORDER BY nbr  ")
            resultat = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(jeu.id_jeu) as nbr, jeu.description FROM jeu LEFT JOIN achete ON jeu.id_jeu = achete.id_jeu GROUP BY jeu.id_jeu ORDER BY nbr  ")
            description_jeu = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(jeu.id_jeu) as nbr, jeu.prix FROM jeu LEFT JOIN achete ON jeu.id_jeu = achete.id_jeu GROUP BY jeu.id_jeu ORDER BY nbr  ")
            description_prix = cur.fetchall()
    return render_template("/home.html", jeu = resultat,description=description_jeu,prix=description_prix)

@app.route("/boutique_moins_bonne_note")
def boutique_moins_bonne_note():
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT jeu.titre, AVG(commente.note) AS moyenne_note FROM jeu LEFT JOIN commente ON jeu.id_jeu = commente.id_jeu GROUP BY jeu.id_jeu ORDER BY CASE WHEN AVG(commente.note) IS NULL THEN 1 ELSE 0 END, AVG(commente.note) DESC ")
            resultat = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT jeu.description, AVG(commente.note) AS moyenne_note FROM jeu LEFT JOIN commente ON jeu.id_jeu = commente.id_jeu GROUP BY jeu.id_jeu ORDER BY CASE WHEN AVG(commente.note) IS NULL THEN 1 ELSE 0 END, AVG(commente.note) DESC ")
            description_jeu = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT jeu.prix, AVG(commente.note) AS moyenne_note FROM jeu LEFT JOIN commente ON jeu.id_jeu = commente.id_jeu GROUP BY jeu.id_jeu ORDER BY CASE WHEN AVG(commente.note) IS NULL THEN 1 ELSE 0 END, AVG(commente.note) DESC ")
            description_prix = cur.fetchall()
    return render_template("/home.html", jeu = resultat,description=description_jeu,prix=description_prix)

@app.route("/boutique_bonne_note")
def boutique_bonne_note():
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT jeu.*, AVG(commente.note) AS moyenne_note FROM jeu LEFT JOIN commente ON jeu.id_jeu = commente.id_jeu GROUP BY jeu.id_jeu ORDER BY  AVG(commente.note)  ")
            resultat = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT jeu.description, AVG(commente.note) AS moyenne_note FROM jeu LEFT JOIN commente ON jeu.id_jeu = commente.id_jeu GROUP BY jeu.id_jeu ORDER BY  AVG(commente.note)  ")
            description_jeu = cur.fetchall()
        with conn.cursor() as cur:
            cur.execute("SELECT jeu.prix, AVG(commente.note) AS moyenne_note FROM jeu LEFT JOIN commente ON jeu.id_jeu = commente.id_jeu GROUP BY jeu.id_jeu ORDER BY  AVG(commente.note)  ")
            description_prix = cur.fetchall()
    return render_template("/home.html", jeu = resultat,description=description_jeu,prix=description_prix)

@app.route("/bibliotheque")
def bibliotheque():
    if 'pseudo' in session :
        with db.connect() as conn : 
            with conn.cursor() as cur:
                cur.execute("SELECT titre FROM jeu natural JOIN achete WHERE pseudonyme = %s", (session["pseudo"],))
                resultat = cur.fetchall()
            with conn.cursor() as cur:
                cur.execute("SELECT description FROM jeu natural JOIN achete WHERE pseudonyme = %s", (session["pseudo"],))
                description_jeu = cur.fetchall()
            with conn.cursor() as cur:
                cur.execute("SELECT prix FROM jeu natural JOIN achete WHERE pseudonyme = %s", (session["pseudo"],))
                description_prix = cur.fetchall()
        return render_template("bibliotheque.html", jeu = resultat,description=description_jeu,prix=description_prix,name = session['pseudo'])
    else : 
        return redirect(url_for('fct_home'))

@app.route("/jeu/<string:thisjeu>")
def display_jeux(thisjeu):
    pseudo_value = session.get("pseudo", None)
    if thisjeu not in dico:
        return render_template("erreur.html", message = "Pas de jeu")

    if pseudo_value is None:
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM jeu")
                resultat = cur.fetchall()

        for cle, valeur in dico.items():
            if cle == thisjeu:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM jeu WHERE titre = %s",(thisjeu,)) #toutes les infos du jeu en question
                    infos = cur.fetchone()
                    
                    
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM commente WHERE id_jeu = %s",(infos.id_jeu,)) 
                    commentaires = cur.fetchall()

              
                return render_template("jeu_pas_de_compt.html", lien=valeur, commentaires = commentaires) #n'est pas connecté

        return render_template("erreur.html", message = "Ce jeu n'existe pas")
    
    else : 
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id_jeu FROM achete WHERE pseudonyme = %s", (pseudo_value,)) #liste de tous les jeux du joueur
                res = cur.fetchall()

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM jeu") #liste de tous les jeux total
                resultat = cur.fetchall()

        titre = []
        jeu = []

        for i in resultat:
            titre.append([i.titre, i.id_jeu])

        for i in res:
            jeu.append(i[0])

        for cle, valeur in dico.items():
            if cle == thisjeu:
                for i in titre:
                 
                    with conn.cursor() as cur:
                        cur.execute("SELECT id_jeu FROM partage WHERE pseudonyme2 = %s", (pseudo_value,)) #liste de tous les jeux du joueur reçus d'un partage
                        partage = cur.fetchall()

                    lst =[]
                    for j in partage:
                        lst.append(j[0])
                    if i[1] in lst and i[0]==cle:
                        with conn.cursor() as cur:
                            cur.execute("SELECT * FROM jeu WHERE titre = %s",(thisjeu,)) #toutes les infos du jeu en question
                            infos = cur.fetchone()
                        with conn.cursor() as cur:
                            cur.execute("SELECT nom_entreprise FROM entreprise WHERE id_entreprise = %s", (infos.id_entreprise_edit,))
                            res_edit = cur.fetchall()
                        with conn.cursor() as cur:
                            cur.execute("SELECT nom_entreprise FROM entreprise WHERE id_entreprise = %s", (infos.id_entreprise_dev,))
                            res_dev = cur.fetchall()
                        with conn.cursor() as cur:
                            cur.execute("SELECT * FROM commente WHERE id_jeu = %s",(infos.id_jeu,)) 
                            commentaires = cur.fetchall()
                     
                        return render_template("jeu_en_partage_ami.html", lien=valeur, 
                                                 infos = infos, entreprise_edit = res_edit[0].nom_entreprise, 
                                                 entreprise_dev = res_dev[0].nom_entreprise, commentaires = commentaires) #partage le jeu a un ami
            
                    if cle == i[0] and i[1] in jeu: #si nom_jeu = nom_jeu_parmi_tous et id_jeu dans jeu_du_joueur
                        with db.connect() as conn:
                            with conn.cursor() as cur:
                                cur.execute("SELECT *FROM partage")
                                part =cur.fetchall()
                            lst=[]
                            for j in part:
                                lst.append([j[0],j[1],j[2]])
                            for j in lst:
                                if i[1] in j and j[0] == pseudo_value:
                                    with conn.cursor() as cur:
                                        cur.execute("SELECT * FROM jeu WHERE titre = %s",(thisjeu,)) #toutes les infos du jeu en question
                                        infos = cur.fetchone()
                                    with conn.cursor() as cur:
                                        cur.execute("SELECT nom_entreprise FROM entreprise WHERE id_entreprise = %s", (infos.id_entreprise_edit,))
                                        res_edit = cur.fetchall()
                                    with conn.cursor() as cur:
                                        cur.execute("SELECT nom_entreprise FROM entreprise WHERE id_entreprise = %s", (infos.id_entreprise_dev,))
                                        res_dev = cur.fetchall()
                                    with conn.cursor() as cur:
                                        cur.execute("SELECT * FROM commente WHERE id_jeu = %s",(infos.id_jeu,)) 
                                        commentaires = cur.fetchall()

                                    return render_template("jeu_en_partage.html", lien=valeur, num=i[1],
                                                ami=j[1], infos = infos, entreprise_edit = res_edit[0].nom_entreprise, 
                                                entreprise_dev = res_dev[0].nom_entreprise, commentaires = commentaires)
                        
                        with db.connect() as conn:
                            with conn.cursor() as cur:
                                cur.execute("SELECT * FROM est_ami_avec")
                                partage = cur.fetchall()
                            with conn.cursor() as cur:
                                cur.execute("SELECT * FROM partage")
                                part =cur.fetchall()
                            with conn.cursor() as cur:
                                cur.execute("SELECT * FROM achete")
                                achete =cur.fetchall()
                        
                        ami_posede_jeu=[]
                        for j in achete:
                            if i[1]==j[1]:
                                ami_posede_jeu.append(j[0])
                            
                        ami = []
                        for j in partage:
                            if j[0] == pseudo_value:
                                ami.append(j[1])
                            if j[1] == pseudo_value:
                                ami.append(j[0])
                                
                        dejajeu = []
                        for j in part:
                            if i[1]==j[2]:
                                dejajeu.append(j[1])
                        for m in ami:
                            if m in dejajeu:
                                ami.remove(m)
                            if m in ami_posede_jeu:
                                ami.remove(m)
                        with conn.cursor() as cur:
                            cur.execute("SELECT * FROM jeu WHERE titre = %s",(thisjeu,)) #toutes les infos du jeu en question
                            infos = cur.fetchone()
                        with conn.cursor() as cur:
                            cur.execute("SELECT nom_entreprise FROM entreprise WHERE id_entreprise = %s", (infos.id_entreprise_edit,))
                            res_edit = cur.fetchall()
                        with conn.cursor() as cur:
                            cur.execute("SELECT nom_entreprise FROM entreprise WHERE id_entreprise = %s", (infos.id_entreprise_dev,))
                            res_dev = cur.fetchall()
                        with conn.cursor() as cur:
                            cur.execute("SELECT * FROM commente WHERE id_jeu = %s",(infos.id_jeu,)) 
                            commentaires = cur.fetchall()

                       
                        return render_template("jeu_possede.html", lien=valeur, lst=ami, num=i[1],
                                                ami=pseudo_value, infos = infos, entreprise_edit = res_edit[0].nom_entreprise, 
                                                entreprise_dev = res_dev[0].nom_entreprise, commentaires = commentaires) #a le jeu
              

                    
                    if cle == i[0] and i[1] in jeu: #si nom_jeu = nom_jeu_parmi_tous et id_jeu dans jeu_du_joueur
                        with db.connect() as conn:
                            with conn.cursor() as cur:
                                cur.execute("SELECT *FROM partage")
                                part =cur.fetchall()
                            lst=[]
                            for j in part:
                                lst.append([j[0],j[1],j[2]])
                            for j in lst:
                                if i[1] in j and j[1] == pseudo_value:
                                    with conn.cursor() as cur:
                                        cur.execute("SELECT * FROM commente WHERE id_jeu = %s",(infos.id_jeu,)) 
                                        commentaires = cur.fetchall()
                                    return render_template("jeu_en_partage_ami.html", lien=valeur, lst=ami, num=i[1],
                                                ami=pseudo_value, infos = infos, entreprise_edit = res_edit[0].nom_entreprise, 
                                                entreprise_dev = res_dev[0].nom_entreprise, commentaires = commentaires)
                        
                        with db.connect() as conn:
                            with conn.cursor() as cur:
                                cur.execute("SELECT * FROM est_ami_avec")
                                partage = cur.fetchall()
                        ami = []
                        for j in partage:
                            if j[0] == pseudo_value:
                                ami.append(j[1])
                            if j[1] == pseudo_value:
                                ami.append(j[0])
                        with db.connect() as conn:
                            with conn.cursor() as cur:
                                cur.execute(
                                    "SELECT DISTINCT * FROM achete EXCEPT SELECT DISTINCT * FROM achete WHERE id_jeu <> %s",(i[1],)) 
                                partage = cur.fetchall()

                        dejajeu = []
                        for j in partage:
                            dejajeu.append(j[0])
                        for m in ami:
                            if m in dejajeu:
                                ami.remove(m)

                        with conn.cursor() as cur:
                            cur.execute("SELECT * FROM jeu WHERE titre = %s",(thisjeu,)) #toutes les infos du jeu en question
                            infos = cur.fetchone()
                        with conn.cursor() as cur:
                            cur.execute("SELECT nom_entreprise FROM entreprise WHERE id_entreprise = %s", (infos.id_entreprise_edit,))
                            res_edit = cur.fetchall()
                        with conn.cursor() as cur:
                            cur.execute("SELECT nom_entreprise FROM entreprise WHERE id_entreprise = %s", (infos.id_entreprise_dev,))
                            res_dev = cur.fetchall()
                        with conn.cursor() as cur:
                            cur.execute("SELECT * FROM commente WHERE id_jeu = %s",(infos.id_jeu,)) 
                            commentaires = cur.fetchall()
                        return render_template("jeu_possede.html", lien=valeur, nom_jeu=thisjeu, lst=ami, num=i[1],
                                                ami=pseudo_value, infos = infos, entreprise_edit = res_edit[0].nom_entreprise, 
                                                entreprise_dev = res_dev[0].nom_entreprise, commentaires = commentaires) #a le jeu
                    
                    
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM jeu WHERE titre = %s",(thisjeu,)) #toutes les infos du jeu en question
                    infos = cur.fetchone()
                    
                with conn.cursor() as cur:
                    cur.execute("SELECT nom_entreprise FROM entreprise WHERE id_entreprise = %s", (infos.id_entreprise_edit,))
                    res_edit = cur.fetchone()
                with conn.cursor() as cur:
                    cur.execute("SELECT nom_entreprise FROM entreprise WHERE id_entreprise = %s", (infos.id_entreprise_dev,))
                    res_dev = cur.fetchone()
                with conn.cursor() as cur:
                        cur.execute("SELECT * FROM commente WHERE id_jeu = %s",(infos.id_jeu,)) 
                        commentaires = cur.fetchall()
                return render_template("jeu.html", lien=valeur, id_jeu=i[1],infos = infos, entreprise_edit = res_edit.nom_entreprise, 
                                       entreprise_dev = res_dev.nom_entreprise, commentaires = commentaires)

@app.route("/jeu_fin",methods=['POST'])
def fin_partage():
    
    jeu = request.form['invisible']
    with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM partage
                    WHERE (pseudonyme1 = %s AND pseudonyme2 = %s)
                    """,
                    (session["pseudo"], jeu))   
    return redirect (url_for("fct_home"))

@app.route("/jeu_debut", methods=['POST'])
def debut_partage():
    ami_SELECTionne = request.form.get("amis", None)
    jeu = request.form['invisible']
    with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO partage (pseudonyme1, pseudonyme2,id_jeu)
                    VALUES (%s, %s,%s)
                    """,
        (session["pseudo"], ami_SELECTionne,jeu))

    return redirect(url_for("fct_home"))

@app.route("/jeu_achat", methods=['POST'])
def achat_jeux():
    jeu_titre = request.form['invisible']
    
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM jeu WHERE titre = %s", (jeu_titre,))
            infos = cur.fetchone()

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM commente WHERE id_jeu = %s",(infos.id_jeu,)) 
            commentaires = cur.fetchall()
        
    if not infos:
        return render_template("erreur.html", message="Le jeu n'existe pas.")


    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM joueur WHERE pseudonyme = %s", (session["pseudo"],))
            joueur_info = cur.fetchone()

    if not joueur_info:
        return render_template("erreur.html", message="Le joueur n'existe pas.")


    age = datetime.now().year - (joueur_info.date_naissance).year

    if joueur_info.argent < infos.prix:
        return render_template("jeu_pas_argent.html", lien="erreur", commentaires = commentaires)

    if age < infos.age_min:
        

        return render_template("jeu_pas_age.html", lien="erreur", commentaires = commentaires)

    # Effectuer l'achat
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO achete (pseudonyme, id_jeu, date_achat)
                VALUES (%s, %s, %s)
                """,
                (session["pseudo"], infos.id_jeu, datetime.now().strftime("%Y-%m-%d"))
            )
            
            cur.execute(
                """
                UPDATE joueur
                SET argent = %s
                WHERE pseudonyme = %s
                """,
                (joueur_info.argent - infos.prix, session["pseudo"])
            )

    return redirect(url_for("fct_home"))

@app.route("/formulaire")
def form():
    local_time = time.localtime()
    if "pseudo" in session:
        return redirect(url_for('fct_home'))
    if local_time.tm_mon>9:
        if local_time.tm_mday>9:
            datemin= str(local_time.tm_year-13)+"-"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
        else:
            datemin= str(local_time.tm_year-13)+"-"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
    else:
        if local_time.tm_mday>9:
            datemin= str(local_time.tm_year-13)+"-0"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-0"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
        else:
            datemin= str(local_time.tm_year-13)+"-0"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-0"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
    return render_template("inscription.html",datemin= datemax,datemax=datemin)  

@app.route("/compte")
def compte():
    if "pseudo" in session:
        return redirect(url_for('profil'))
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT pseudonyme FROM joueur")
            res = cur.fetchall()
    return render_template("connexion.html",moi=res)  

@app.route("/client ", methods=['POST'])
def inscrit():
    pseudo = request.form.get("pseudo", None)
    if not pseudo:
        return redirect(url_for("compte"))
    session["pseudo"] = pseudo
    return redirect(url_for("fct_home"))

@app.route("/verification_inscrit", methods=['POST'])
def verification_inscrit():
    mail = request.form.get("email", None)  
    motdepasse = request.form.get("motdepasse", None)
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT pseudonyme,motdepasse,email FROM joueur WHERE email= %s",(mail,))
            res = cur.fetchall()
    for row in res:
        d=password_ctx.verify(motdepasse, row[1])
    if d== True and mail == row[2]:
        session["pseudo"] = row[0]
        return redirect(url_for("fct_home"))
    return redirect(url_for("compte"))

@app.route("/verification_formulaire", methods=['POST'])
def verification_formulaire():
    pseudo = request.form.get("pseudo", None)
    email = request.form.get("email", None)
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT pseudonyme, email FROM joueur")
            res = cur.fetchall()
    password_hashed = password_ctx.hash(request.form.get("motdepasse", None))
    nom = request.form.get("nom", None)
    date_naissance = request.form.get("date_naissance", None)
    pseudonymes, emails = zip(*res)
    local_time = time.localtime()
    if local_time.tm_mon>9:
        if local_time.tm_mday>9:
            datemin= str(local_time.tm_year-13)+"-"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
        else:
            datemin= str(local_time.tm_year-13)+"-"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
    else:
        if local_time.tm_mday>9:
            datemin= str(local_time.tm_year-13)+"-0"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-0"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
        else:
            datemin= str(local_time.tm_year-13)+"-0"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-0"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
    if pseudo in pseudonymes:
        return render_template("inscriptionpseudo.html",pseudo=pseudo,nom=nom,email=email,date_naissance=date_naissance,datemin= datemax,datemax=datemin)
    if email in emails:
        return render_template("inscriptionmail.html",pseudo=pseudo,nom=nom,date_naissance=date_naissance,datemin= datemax,datemax=datemin)
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO joueur (pseudonyme, motdepasse, nom, email, date_naissance, argent)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (pseudo, password_hashed, nom, email, date_naissance, 0))
    session["pseudo"] = pseudo
    return redirect(url_for("fct_home"))

@app.route("/deconnexion")
def deconnexion():
    session.pop('pseudo', None)
    return redirect(url_for('fct_home'))

@app.route("/partage")
def partage():
    if 'pseudo' in session:
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT pseudonyme1, titre, description FROM jeu NATURAL JOIN partage WHERE pseudonyme2 = %s", (session["pseudo"],))
                partages = cur.fetchall()
            
        amis = []
        for i in partages:
            amis.append(i[0])

        jeux = [partage[1] for partage in partages]

        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT pseudonyme2, titre, description FROM jeu NATURAL JOIN partage WHERE pseudonyme1 = %s", (session["pseudo"],))
                partagespartoi = cur.fetchall()
        
        amispartage = []
        for i in partagespartoi:
            amispartage.append(i[0])
        
        jeuxpartoi = [partage[1] for partage in partagespartoi]
        descriptionspartoi = [partage[2] for partage in partagespartoi]


        return render_template("partage.html", amis=amis, jeu=jeux, jeupartoi=jeuxpartoi, descriptionpartoi=descriptionspartoi, amispartage=amispartage, name=session['pseudo'])
    else:
        return redirect(url_for('fct_home'))

@app.route("/commente")
def commente():
    if 'pseudo' in session :
        with db.connect() as conn : 
            with conn.cursor() as cur:
                cur.execute("SELECT id_jeu,titre FROM jeu natural JOIN achete WHERE pseudonyme = %s", (session["pseudo"],))
                resultat = cur.fetchall()
            with conn.cursor() as cur:
                cur.execute("SELECT description FROM jeu natural JOIN achete WHERE pseudonyme = %s", (session["pseudo"],))
                description_jeu = cur.fetchall()
            with conn.cursor() as cur:
                cur.execute("SELECT prix FROM jeu natural JOIN achete WHERE pseudonyme = %s", (session["pseudo"],))
                description_prix = cur.fetchall()          
            with conn.cursor() as cur:
                cur.execute("SELECT  pseudonyme ,id_jeu ,note ,commentaire FROM commente WHERE pseudonyme = %s", (session["pseudo"],))
                commente = cur.fetchall()
            comments=[]
            id_jeux=[]
            for row in commente:
                comments.append([row[0],row[1],row[2],row[3]])
                id_jeux.append(row[1])
        return render_template("commente.html", jeu = resultat,description=description_jeu,prix=description_prix,jeux=id_jeux,commente= comments,name = session['pseudo'])
    else : 
        return redirect(url_for('fct_home'))

@app.route("/verification_commente_uptade", methods=['POST'])
def verification_commente():
    jeu = request.form['id_jeu']
    pseudo = request.form['joueur']
    commentaire = request.form.get('texte')
    note = request.form.get('note')
    if commentaire == 'texte':
        commentaire = None
    if note == 'choisir':
        note = None
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE commente
                SET commentaire = %s, note = %s
                WHERE id_jeu = %s AND pseudonyme = %s
                """,
                (commentaire, note, jeu, pseudo,)
            )
    return redirect(url_for('commente'))

@app.route("/verification_commente_creat", methods=['POST'])
def verification_commente_creat():
    jeu = request.form['id_jeu']
    pseudo = request.form['joueur']
    commentaire = request.form.get('texte')
    note = request.form.get('note')
    if commentaire == 'texte':
        commentaire = None
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO commente (pseudonyme,id_jeu,note,commentaire )
                VALUES (%s, %s, %s, %s)
                """,
                (pseudo,jeu,note,commentaire)
            )  
    return redirect(url_for('commente'))

@app.route("/state")
def state():
    if 'pseudo' in session :
        with db.connect() as conn : 
            with conn.cursor() as cur:
                cur.execute("SELECT titre FROM jeu natural JOIN achete WHERE pseudonyme = %s", (session["pseudo"],))
                resultat = cur.fetchall()
            with conn.cursor() as cur:
                cur.execute("SELECT id_jeu FROM jeu natural JOIN achete WHERE pseudonyme = %s", (session["pseudo"],))
                res = cur.fetchall()
            with conn.cursor() as cur:
                cur.execute("SELECT description FROM jeu natural JOIN achete WHERE pseudonyme = %s", (session["pseudo"],))
                description_jeu = cur.fetchall()
            with conn.cursor() as cur:
                cur.execute(" SELECT id_succes,id_jeu_s FROM obtient natural JOIN succes WHERE pseudonyme = %s", (session["pseudo"],))
                succesjoueur = cur.fetchall()
            with conn.cursor() as cur:
                cur.execute(" SELECT id_succes,id_jeu_s FROM  succes")
                succestout = cur.fetchall()
        jeu=[]
        succ=[]
        for i in succestout:
            jeu.append(i.id_jeu_s)
            succ.append(i.id_succes)
        pourcentage=[]
        nbr_succes=[]
        for i in res:
            if (i.id_jeu in jeu):
                 nbr_succes.append([i.id_jeu,0])
                 pourcentage.append([i.id_jeu,0])
            else:
                 nbr_succes.append([i.id_jeu,"NULL"])
                 pourcentage.append([i.id_jeu,"NULL"])
        for i in jeu:
            for j in  nbr_succes:
                if i == j[0]:
                    j[1]+=1 
        for i in succesjoueur:
            for j in pourcentage:
                if i.id_jeu_s == j[0]:
                    j[1]+=1
        pourcentagedesjeux=[]
        for i in pourcentage:
            if i[1]!="NULL":
                for j in nbr_succes:
                    if i[0] == j[0]:
                        pourcentagedesjeux.append((i[1]*100)/j[1])
            else:
                pourcentagedesjeux.append("NULL")
        return render_template("state.html", jeu = resultat,description=description_jeu,pourcentage=pourcentagedesjeux,name = session['pseudo'])
    else : 
        return redirect(url_for('fct_home'))

@app.route("/gestion_payement")
def gestion_payement():
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT argent FROM joueur WHERE pseudonyme = %s", (session["pseudo"],))
            resultat = cur.fetchall()
        res=[]
        for i in resultat:
            res.append (i.argent)
    return render_template("payement.html", prix=res)

@app.route("/montant", methods=['POST'])
def montant():
    with db.connect() as conn : 
        with conn.cursor() as cur:
            cur.execute("SELECT argent FROM joueur WHERE pseudonyme = %s", (session["pseudo"],))
            resultat = cur.fetchall()
        res=[]
        for i in resultat:
            res.append (i.argent)
    return render_template("montant.html", prix=res)

@app.route("/aprovisionnement", methods=['POST'])
def modif_base():
    prix = request.form['prix']
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE joueur
                SET argent = argent + %s
                WHERE pseudonyme = %s
                """,
                (prix,session["pseudo"])
            )
    return redirect(url_for('gestion_payement'))

@app.route("/profil")
def profil():
    local_time = time.localtime()
    if local_time.tm_mon>9:
        if local_time.tm_mday>9:
            datemin= str(local_time.tm_year-13)+"-"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
        else:
            datemin= str(local_time.tm_year-13)+"-"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
    else:
        if local_time.tm_mday>9:
            datemin= str(local_time.tm_year-13)+"-0"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-0"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
        else:
            datemin= str(local_time.tm_year-13)+"-0"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
            datemax= str(local_time.tm_year-113)+"-0"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
    pseudo = session["pseudo"]
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT pseudonyme, nom, email, date_naissance FROM joueur WHERE pseudonyme = (%s)", (pseudo,))
            joueur_info = cur.fetchone() 
    return render_template("profil.html", joueur_info=joueur_info,datemin=datemin,datemax=datemax)

@app.route("/profil", methods=['POST'])
def profil_modification():
    if 'pseudo' in session:
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT pseudonyme,nom,email,date_naissance FROM joueur WHERE pseudonyme = %s", (session["pseudo"],))
                resultat = cur.fetchall()
        error =[]
        bdpseudo =""
        bdemail =""
        bdnom =""
        bddate=""
        for i in resultat:
            bdpseudo = i.pseudonyme
            bdemail = i.email
            bdnom = i.nom
            bddate = i.date_naissance
            

        pseudo = request.form.get("new_pseudo", None)
        email = request.form.get("new_email", None)
        nom = request.form.get("new_nom", None)
        date = request.form.get("new_date_naissance", None)
        mot_de_passe = request.form.get("motdepasse", None)
        if pseudo != bdpseudo:
            error.append("pseudo")
        if email != bdemail:
            error.append("email")
        if nom != bdnom:
            error.append("nom")
        if str(date)!= str(bddate):
            error.append("date")
        if mot_de_passe != "None":
            password_hashed = password_ctx.hash(mot_de_passe)
            with db.connect() as conn:
                    with conn.cursor() as cur:
                        cur.execute(
                            """
                            UPDATE joueur
                            SET motdepasse = %s
                            WHERE pseudonyme = %s
                            """,
                            (password_hashed,session["pseudo"]))  
        for i in error:
            if i == "date":
                with db.connect() as conn:
                    with conn.cursor() as cur:
                        cur.execute(
                            """
                            UPDATE joueur
                            SET date_naissance = %s
                            WHERE pseudonyme = %s
                            """,
                            (date,session["pseudo"]))
            if i == "nom":
                with db.connect() as conn:
                    with conn.cursor() as cur:
                        cur.execute(
                            """
                            UPDATE joueur
                            SET nom = %s
                            WHERE pseudonyme = %s
                            """,
                            (nom,session["pseudo"]))
            if i == "email":
                with db.connect() as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT email FROM joueur")
                        tou_email = cur.fetchall()  # Utilisez fetchall() pour récupérer toutes les lignes
                lst = [emaile[0] for emaile in tou_email]  # Utilisez une compréhension de liste pour extraire les emails
                if email not in lst:
                    with db.connect() as conn:
                        with conn.cursor() as cur:
                            cur.execute(
                                """
                                UPDATE joueur
                                SET email = %s
                                WHERE pseudonyme = %s
                                """,
                                (email,session["pseudo"]))
                else:
                    local_time = time.localtime()
                    if local_time.tm_mon>9:
                        if local_time.tm_mday>9:
                            datemin= str(local_time.tm_year-13)+"-"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
                            datemax= str(local_time.tm_year-113)+"-"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
                        else:
                            datemin= str(local_time.tm_year-13)+"-"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
                            datemax= str(local_time.tm_year-113)+"-"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
                    else:
                        if local_time.tm_mday>9:
                            datemin= str(local_time.tm_year-13)+"-0"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
                            datemax= str(local_time.tm_year-113)+"-0"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
                        else:
                            datemin= str(local_time.tm_year-13)+"-0"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
                            datemax= str(local_time.tm_year-113)+"-0"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
                    pseudo = session["pseudo"]
                    with db.connect() as conn:
                        with conn.cursor() as cur:
                            cur.execute("SELECT pseudonyme, nom, email, date_naissance FROM joueur WHERE pseudonyme = (%s)", (pseudo,))
                            joueur_info = cur.fetchone() 
                    return render_template("profil_email.html", joueur_info=joueur_info,datemin=datemin,datemax=datemax)
            
            if i == "pseudo":
                with db.connect() as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT pseudonyme FROM joueur")
                        tou_pseudo = cur.fetchall()  # Utilisez fetchall() pour récupérer toutes les lignes
                lst = [pseudoe[0] for pseudoe in tou_pseudo]  # Utilisez une compréhension de liste pour extraire les emails
                if pseudo not in lst:
                    with db.connect() as conn:
                        with conn.cursor() as cur:
                            cur.execute(
                                """
                                UPDATE joueur
                                SET pseudonyme = %s
                                WHERE pseudonyme = %s
                                """,
                                (pseudo,session["pseudo"])
                            )
                    session["pseudo"]=pseudo
                else:
                    local_time = time.localtime()
                    if local_time.tm_mon>9:
                        if local_time.tm_mday>9:
                            datemin= str(local_time.tm_year-13)+"-"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
                            datemax= str(local_time.tm_year-113)+"-"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
                        else:
                            datemin= str(local_time.tm_year-13)+"-"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
                            datemax= str(local_time.tm_year-113)+"-"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
                    else:
                        if local_time.tm_mday>9:
                            datemin= str(local_time.tm_year-13)+"-0"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
                            datemax= str(local_time.tm_year-113)+"-0"+str(local_time.tm_mon)+"-"+str(local_time.tm_mday)
                        else:
                            datemin= str(local_time.tm_year-13)+"-0"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
                            datemax= str(local_time.tm_year-113)+"-0"+str(local_time.tm_mon)+"-0"+str(local_time.tm_mday)
                    pseudo = session["pseudo"]
                    with db.connect() as conn:
                        with conn.cursor() as cur:
                            cur.execute("SELECT pseudonyme, nom, email, date_naissance FROM joueur WHERE pseudonyme = (%s)", (pseudo,))
                            joueur_info = cur.fetchone() 
                    return render_template("profil_pseudo.html", joueur_info=joueur_info,datemin=datemin,datemax=datemax)
    return redirect(url_for('profil'))

@app.route("/ami")
def amis():
    if 'pseudo' in session:
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT pseudonyme1, pseudonyme2 FROM est_ami_avec WHERE pseudonyme1 = %s OR pseudonyme2 = %s", (session["pseudo"], session["pseudo"]))
                amis = cur.fetchall()
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT pseudonyme FROM joueur")
                pseudo = cur.fetchall()

    lstpseudo1 = []
    lstpseudo2 = []
    for i in amis:
        if i[0] != session["pseudo"]:
            lstpseudo1.append(i[0])
        if i[1] != session["pseudo"]:
            lstpseudo2.append(i[1])
 

    lstamis = lstpseudo1 + lstpseudo2
    lstpseudo = [p[0] for p in pseudo]
    for i in lstamis:
        if i in lstpseudo:
            lstpseudo.remove(i)
    lstpseudo.remove(session["pseudo"])


    return render_template("ami.html",ami=lstamis,pseudo=lstpseudo,rat=lstamis)

@app.route("/ami_add", methods=['POST'])
def ajouter_ami():
    new_ami = request.form.get("amis", None)
    if new_ami != "Demander en amis":
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO est_ami_avec (pseudonyme1, pseudonyme2)
                    VALUES (%s, %s)
                    """,
        (session["pseudo"], new_ami))
    return redirect(url_for('amis'))

@app.route("/ami_supp", methods=['POST'])
def supprimer_ami():
    supprimer_ami = request.form.get("rat", None)
    if supprimer_ami != "Supprimer":
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM est_ami_avec 
                    WHERE (pseudonyme1 = %s AND pseudonyme2 = %s)
                    OR (pseudonyme1 = %s AND pseudonyme2 = %s)
                    """,
                    (session["pseudo"], supprimer_ami, supprimer_ami, session["pseudo"])
                )
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM partage
                    WHERE (pseudonyme1 = %s AND pseudonyme2 = %s)
                    OR (pseudonyme1 = %s AND pseudonyme2 = %s)
                    """,
                    (session["pseudo"], supprimer_ami, supprimer_ami, session["pseudo"])
                )
                
    return redirect(url_for('amis'))

@app.route("/recherche", methods = ['get'])
def recherche():
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT nom_genre FROM genre")
            lst = cur.fetchall()

            lst_genres = []
            for elem in lst :
                lst_genres.append(elem[0])

        with conn.cursor() as cur:
                cur.execute("SELECT nom_entreprise FROM entreprise limit 16")
                lst2 =          cur.fetchall()

                lst_entreprises_edit = []
                for elem in lst2 :
                    lst_entreprises_edit.append(elem[0])
        
        with conn.cursor() as cur:
            cur.execute("SELECT nom_entreprise FROM entreprise offset 16")
            lst2 = cur.fetchall()

            lst_entreprises_dev = []
            for elem in lst2 :
                lst_entreprises_dev.append(elem[0])

    return render_template("recherche.html",lst_genres = lst_genres, entreprises_dev = lst_entreprises_dev, entreprises_edit = lst_entreprises_edit)


@app.route("/tri", methods = ['get'])
def tri():

    genres = request.args.getlist('genre',None)
    titre = request.args.get('titre',None)
    prix = request.args.get('prix',None)
    entreprise_dev = request.args.get('entreprise_dev',None)
    entreprise_edit = request.args.get('entreprise_edit',None)


    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT nom_genre FROM genre")
            lst = cur.fetchall()
            lst_genres = []
            for elem in lst :
                lst_genres.append(elem[0]) 
        with conn.cursor() as cur:
                cur.execute("SELECT nom_entreprise FROM entreprise limit 16")
                lst2 = cur.fetchall()

                lst_entreprises_edit = []
                for elem in lst2 :
                    lst_entreprises_edit.append(elem[0])
        with conn.cursor() as cur:
            cur.execute("SELECT nom_entreprise FROM entreprise offset 16")
            lst2 = cur.fetchall()
            lst_entreprises_dev = []
            for elem in lst2 :
                lst_entreprises_dev.append(elem[0])
                


    if len(genres)==0 and  titre == "Recherche" and prix=="Prix" and entreprise_dev == "None" and entreprise_edit== "None" :
        return redirect(url_for('recherche'))

    lst=[]
    lst_edit=[]
    lst_dev=[]
    lst_prix=[]
    lst_titre=[]
    lst_genre=[]
    with db.connect() as conn:
        with conn.cursor() as cur:
                    cur.execute("SELECT * FROM jeu") 
                    list_jeut = cur.fetchall()
        for i in list_jeut:
            lst.append ([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
        
        if entreprise_edit != "None" : 
            with db.connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM jeu JOIN entreprise on jeu.id_entreprise_edit=entreprise.id_entreprise WHERE nom_entreprise = %s", (entreprise_edit,)) #recherche par entreprise_edit
                    list_jeux_entreprise_edit = cur.fetchall()  
            for i in list_jeux_entreprise_edit:
                lst_edit.append ([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]])
        
        if entreprise_dev != "None": 
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM jeu JOIN entreprise on jeu.id_entreprise_dev=entreprise.id_entreprise WHERE nom_entreprise =  %s", (entreprise_dev,)) #recherche par entreprise_dev
                list_jeux_entreprise_dev = cur.fetchall()
            for i in list_jeux_entreprise_dev:
                lst_dev.append ([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]])
        
        if prix != "" : 
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM jeu WHERE prix = %s", (prix,))
                list_jeux_prix = cur.fetchall()     
            for i in list_jeux_prix:
                lst_prix.append ([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])      
        
        if titre != "":
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM jeu WHERE LOWER(titre) LIKE LOWER(%s)", ("%" + titre + "%",)) # recherche par titre, insensible à la casse
                list_jeux_titre = cur.fetchall()
            for i in list_jeux_titre:
                lst_titre.append ([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
        
        if len(genres)!=0 :
            for i in genres : 
                with conn.cursor() as cur:
                    cur.execute("SELECT DISTINCT titre FROM  jeu natural JOIN appartient natural JOIN genre WHERE nom_genre = %s", (i,)) #recherche par genres
                    subjeux = cur.fetchall()
            for i in subjeux:
                lst_genre.append([i[0]])

        if entreprise_edit != "None" :
            copy=lst_edit.copy()
            for i in copy:
                cmpt=0
                for j in lst:
                    if i [1]==j[1]:
                        cmpt+=1
                if cmpt ==0:
                    lst_edit.remove(i)
            lst=lst_edit

        if entreprise_dev != "None":
            copy=lst_dev.copy()
            for i in copy:
                cmpt=0
                for j in lst:
                    if i [1]==j[1]:
                        cmpt+=1
                if cmpt ==0:
                    lst_dev.remove(i)
            lst=lst_dev
    
        if prix != "" : 
            copy=lst_prix.copy()
            for i in copy:
                cmpt=0
                for j in lst:
                    if i [1]==j[1]:
                        cmpt+=1
                if cmpt ==0:
                    lst_prix.remove(i)
            lst=lst_prix

        if titre != "":
            copy=lst_titre.copy()
            for i in copy:
                cmpt=0
                for j in lst:
                    if i [1]==j[1]:
                        cmpt+=1
                if cmpt ==0:
                    lst_titre.remove(i)
            lst=lst_titre

        if len(genres)!=0 :
            copy=lst_genre.copy()
            for i in copy:
                cmpt=0
                for j in lst:
                    if i [0]==j[1]:
                        cmpt+=1
                if cmpt ==0:
                    lst_genre.remove(i)
            p=[]
            for i in lst_genre:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM jeu WHERE titre = %s", (i[0],))
                    fr = cur.fetchall()     
                for i in fr:         
                    p.append ([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]) 
            lst=p

        return render_template("recherche.html",lst_genres = lst_genres, entreprises_dev = lst_entreprises_dev, entreprises_edit = lst_entreprises_edit, lst_jeux=lst)


if __name__ == '__main__':
    app.run()