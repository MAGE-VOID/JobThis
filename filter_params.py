filter_parameters = {
    # Filtramos trabajos publicados en los últimos X días
    "days_back": 1,
    
    # Keywords positivos en la descripción (para indicar que es remoto, teletrabajo, etc.)
    # + SE AGREGAN TÉRMINOS QUE DEFINEN PUESTOS DE DESARROLLADOR/PROGRAMADOR
    "keywords_in_description": [
        # Palabras clave de 'remoto'
        "remoto", 
        "teletrabajo",
        "tele-trabajo", 
        "remote", 
        "wfh", 
        "work from home", 
        "home office", 
        "home-office", 
        "fully remote", 
        "100% remote", 
        "completely remote", 
        "telecommute",

        # Palabras clave de 'desarrollo/programación'
        "developer",
        "programmer",
        "desarrollador",
        "programador",
        "software engineer",
        "ingeniero de software",
        "full stack",
        "frontend",
        "back end",
        "backend",
        "web developer",
        "software developer",
    ],

    # Frases negativas en la descripción (para excluir trabajos NO-remotos, presenciales, híbridos, viajes, etc.)
    # + AÑADIMOS LAS QUE EXCLUYEN “SENIOR”, “LEAD”, ETC.
    "negatives_in_description": [
        # --- NO REMOTO / PRESENCIAL ---
        "no remote", "not remote", "no remoto", "not remoto",
        "onsite only", "on-site only",
        "office only", "office-based", "in-person only",
        "presencial",
        "work on site", "work onsite", "work on-site",

        # --- HÍBRIDO / SEMI REMOTO ---
        "hybrid", "híbrido", "hibrido", "hybrid only",
        "partially remote", "part-time remote", "semi-remote", 
        "mixed remote", "some days remote", "some days onsite", 
        "some office days", "flexible location",

        # --- VIAJE / TRAVEL
        "travel", "TRAVEL",
        "traveling", "TRAVELING",
        "travel required", "TRAVEL REQUIRED",
        "requires travel", "REQUIRES TRAVEL",
        "some travel", "SOME TRAVEL",
        "traveling is required", "TRAVELING IS REQUIRED",
        "must be able to travel", "MUST BE ABLE TO TRAVEL",

        "viajar", "VIAJAR",
        "viajes", "VIAJES",
        "disponibilidad para viajar", "DISPONIBILIDAD PARA VIAJAR",
        "requiere viajar", "REQUIERE VIAJAR",
        "requiere viajes", "REQUIERE VIAJES",
        "viajar frecuentemente", "VIAJAR FRECUENTEMENTE",
        "viajar obligatorio", "VIAJAR OBLIGATORIO",

        "travel up to", "TRAVEL UP TO",
        "travel 25%", "TRAVEL 25%",
        "travel 50%", "TRAVEL 50%",
        "25% travel", "25% TRAVEL",
        "50% travel", "50% TRAVEL",
        "occasional travel", "OCCASIONAL TRAVEL",
        "frequent travel", "FREQUENT TRAVEL",

        # --- RELOCATION / COMMUTE ---
        "relocation required", "RELOCATION REQUIRED",
        "relocation assistance", "RELOCATION ASSISTANCE",
        "some relocation", "SOME RELOCATION",
        "must relocate", "MUST RELOCATE",
        "requires relocation", "REQUIRES RELOCATION",
        "commute required", "COMMUTE REQUIRED",
        "commuting is required", "COMMUTING IS REQUIRED",
        "desplazamiento obligatorio", "DESPLAZAMIENTO OBLIGATORIO",
        "desplazarse", "DESPLAZARSE",

        # --- EXCLUIR SENIOR/LEAD (EN LA DESCRIPCIÓN) ---
        "senior",
        "sr.",
        "lead",
        "chief",
        "principal",
        "architect",
        "manager",
    ],

    # Filtrado según título: VACÍO
    "title_keywords": [],

    # Frases negativas en el título: VACÍO
    "negatives_in_title": [],

    # Lista de países (exact match). Vacío => no filtra
    "country_list": [],
}
