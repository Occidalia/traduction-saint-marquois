
print("Attention : ce logiciel de traduction est BETA, ne mettez pas de majuscule. Si un mot s'affiche en français dans la traduction, c'est qu'il n'éxiste pas dans la bibliothèque de traduction")
traductions = {
    # I - Articles
    "le": "A", "la": "A", "les": "A", "l'": "A",
    "un": "Ó", "une": "Ó",
    
    # II - Conjonctions et prépositions
    "de": "Tu", "des": "Tu", 
    "du": "Tua", "de la": "Tua", "des": "Tua",
    "et": "Í",
    "ce": "Su", "cet": "Su", "cette": "Su", "ces": "Su", "c'": "Su",
    
    # III - Adjectifs possessifs
    "mon": "Maí", "ma": "Maí", "mes": "Maí",
    "ton": "Daí", "ta": "Daí", "tes": "Daí",
    "son": "Saí", "sa": "Saí", "ses": "Saí",
    "notre": "Nadru", "nos": "Nadru",
    "votre": "Vadru", "vos": "Vadru",
    "leur": "Lur", "leurs": "Lur",
    
    # IV - Prépositions
    "à": "O", "au": "Ona", "à la": "Ona", "aux": "Ona",
    "pour": "Pér", "par": "Por", "que": "Chu", "quoi": "Chu", "qui": "Che",
    "en": "Oí", "dans": "Toí",
    "sur": "Sór", "sous": "Séu", "sans": "Soí",
    
    # V - Couleurs
    "rouge": "Rédun", "rouges": "Rédun",
    "orange": "Aroigun", "oranges": "Aroigun",
    "vert": "Virdun", "verte": "Virdun", "verts": "Virdun", "vertes": "Virdun",
    "noir": "Naurun", "noirs": "Naurun", "noire": "Naurun", "noires": "Naurun",
    "bleu": "Blun", "bleue": "Blun", "bleus": "Blun", "bleues": "Blun",
    "violet": "Vhalíun", "violette": "Vhalíun", "violets": "Vhalíun", "violettes": "Vhalíun",
    "marron": "Moraíun", "marrons": "Moraíun",
    "blanc": "Bloighun", "blanche": "Bloighun", "blancs": "Bloighun", "blanches": "Bloighun",
    "turquoise": "Dórchausun", "turquoises": "Dórchausun",
    "jaune": "Ganun", "jaunes": "Ganun",
    
    # VI - Adjectifs émotionnels
    "heureux": "Yurun", "heureuse": "Yurun", "heureuses": "Yurun",
    "triste": "Dredhun", "tristes": "Dredhun",
    "content": "Chaidoíun", "contente": "Chaidoíun", "contents": "Chaidoíun", "contentes": "Chaidoíun",
    "colérique": "Chalirechun", "colériques": "Chalirechun",
    "embarrassé": "Oiborosíun", "embarrassée": "Oiborosíun", "embarrassés": "Oiborosíun", "embarrassées": "Oiborosíun",
    "timide": "Demetun", "timides": "Demetun",
    
    # VII - Bases
    "bonjour": "Gérbhán", 
    "au revoir": "Oruvauhim",
    "s'il te plaît": "Se h-el pliren dau", "s'il vous plaît": "Se h-el pliren véu",
    "merci": "Mirse",
    "oui": "Ées", "non": "Naí", "ne ... pas": "Naí",
    "à bientôt": "O bháda",
    "à demain": "Ona tumá", "à plus tard": "O plós dortun",
    
    # VIII - Jours de la semaine
    "lundi": "Lóngér", "mardi": "Morgér", "mercredi": "Mirchrugér", 
    "jeudi": "Gugér", "vendredi": "Voitrugér", 
    "samedi": "Somgér", "dimanche": "Salihugér",
    
    # IX - Mois et saisons
    "janvier": "Goivhir", "février": "Fivrehir", "mars": "Mors", "avril": "Ovrel", "mai": "Mihu", 
    "juin": "Góhá", "juillet": "Góehí", "août": "Éd", "septembre": "Sipudoibru", "octobre": "Achdabru", 
    "novembre": "Navoibru", "décembre": "Tisoibru",
    "printemps": "Prádoipsu", "été": "Idí", "automne": "Adan", "hiver": "Evir",
    
    # X - Numéros
    "un": "Ón", "deux": "Tus", "trois": "Draus", "quatre": "Chodru", "cinq": "Sách", "six": "Ses", 
    "sept": "Sid", "huit": "Óed", "neuf": "Nuf", "dix": "Tes", "onze": "Aisu", "douze": "Tés", 
    "treize": "Dris", "quatorze": "Chodars", "quinze": "Chás", "seize": "Setes", 
    "dix-sept": "Sides", "dix-huit": "Óedes", "dix-neuf": "Nuftes", "vingt": "Vá"
}

# Demander les mots en français
mot1 = input("Quel est le premier mot en français ? ")
mot2 = input("Quel est le second mot en français ? ")
mot3 = input("Quel est le troisième mot en français ? ")
mot4 = input("Quel est le quatrième mot en français ? ")
mot5 = input("Quel est le cinquième mot en français ? ")

# Liste des mots saisis
mots = [mot1, mot2, mot3, mot4, mot5]

# Traduire les mots si possible
mots_traduits = [traductions.get(mot, mot) for mot in mots]

# Afficher les mots traduits
print("Traduction: ", " ".join(mots_traduits))
