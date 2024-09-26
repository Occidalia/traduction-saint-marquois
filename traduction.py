print("Attention : ce logiciel de traduction est BETA, ne mettez pas de majuscule. Si un mot s'affiche en français dans la traduction, c'est qu'il n'éxiste pas dans la bibliothèque de traduction")
traductions = {
    # I - Articles
    "le": "a", "la": "a", "les": "a", "l'": "a",
    "un": "ó", "une": "ó",
    
    # II - Conjonctions et prépositions
    "de": "tu", "des": "tu", 
    "du": "tua", "de la": "tua", "des": "tua",
    "et": "í",
    "ce": "su", "cet": "su", "cette": "su", "ces": "su", "c'": "su",
    
    # III - Adjectifs possessifs
    "mon": "maí", "ma": "maí", "mes": "maí",
    "ton": "daí", "ta": "daí", "tes": "daí",
    "son": "saí", "sa": "saí", "ses": "saí",
    "notre": "nadru", "nos": "nadru",
    "votre": "vadru", "vos": "vadru",
    "leur": "lur", "leurs": "lur",
    
    # IV - Prépositions
    "à": "o", "au": "ona", "à la": "ona", "aux": "ona",
    "pour": "pér", "par": "por", "que": "chu", "quoi": "chu", "qui": "che",
    "en": "oí", "dans": "toí",
    "sur": "sór", "sous": "séu", "sans": "soí",
    
    # V - Couleurs
    "rouge": "rédun", "rouges": "rédun",
    "orange": "aroigun", "oranges": "aroigun",
    "vert": "virdun", "verte": "virdun", "verts": "virdun", "vertes": "virdun",
    "noir": "naurun", "noirs": "naurun", "noire": "naurun", "noires": "naurun",
    "bleu": "blun", "bleue": "blun", "bleus": "blun", "bleues": "blun",
    "violet": "vhalíun", "violette": "vhalíun", "violets": "vhalíun", "violettes": "vhalíun",
    "marron": "moraíun", "marrons": "moraíun",
    "blanc": "bloighun", "blanche": "bloighun", "blancs": "bloighun", "blanches": "bloighun",
    "turquoise": "dórchausun", "turquoises": "dórchausun",
    "jaune": "ganun", "jaunes": "ganun",
    
    # VI - Adjectifs émotionnels
    "heureux": "yurun", "heureuse": "yurun", "heureuses": "yurun",
    "triste": "dredhun", "tristes": "dredhun",
    "content": "chaidoíun", "contente": "chaidoíun", "contents": "chaidoíun", "contentes": "chaidoíun",
    "colérique": "chalirechun", "colériques": "chalirechun",
    "embarrassé": "oiborosíun", "embarrassée": "oiborosíun", "embarrassés": "oiborosíun", "embarrassées": "oiborosíun",
    "timide": "demetun", "timides": "demetun",
    
    # VII - Bases
    "bonjour": "gérbhán", 
    "au revoir": "oruvauhim",
    "s'il te plaît": "se h-el pliren dau", "s'il vous plaît": "se h-el pliren véu",
    "merci": "mirse",
    "oui": "ées", "non": "naí", "ne ... pas": "naí",
    "à bientôt": "o bháda",
    "à demain": "ona tumá", "à plus tard": "o plós dortun",
    
    # VIII - Jours de la semaine
    "lundi": "lóngér", "mardi": "morgér", "mercredi": "mirchrugér", 
    "jeudi": "gugér", "vendredi": "voitrugér", 
    "samedi": "somgér", "dimanche": "salihugér",
    
    # IX - Mois et saisons
    "janvier": "goivhir", "février": "fivrehir", "mars": "mors", "avril": "ovrel", "mai": "mihu", 
    "juin": "góhá", "juillet": "góehí", "août": "éd", "septembre": "sipudoibru", "octobre": "achdabru", 
    "novembre": "navoibru", "décembre": "tisoibru",
    "printemps": "prádoipsu", "été": "idí", "automne": "adan", "hiver": "evir",
    
    # X - Numéros
    "un": "ón", "deux": "tus", "trois": "draus", "quatre": "chodru", "cinq": "sách", "six": "ses", 
    "sept": "sid", "huit": "óed", "neuf": "nuf", "dix": "tes", "onze": "aisu", "douze": "tés", 
    "treize": "dris", "quatorze": "chodars", "quinze": "chás", "seize": "setes", 
    "dix-sept": "sides", "dix-huit": "óedes", "dix-neuf": "nuftes", "vingt": "vá"
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
