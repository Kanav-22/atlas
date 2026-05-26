SCHENGEN_COUNTRIES = [
    "austria", "belgium", "croatia", "czechia", "czech republic",
    "denmark", "estonia", "finland", "france", "germany", "greece",
    "hungary", "iceland", "italy", "latvia", "liechtenstein",
    "lithuania", "luxembourg", "malta", "netherlands", "norway",
    "poland", "portugal", "slovakia", "slovenia", "spain", "sweden",
    "paris", "rome", "berlin", "barcelona", "amsterdam", "prague",
    "vienna", "athens", "lisbon", "budapest", "warsaw", "stockholm"
]

def normalize_country(query: str) -> str:
    query_lower = query.lower()
    for country in SCHENGEN_COUNTRIES:
        if country in query_lower:
            return "Schengen visa requirements Europe"
    return query

VISA_DATA = [
    {
        "country": "United States",
        "code": "USA",
        "visa_type": "B1/B2 Tourist/Business Visa",
        "visa_required": True,
        "processing_time": "3-5 weeks",
        "fee": "USD 185 (non-refundable)",
        "validity": "10 years (multiple entry)",
        "required_documents": [
            "Valid Indian passport (minimum 6 months validity)",
            "DS-160 online application form (fully completed)",
            "Visa appointment confirmation",
            "Recent passport-size photograph (5x5 cm, white background)",
            "Bank statements (last 6 months, showing sufficient funds)",
            "Income Tax Returns (last 3 years)",
            "Salary slips (last 3 months) or business proof",
            "Property documents or assets proof",
            "Employment letter or business ownership proof",
            "Travel itinerary and hotel bookings",
            "Previous US visa (if any)",
            "Ties to India proof (family, property, job)"
        ],
        "interview_required": True,
        "notes": "Interview at US Embassy/Consulate is mandatory. Strong ties to India must be demonstrated. Rejection rate is significant — financial proof is critical."
    },
    {
        "country": "United Kingdom",
        "code": "UK",
        "visa_type": "Standard Visitor Visa",
        "visa_required": True,
        "processing_time": "3 weeks",
        "fee": "GBP 115",
        "validity": "6 months (single/multiple entry)",
        "required_documents": [
            "Valid Indian passport",
            "Online UK visa application form",
            "Biometric enrollment (at visa application centre)",
            "Recent passport-size photograph",
            "Bank statements (last 6 months)",
            "Income Tax Returns (last 2-3 years)",
            "Salary slips or business proof",
            "Employment letter with leave approval",
            "Travel itinerary and hotel bookings",
            "Proof of accommodation in UK",
            "Travel insurance",
            "Property or asset proof in India"
        ],
        "interview_required": False,
        "notes": "No interview required. Application submitted at VFS Global. Biometrics mandatory. Strong financial history increases approval chances."
    },
    {
        "country": "Schengen Area",
        "code": "SCHENGEN",
        "visa_type": "Schengen Tourist Visa (Type C)",
        "visa_required": True,
        "processing_time": "15 working days",
        "fee": "EUR 90",
        "validity": "90 days within 180 days",
        "required_documents": [
            "Valid Indian passport (minimum 3 months beyond stay)",
            "Schengen visa application form",
            "Recent passport-size photograph (white background)",
            "Travel insurance (minimum EUR 30,000 coverage)",
            "Flight bookings (confirmed or tentative)",
            "Hotel bookings for entire stay",
            "Bank statements (last 3-6 months)",
            "Income Tax Returns",
            "Salary slips or employment proof",
            "Employment letter with leave sanctioned",
            "Cover letter explaining purpose of visit",
            "Previous Schengen or other visas (helps approval)"
        ],
        "interview_required": False,
        "notes": "Covers all 27 Schengen member states: France, Germany, Italy, Spain, Netherlands, Greece, Portugal, Austria, Belgium, Switzerland, Czech Republic, Denmark, Finland, Hungary, Norway, Poland, Sweden, Croatia, Estonia, Latvia, Lithuania, Luxembourg, Malta, Slovakia, Slovenia, Iceland, Liechtenstein. Apply at embassy of country where you spend most time or enter first. Travel insurance is mandatory. Apply 15 days in advance minimum."
    },
    {
        "country": "Canada",
        "code": "CAN",
        "visa_type": "Temporary Resident Visa (Tourist Visa)",
        "visa_required": True,
        "processing_time": "4-8 weeks",
        "fee": "CAD 100",
        "validity": "Up to 10 years or passport expiry",
        "required_documents": [
            "Valid Indian passport",
            "Online IRCC application (IMM 5257)",
            "Recent passport-size photograph",
            "Biometrics enrollment",
            "Bank statements (last 4-6 months)",
            "Income Tax Returns (last 3 years)",
            "Employment letter or business proof",
            "Salary slips (last 3 months)",
            "Property documents",
            "Travel itinerary",
            "Invitation letter (if visiting family/friends)",
            "Proof of ties to India"
        ],
        "interview_required": False,
        "notes": "Applied online via IRCC portal. Biometrics required. Processing times vary significantly. Digital photograph must meet specific requirements."
    },
    {
        "country": "Australia",
        "code": "AUS",
        "visa_type": "Visitor Visa (subclass 600)",
        "visa_required": True,
        "processing_time": "20-30 working days",
        "fee": "AUD 190",
        "validity": "3, 6, or 12 months",
        "required_documents": [
            "Valid Indian passport",
            "ImmiAccount online application",
            "Recent passport-size photograph",
            "Bank statements (last 6 months)",
            "Income Tax Returns (last 3 years)",
            "Superannuation or investment proof",
            "Employment letter",
            "Salary slips",
            "Travel itinerary",
            "Hotel bookings",
            "Health insurance",
            "Proof of ties to India"
        ],
        "interview_required": False,
        "notes": "Fully online application. No biometrics initially but may be requested. Health examination may be required for stays over 3 months."
    },
    {
        "country": "UAE",
        "code": "UAE",
        "visa_type": "Tourist Visa / Visa on Arrival",
        "visa_required": False,
        "processing_time": "Instant (on arrival) or 2-3 days (pre-applied)",
        "fee": "Free on arrival / AED 100-250 if pre-applied",
        "validity": "30 days (extendable to 60 days)",
        "required_documents": [
            "Valid Indian passport (minimum 6 months validity)",
            "Return flight ticket",
            "Hotel booking or host address",
            "Sufficient funds proof",
            "Travel insurance (recommended)"
        ],
        "interview_required": False,
        "notes": "Indians get visa on arrival at Dubai, Abu Dhabi, Sharjah airports. 30-day stay extendable once. Very straightforward for Indian passport holders."
    },
    {
        "country": "Thailand",
        "code": "THA",
        "visa_type": "Visa on Arrival / e-Visa",
        "visa_required": False,
        "processing_time": "Instant (on arrival)",
        "fee": "THB 2000 (approx INR 4500) on arrival / Free e-visa",
        "validity": "30 days",
        "required_documents": [
            "Valid Indian passport (minimum 6 months validity)",
            "Return flight ticket",
            "Hotel booking confirmation",
            "Sufficient funds (THB 10,000 per person or THB 20,000 per family)",
            "Passport-size photograph",
            "Completed arrival card"
        ],
        "interview_required": False,
        "notes": "Visa on arrival available at major airports. e-Visa is free and avoids queues. 30-day stay, extendable by 30 days at local immigration office."
    },
    {
        "country": "Singapore",
        "code": "SGP",
        "visa_type": "Tourist Visa",
        "visa_required": True,
        "processing_time": "3-5 working days",
        "fee": "SGD 30",
        "validity": "30 days",
        "required_documents": [
            "Valid Indian passport",
            "Completed visa application form (online)",
            "Recent passport-size photograph",
            "Bank statements (last 3 months)",
            "Employment letter or business proof",
            "Return flight ticket",
            "Hotel booking",
            "Travel insurance"
        ],
        "interview_required": False,
        "notes": "Applied online via ICA website or through authorised agents. Indians with US/UK/Schengen visa may be eligible for VIBE — easier process."
    },
    {
        "country": "Malaysia",
        "code": "MYS",
        "visa_type": "eNTRI / Visa Free",
        "visa_required": False,
        "processing_time": "Instant",
        "fee": "Free",
        "validity": "15 days (eNTRI) / 30 days (visa free)",
        "required_documents": [
            "Valid Indian passport (minimum 6 months validity)",
            "Return flight ticket",
            "Hotel booking",
            "Sufficient funds"
        ],
        "interview_required": False,
        "notes": "Indians can enter Malaysia visa-free for up to 30 days. eNTRI allows 15-day stay via Changi or KLIA. No visa application needed."
    },
    {
        "country": "Japan",
        "code": "JPN",
        "visa_type": "Tourist Visa",
        "visa_required": True,
        "processing_time": "5-7 working days",
        "fee": "INR 800 (single entry) / INR 1600 (multiple entry)",
        "validity": "Single entry 15/30 days, multiple entry 5 years",
        "required_documents": [
            "Valid Indian passport",
            "Visa application form",
            "Recent passport-size photograph",
            "Bank statements (last 3-6 months, minimum INR 3 lakhs balance)",
            "Income Tax Returns (last 2-3 years)",
            "Employment letter",
            "Salary slips (last 3 months)",
            "Detailed travel itinerary (day-by-day)",
            "Hotel bookings for entire stay",
            "Return flight ticket",
            "Tour plan or invitation letter"
        ],
        "interview_required": False,
        "notes": "Apply at Japan Consulate or through authorised agents. Very strict documentation required. Detailed day-by-day itinerary is mandatory. Financial stability is heavily scrutinised."
    },
    {
        "country": "Maldives",
        "code": "MDV",
        "visa_type": "Visa on Arrival",
        "visa_required": False,
        "processing_time": "Instant",
        "fee": "Free",
        "validity": "30 days",
        "required_documents": [
            "Valid Indian passport",
            "Return flight ticket",
            "Hotel/resort booking confirmation",
            "Sufficient funds (USD 100 per day minimum)"
        ],
        "interview_required": False,
        "notes": "Free visa on arrival for all nationalities including Indians. 30-day stay. One of the easiest international destinations for Indians."
    },
    {
        "country": "Sri Lanka",
        "code": "LKA",
        "visa_type": "Electronic Travel Authorization (ETA)",
        "visa_required": True,
        "processing_time": "Instant to 24 hours",
        "fee": "USD 20 (online ETA)",
        "validity": "30 days",
        "required_documents": [
            "Valid Indian passport",
            "Online ETA application (eta.gov.lk)",
            "Return flight ticket",
            "Hotel booking",
            "Sufficient funds"
        ],
        "interview_required": False,
        "notes": "ETA applied online before travel. Very simple process. USD 20 fee paid online. Approval usually within hours."
    },
    {
        "country": "Indonesia",
        "code": "IDN",
        "visa_type": "Visa on Arrival / e-VOA",
        "visa_required": False,
        "processing_time": "Instant",
        "fee": "USD 35",
        "validity": "30 days (extendable once)",
        "required_documents": [
            "Valid Indian passport (minimum 6 months validity)",
            "Return flight ticket",
            "Hotel booking",
            "Sufficient funds"
        ],
        "interview_required": False,
        "notes": "Visa on arrival at major Indonesian airports including Bali (Ngurah Rai). e-VOA available to avoid queues. 30-day stay extendable by 30 days."
    },
    {
        "country": "Nepal",
        "code": "NPL",
        "visa_type": "Visa Free",
        "visa_required": False,
        "processing_time": "Instant",
        "fee": "Free",
        "validity": "Unlimited stay",
        "required_documents": [
            "Valid Indian passport OR any government-issued photo ID",
            "Indians can also use Voter ID card"
        ],
        "interview_required": False,
        "notes": "Indians do not need a passport for Nepal — any government photo ID works. No visa required. Completely free and open border."
    },
    {
        "country": "South Africa",
        "code": "ZAF",
        "visa_type": "Tourist Visa",
        "visa_required": True,
        "processing_time": "10-15 working days",
        "fee": "Free (no visa fee for Indians)",
        "validity": "30 days",
        "required_documents": [
            "Valid Indian passport (minimum 30 days beyond return)",
            "Visa application form (BI-84)",
            "Recent passport-size photographs (2 copies)",
            "Bank statements (last 3 months)",
            "Proof of sufficient funds",
            "Return flight ticket",
            "Hotel bookings",
            "Yellow fever vaccination certificate (if transiting through yellow fever zone)",
            "Travel insurance"
        ],
        "interview_required": False,
        "notes": "No visa fee for Indian nationals. Applied at South African High Commission or VFS Global. Yellow fever certificate may be required depending on travel route."
    },
    {
        "country": "New Zealand",
        "code": "NZL",
        "visa_type": "Visitor Visa",
        "visa_required": True,
        "processing_time": "20-25 working days",
        "fee": "NZD 211",
        "validity": "9 months",
        "required_documents": [
            "Valid Indian passport",
            "Online application (Immigration New Zealand)",
            "Recent passport-size photograph",
            "Bank statements (last 6 months)",
            "Income Tax Returns",
            "Employment letter",
            "Return flight ticket",
            "Hotel bookings",
            "Travel insurance",
            "Proof of ties to India"
        ],
        "interview_required": False,
        "notes": "Fully online application. Biometrics may be required. Processing is slow — apply well in advance. New Zealand is strict about genuine visitor intent."
    },
    {
        "country": "Hong Kong",
        "code": "HKG",
        "visa_type": "Visa Free",
        "visa_required": False,
        "processing_time": "Instant",
        "fee": "Free",
        "validity": "14 days",
        "required_documents": [
            "Valid Indian passport",
            "Return flight ticket",
            "Hotel booking",
            "Sufficient funds proof"
        ],
        "interview_required": False,
        "notes": "Indians can visit Hong Kong visa-free for 14 days. Simple and quick. Longer stays require pre-arrival visa application."
    },
    {
        "country": "Bahrain",
        "code": "BHR",
        "visa_type": "Visa on Arrival / e-Visa",
        "visa_required": False,
        "processing_time": "Instant (on arrival) or 3-5 days (e-visa)",
        "fee": "BHD 5 (approx INR 1100)",
        "validity": "14 days",
        "required_documents": [
            "Valid Indian passport (minimum 6 months validity)",
            "Return flight ticket",
            "Hotel booking",
            "Sufficient funds"
        ],
        "interview_required": False,
        "notes": "Visa on arrival at Bahrain International Airport. e-Visa also available online. 14-day stay for tourism."
    },
    {
        "country": "Qatar",
        "code": "QAT",
        "visa_type": "Visa on Arrival / Hayya Card",
        "visa_required": False,
        "processing_time": "Instant",
        "fee": "Free",
        "validity": "30 days",
        "required_documents": [
            "Valid Indian passport (minimum 6 months validity)",
            "Return flight ticket",
            "Hotel booking or host address",
            "Sufficient funds"
        ],
        "interview_required": False,
        "notes": "Indians get free visa on arrival in Qatar. 30-day stay. Very straightforward process."
    },
    {
        "country": "Oman",
        "code": "OMN",
        "visa_type": "e-Visa",
        "visa_required": True,
        "processing_time": "1-3 working days",
        "fee": "OMR 20 (approx INR 4500)",
        "validity": "30 days",
        "required_documents": [
            "Valid Indian passport (minimum 6 months validity)",
            "Online e-visa application (evisa.rop.gov.om)",
            "Recent passport-size photograph",
            "Return flight ticket",
            "Hotel booking",
            "Bank statements (last 3 months)"
        ],
        "interview_required": False,
        "notes": "e-Visa only — no visa on arrival for Indians. Must apply online before travel. Approval usually within 1-3 days."
    }
]