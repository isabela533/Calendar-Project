from datetime import date, timedelta

def get_fechas_clave(year: int) -> list[dict]:

    def nth_weekday(year, month, weekday, n):
        """n-ésimo día de la semana del mes. weekday: 0=lunes, 6=domingo"""
        d = date(year, month, 1)
        days = [(d + timedelta(i)) for i in range(31) if (d + timedelta(i)).month == month]
        matches = [x for x in days if x.weekday() == weekday]
        return matches[n - 1]

    fechas = [
        # ── Enero ──
        {"nombre": "New Year's Day",           "fecha": date(year, 1, 1),               "tipo": "festivo",   "emoji": "🎆", "desc": "New beginnings campaigns, fitness, resolutions."},
        {"nombre": "Martin Luther King Day",   "fecha": nth_weekday(year, 1, 0, 3),     "tipo": "social",    "emoji": "✊", "desc": "Brand purpose and diversity campaigns."},
        {"nombre": "Super Bowl Sunday",        "fecha": nth_weekday(year, 2, 6, 1) - timedelta(days=1) if nth_weekday(year, 2, 6, 1).weekday() == 6 else nth_weekday(year, 2, 0, 2) - timedelta(days=1), "tipo": "retail", "emoji": "🏈", "desc": "Biggest advertising day of the year in the US."},

        # ── Febrero ──
        {"nombre": "Valentine's Day",          "fecha": date(year, 2, 14),              "tipo": "retail",    "emoji": "❤️", "desc": "One of the highest retail peaks of the year."},
        {"nombre": "Presidents' Day",          "fecha": nth_weekday(year, 2, 0, 3),     "tipo": "retail",    "emoji": "🏛️", "desc": "Major sales weekend, especially automotive and furniture."},

        # ── Marzo ──
        {"nombre": "International Women's Day","fecha": date(year, 3, 8),               "tipo": "social",    "emoji": "💜", "desc": "High visibility for purpose-driven brands."},
        {"nombre": "St. Patrick's Day",        "fecha": date(year, 3, 17),              "tipo": "temporada", "emoji": "🍀", "desc": "Strong for food, beverage and entertainment brands."},
        {"nombre": "Spring Equinox / Fashion", "fecha": date(year, 3, 20),              "tipo": "moda",      "emoji": "🌸", "desc": "Spring collection launches and outdoor lifestyle."},

        # ── Abril ──
        {"nombre": "Easter",                   "fecha": date(year, 4, 20),              "tipo": "retail",    "emoji": "🐣", "desc": "Family, food and gifting campaigns. Big in retail."},
        {"nombre": "Earth Day",                "fecha": date(year, 4, 22),              "tipo": "social",    "emoji": "🌍", "desc": "Sustainability and eco-conscious brand campaigns."},
        {"nombre": "Tax Day",                  "fecha": date(year, 4, 15),              "tipo": "retail",    "emoji": "💰", "desc": "Financial services and deals campaigns around refunds."},

        # ── Mayo ──
        {"nombre": "Mother's Day",             "fecha": nth_weekday(year, 5, 6, 2),     "tipo": "retail",    "emoji": "🌸", "desc": "Top retail event of the year in the US."},
        {"nombre": "Memorial Day Weekend",     "fecha": nth_weekday(year, 5, 0, 4) - timedelta(days=2), "tipo": "retail", "emoji": "🇺🇸", "desc": "Major sales weekend, start of summer season."},

        # ── Junio ──
        {"nombre": "Father's Day",             "fecha": nth_weekday(year, 6, 6, 3),     "tipo": "retail",    "emoji": "👔", "desc": "Second biggest gifting event after Mother's Day."},
        {"nombre": "Juneteenth",               "fecha": date(year, 6, 19),              "tipo": "social",    "emoji": "✊", "desc": "Federal holiday. Cultural and diversity campaigns."},
        {"nombre": "Pride Month (peak)",       "fecha": date(year, 6, 28),              "tipo": "social",    "emoji": "🏳️‍🌈", "desc": "High visibility for inclusive brands throughout June."},

        # ── Julio ──
        {"nombre": "Independence Day",         "fecha": date(year, 7, 4),               "tipo": "festivo",   "emoji": "🎇", "desc": "Patriotic campaigns and summer sales peak."},
        {"nombre": "Amazon Prime Day",         "fecha": nth_weekday(year, 7, 1, 2),     "tipo": "tech",      "emoji": "📦", "desc": "Biggest e-commerce event of the summer."},

        # ── Agosto ──
        {"nombre": "Back to School",           "fecha": date(year, 8, 1),               "tipo": "retail",    "emoji": "🎒", "desc": "High demand in tech, apparel and supplies."},
        {"nombre": "National Dog Day",         "fecha": date(year, 8, 26),              "tipo": "social",    "emoji": "🐶", "desc": "Viral content opportunity for pet and lifestyle brands."},

        # ── Septiembre ──
        {"nombre": "Labor Day Weekend",        "fecha": nth_weekday(year, 9, 0, 1),     "tipo": "retail",    "emoji": "🛍️", "desc": "End of summer sales. Major retail weekend."},
        {"nombre": "Hispanic Heritage Month",  "fecha": date(year, 9, 15),              "tipo": "social",    "emoji": "🌮", "desc": "Runs Sept 15 – Oct 15. Large demographic opportunity."},
        {"nombre": "Fall Fashion Season",      "fecha": date(year, 9, 22),              "tipo": "moda",      "emoji": "🍂", "desc": "Fall collection launches and lifestyle content."},

        # ── Octubre ──
        {"nombre": "Halloween",                "fecha": date(year, 10, 31),             "tipo": "temporada", "emoji": "🎃", "desc": "Massive retail and content opportunity across all industries."},
        {"nombre": "World Mental Health Day",  "fecha": date(year, 10, 10),             "tipo": "social",    "emoji": "🧠", "desc": "High engagement for purpose-driven brands."},
        {"nombre": "Pre-Holiday Sales Start",  "fecha": date(year, 10, 15),             "tipo": "retail",    "emoji": "🏷️", "desc": "Consumers start holiday shopping earlier every year."},

        # ── Noviembre ──
        {"nombre": "Veterans Day",             "fecha": date(year, 11, 11),             "tipo": "social",    "emoji": "🎖️", "desc": "Brand gratitude and community campaigns."},
        {"nombre": "Thanksgiving",             "fecha": nth_weekday(year, 11, 3, 4),    "tipo": "festivo",   "emoji": "🦃", "desc": "Family and gratitude campaigns. Huge food and travel moment."},
        {"nombre": "Black Friday",             "fecha": nth_weekday(year, 11, 3, 4) + timedelta(days=1), "tipo": "retail", "emoji": "🛍️", "desc": "Highest conversion day of the year in US e-commerce."},
        {"nombre": "Small Business Saturday",  "fecha": nth_weekday(year, 11, 3, 4) + timedelta(days=2), "tipo": "retail", "emoji": "🏪", "desc": "Growing movement supporting local and small brands."},
        {"nombre": "Cyber Monday",             "fecha": nth_weekday(year, 11, 3, 4) + timedelta(days=4), "tipo": "tech",   "emoji": "💻", "desc": "Digital extension of Black Friday. Strong in tech and services."},

        # ── Diciembre ──
        {"nombre": "Giving Tuesday",           "fecha": nth_weekday(year, 11, 3, 4) + timedelta(days=5), "tipo": "social", "emoji": "💝", "desc": "Nonprofit and CSR campaigns. High social engagement."},
        {"nombre": "Hanukkah",                 "fecha": date(year, 12, 14),             "tipo": "retail",    "emoji": "🕎", "desc": "8-day gifting window. Important for inclusive campaigns."},
        {"nombre": "Christmas Eve",            "fecha": date(year, 12, 24),             "tipo": "festivo",   "emoji": "🎄", "desc": "Last-minute gifting and emotional brand campaigns."},
        {"nombre": "Christmas Day",            "fecha": date(year, 12, 25),             "tipo": "festivo",   "emoji": "🎅", "desc": "Peak of emotional and brand storytelling campaigns."},
        {"nombre": "New Year's Eve",           "fecha": date(year, 12, 31),             "tipo": "temporada", "emoji": "🥂", "desc": "Year-end brand wrap-up and countdown campaigns."},
    ]

    return sorted(fechas, key=lambda x: x["fecha"])


def get_proximas(fechas: list, dias: int = 60) -> list:
    hoy = date.today()
    return [f for f in fechas if 0 <= (f["fecha"] - hoy).days <= dias]


TIPO_COLORES = {
    "retail":    "#D85A30",
    "festivo":   "#7F77DD",
    "social":    "#1D9E75",
    "temporada": "#D4537E",
    "tech":      "#378ADD",
    "moda":      "#BA7517",
    "cultural":  "#888780",
}