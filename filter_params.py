filter_parameters = {
    # Filtramos trabajos publicados en los últimos X días
    "days_back": 5,
    
    # Keywords positivos en la descripción (para indicar que es remoto, teletrabajo, etc.)
    "keywords_in_description": [
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
        "telecommute"
    ],

    # Frases negativas en la descripción (para excluir trabajos NO-remotos, presenciales, híbridos, viajes, etc.)
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
    ],

    # Keywords en el título
    "title_keywords": [],

    # Frases negativas en el título, por si quieres excluir ciertos roles
    "negatives_in_title": [],

    # Lista de países (exact match). Vacío => no filtra
    "country_list": [],
}
