import random

class CommonSources:
    firstName = {
        "male":[
            "Liam",     "Noah",     "Oliver",   "William",  "Elijah",       "James",
            "Benjamin", "Lucas",    "Mason",    "Ethan",    "Alexander",    "Henry",
            "Jacob",    "Michael",  "Daniel",   "Logan",    "Jackson",      "Sebastian",
            "Jack",     "Aiden",    "Owen",     "Samuel",   "Matthew",      "Joseph",
            "Levi",     "Mateo",    "David",    "John",     "Wyatt",        "Carter",
            "Julian",   "Luke",     "Grayson",  "Isaac",    "Jayden",       "Theodore",
            "Gabriel",  "Anthony",  "Dylan",    "Leo"
        ],
        "female":[
            "Olivia",   "Emma",         "Ava",      "Sophia",       "Isabella",     "Charlotte",
            "Amelia",   "Mia",          "Harper",   "Evelyn",       "Abigail",      "Emily",
            "Ella",     "Elizabeth",    "Camila",   "Luna",         "Sofia",        "Avery",
            "Mila",     "Aria",         "Scarlett", "Penelope",     "Layla",        "Chloe",
            "Victoria", "Madison",      "Eleanor",  "Grace",        "Nora",         "Riley",
            "Zoey",     "Hannah",       "Hazel",    "Lily",         "Ellie",        "Violet",
            "Lillian",  "Zoe",          "Stella",   "Aurora",       "Natalie",      "Emilia",
            "Everly",   "Leah",         "Aubrey",   "Willow",       "Addison",      "Lucy",
            "Audrey",   "Bella",        "Nova",     "Brooklyn",     "Paisley",      "Savannah",
            "Claire",   "Skylar",       "Isla",     "Genesis",      "Naomi",        "Elena",
            "Caroline", "Eliana",       "Anna",     "Maya",         "Valentina",    "Ruby",
            "Kennedy",  "Ivy",          "Ariana",   "Aaliyah",      "Cora",         "Madelyn",
            "Alice",    "Kinsley",      "Hailey",   "Gabriella",    "Allison",      "Gianna",
            "Serenity", "Samantha",     "Sarah",    "Autumn"
        ]
    }
    lastName = [
        "Tremblay",     "Gagnon",   "Roy",      "Côté",         "Bouchard", "Gauthier",
        "Morin",        "Lavoie",   "Fortin",   "Gagné",        "Smith",    "Johnson",
        "Williams",     "Brown",    "Jones",    "Miller",       "Davis",    "Garcia", 
        "Rodriguez",    "Wilson",   "Martinez", "Anderson",     "Taylor",   "Thomas", 
        "Hernandez",    "Moore",    "Martin",   "Jackson",      "Thompson", "White",
        "Lopez",        "Lee",      "Gonzalez", "Harris",       "Clark",    "Lewis",
        "Robinson",     "Walker",   "Perez",    "Hall",         "Young",    "Allen",
        "Sanchez",      "Wright",   "King",     "Scott",        "Green",    "Baker", 
        "Adams",        "Nelson",   "Hill",     "Ramirez",      "Campbell", "Mitchell", 
        "Roberts",      "Carter",   "Phillips", "Evans",        "Turner",   "Torres",
        "Parker",       "Collins",  "Edwards",  "Stewart",      "Flores",   "Morris",
        "Nguyen",       "Murphy",   "Rivera",   "Cook",         "Rogers",   "Morgan",
        "Peterson",     "Cooper",   "Reed",     "Bailey",       "Bell",     "Gomez",
        "Kelly",        "Howard",   "Ward",     "Cox",          "Diaz",     "Richardson",
        "Wood",         "Watson",   "Brooks",   "Bennett",      "Gray",     "James",
        "Reyes",        "Cruz",     "Hughes",   "Price",        "Myers",    "Long",
        "Foster",       "Sanders",  "Ross",     "Morales",      "Powell",   "Sullivan",
        "Russell",      "Ortiz",    "Jenkins",  "Gutierrez",    "Perry",    "Butler",
        "Barnes",       "Fisher"
    ]
    Address_Template = {
        "name": [
            "Lot. {}",
            "No. {}",
            "{}"
        ],
        "street": [
            "Jalan {} {}/{}"
        ]
    }
    Addresses = {
        "street":[
            "Ampang",               "Bangsar",                  "Bukit Bintang",        "Semarang",                 "MARA",                 "Chow Kit",
            "Cochrane",             "Tan Cheng Lock",           "Damansara",            "Dang Wangi",               "Dewan Bahasa",         "Esfahan",
            "Genting Klang",        "Hang Jebat",               "Hang Kasturi",         "Hang Lekir",               "Hang Lekiu",           "Hang Tuah",
            "Imbi",                 "Kinabalu",                 "Kuching",              "Loke Yew",                 "Maharajalela",         "Masjid India",
            "Pasar Besar",          "Pasar Besar",              "Pahang",               "Parlimen",                 "Pantai Baharu",        "Petaling",
            "Pudu",                 "P. Ramlee",                "Raja Chulan",          "Raja Laut",                "Sultan Ismail",        "Sungai Besi",
            "Syed Putra",           "Tuanku Abdul Rahman",      "Tun H S Lee",          "Tun Perak",                "Tun Tan Siew Sin",     "Tun Sambanthan",
            "Yap Ah Loy",           "Yap Kwan Seng",            "Raja Chulan",          "Thambi Dollah",            "Abdul Rahim Kajai",    "Alor",
            "Aminuddin Baki",       "Ampang Hilir",             "Athinahapan",          "Balai Polis",              "Belfield","Bellamy",   "Berhala",
            "Bukit Aman",           "Bukit Petaling",           "Bukit Tunku",          "Burhanuddin Helmi",        "Carutthers",           "Cenderasari",
            "Ceylon",               "Bukit Ceylon",             "Cenderawasih",         "Chan Sow Lin",             "Chan Wing",            "Choo Cheeng Kay",
            "Conlay",               "Dato' Onn",                "Datuk Sulaiman",       "Dewan Sultan Sulaiman",    "Davis",                "Doraisamy",
            "Doktor Latif",         "Eaton",                    "Faraday",              "Foss",                     "Gallagher",            "Galloway",
            "Gereja",               "Haji Yahya Sheikh Ahmad",  "Istana",               "Kampung Attap",            "Kampung Bandar Dalam", "Kebun Bunga",
            "Kia Peng",             "Kinabalu (part of)",       "Ledang",               "Langgak Golf",             "Leong Yew Koh",        "Limbang",
            "Madge",                "Mahkamah Persekutuan",     "Mahkamah Tinggi",      "Melayu",                   "Munshi Abdullah",      "Pasar",
            "Peel",                 "Perdana",                  "Pudu Lama",            "Punchak",                  "Raja",                 "Raja Abdullah",
            "Raja Alang",           "Raja Bot",                 "Raja Muda Abdul Aziz", "Raja Muda Musa",           "Rakyat",               "Ritchie",
            "Robson",               "Robertson",                "Scott",                "Samarahan",                "Semarang",             "Sentul",
            "Serian",               "Sin Chee",                 "Sin Chew Kee",         "Sri Amar",                 "Stadium",              "Changkat Stadium",
            "Shelley",              "Stonor",                   "Tangsi",               "Talalla",                  "Thambipillay",         "Thambusamy",
            "Thavers",              "Travers",                  "Tugu",                 "Tun Abang Haji Openg",     "Tun Ismail",           "Tuanku Abdul Halim",
            "Tun Mohd Fuad",        "Tun Razak",                "Tunku Putra",          "U-Thant",                  "Vivekananda",          "Walter Grenier",
            "Wan Kadir",            "Wesley",                   "Wickham",              "Wisma Putra",              "Yaacob Latif",         "Yap Ah Shak",
            "Yap Tai Chi",          "Yew",                      "Zaaba",                "Abdul Razak Hussin",       "Abdul Rashid",         "Lenggu ak China",
            "Rosli Buang",          "Hamid Ismail",             "Saimun Tarikat",       "Mohana Chandran",          "Binjai",               "Haji Taib",
            "Kuda",                 "Hampshire",                "Maybank",              "Raja Chulan",              "Tuanku Jaafar",        "Tuanku Syed Sirajuddin"
        ],
        "states":[
            "Johor",            "Kedah",        "Kelantan", "Malacca",  "Pahang",   "Penang",
            "Perak",            "Perlis",       "Sabah",    "Sarawak",  "Selangor", "Terengganu",
            "Negeri Sembilan",  "Kuala Lumpur", "Labuan",   "Putrajaya"
        ],
        "state_city":{
            "Johor": [
                "Bakri",        "Batu Pahat",       "Buloh Kasap",          "Chaah",        "Johor Bahru",      "Kampong Dungun",  
                "Kelapa Sawit", "Kluang",           "Kota Tinggi",          "Kulai",        "Labis",            "Mersing",          
                "Muar",         "Parit Raja",       "Pasir Gudang Baru",    "Pekan Nenas",  "Pontian Kechil",   "Segamat",          
                "Sekudai",      "Simpang Renggam",  "Taman Senai",          "Tangkak",      "Ulu Tiram",        "Yong Peng"
            ],
            "Kedah": [
                "Alor Setar",   "Bedong",       "Gurun",        "Jitra",    "Kuah",     "Kuala Kedah",
                "Kulim",        "Pokok Sena",   "Sungai Petan"
            ],
            "Kelantan": [
                "Gua Musang",   "Kampong Kadok",    "Kampong Pangkal Kalong",   "Kampung Lemal",    "Ketereh",  "Kota Bharu",
                "Pasir Mas",    "Peringat",         "Pulai Chondong",           "Tanah Merah",      "Tumpat"
            ],
            "Malacca": [
                "Alor Gajah",           "Asahan",           "Ayer Keroh",       "Batang Melaka",    "Batu Berendam",    "Bemban",
                "Bukit Katil",          "Cheng",            "Durian Tunggal",   "Hang Tuah Jaya",   "Jasin",            "Klebang",
                "Kuala Sungai Baru",    "Lendu",            "Lubuk China",      "Machap Baru",      "Melaka Pindah",    "Masjid Tanah",
                "Merlimau",             "Naning",           "Nyalas",           "Pulau Sebang",     "Ramuan China",     "Selandar",
                "Serkam",               "Simpang Ampat",    "Sungai Rambai",    "Sungai Udang",     "Tanjung Kling",    "Telok Mas and Umbai"
            ],
            "Negeri Sembilan": [
                "Air Kuning Selatan",   "Bahau",                    "Bandar Baru Nilai",    "Bandar Seri Jempol",               "Batang Benar",     "Batu Kikir",
                "Gemas",                "Kota, Negeri Sembilan",    "Kuala Pilah (town)",   "Kuala Sawah",                      "Lukut",            "Mambau",
                "Nilai",                "Nilai 3 Wholesale Centre", "Pajam",                "Pasir Panjang, Negeri Sembilan",   "Pengkalan Kempas", "Port Dickson (town)",
                "Rembau (town)",        "Rompin, Negeri Sembilan",  "Senawang",             "Seremban 2",                       "Seremban 3",       "Seri Menanti",
                "Serting",              "Sikamat",                  "Siliau",               "Simpang Durian",                   "Simpang Pertang",  "Sungai Gadut",
                "Sungai Muntoh",        "Tampin (town)",            "Tanjung Ipoh",         "Teluk Kemang",                     "Tiroi"
            ],
            "Pahang": [
                "Bandar Bera",      "Bandar Muadzam Shah",  "Bandar Tun Abdul Razak",   "Bandar Tun Razak", "Belimbing",    "Benta",
                "Bentong",          "Beserah",              "Blue Valley",              "Brinchang",        "Bukit Ibam",   "Bukit Tinggi",
                "Cherating",        "Gambang",              "Gebeng",                   "Genting Sempah",   "Jerantut",     "Karak",
                "Kemayan",          "Ketari",               "Kota Shahbandar",          "Kuala Simpang",    "Lanchang",     "Lubuk Paku",
                "Lurah Bilut",      "Maran",                "Mengkarak",                "Mentakab",         "Merapoh",      "Nenasi",
                "Paloh Hinai",      "Pekan",                "Penor",                    "Raub",             "Ringlet",      "Sebertak"
                "Sungai Lembing",   "Sungai Ruan",          "Tanah Rata",               "Temerloh",         "Tringkap"
            ],
            "Penang": [
                "Balik Pulau",      "Batu Kawan",       "Bayan Lepas",      "Bukit Mertajam",   "Bukit Tambun",     "Butterworth",
                "Gertak Sanggul",   "Kepala Batas",     "Mak Mandin",       "Nibong Tebal",     "Penanti",          "Perai",
                "Permatang Pauh",   "Pinang Tunggal",   "Simpang Ampat",    "Tasek Gelugor",    "Teluk Air Tawar",  "Teluk Bahang",
                "Teluk Kumbar",     "Val d'Or, Penang"
            ],
            "Perak": [
                "Bagan Serai",  "Batu Gajah",   "Bidor",            "Ipoh",     "Kampar",   "Lumut",
                "Pantai Remis", "Parit Buntar", "Simpang Empat",    "Sitiawan", "Taiping",  "Tapah Road",
                "Teluk Intan",  "Kuala Kangsar"
            ],
            "Perlis": [
                "Arau", "Kangar", "Kuala Perlis"
            ],
            "Sabah": [
                "Beaufort", "Donggongon",   "Keningau",         "Kinarut",  "Kota Belud",   "Kota Kinabalu",
                "Kudat",    "Lahad Datu",   "Papar",            "Putatan",  "Ranau",        "Sandakan",
                "Semporna", "Tawau",        "Bandar Labuan"
            ],
            "Sarawak": [
                "Bintulu",  "Kapit",    "Kuching",      "Limbang",      "Miri",     "Sarikei",
                "Sibu",     "Sri Aman", "Simanggang"
            ],
            "Selangor": [
                "Balakong",         "Bangi",            "Banting",          "Batu Arang",       "Beranang",     "Cyberjaya",
                "Jenjarum",         "Kajang",           "Klang",            "Kuala Selangor",   "Kuang",        "Kundang",
                "Petaling Jaya",    "Puchong",          "Rawang",           "Sabak Bernam",     "Selayang",     "Semenyih",
                "Serendah",         "Seri Kembangan",   "Shah Alam",        "Subang",           "Subang Jaya",  "Sungai Besar",
                "Sungai Pelek",     "Tanjung Karang",   "Tanjung Sepat",    "Batang Berjuntai"
            ],
            "Terengganu":[
                "Cukai",            "Jertih",   "Kertih",   "Kuala Dungun", "Marang","Paka",
                "Kuala Terengganu"
            ],
            "Kuala Lumpur": [],
            "Labuan": [],
            "Putrajaya": []
        }
    }
    clinics = [
        "Dermatology",
        "Internal medicine",
        "Neurology",
        "Obstetrics and gynecology",
        "Ophthalmology",
        "Pediatrics",
        "Psychiatry",
        "Radiation oncology",
    ]
    clinic_reason = {
        "Dermatology":["Acne","Alergy","Blister","Chickenpox"],
        "Internal medicine":["Fever","Cough","Common Cold","Nose problem"],
        "Neurology":["Headach","Insomnia","Epilepsy","Stroke"],
        "Obstetrics and gynecology":["Menstrual Disorder","Pregnancy","Abortion"], #Female
        "Ophthalmology":["Short Sighted","Long Sighted","Astigmatism","Cataract"],
        "Pediatrics":["Fever","Cough","Common Cold","Nose problem"], #Kids
        "Psychiatry":["Stress","Depression","Schizophrenia","Anxiety","Substance Abuse"],
        "Radiation oncology":["Cancer"],
    }
    position = {
        "Misc":["Medical Director","Personnel Officer"],
        "Nurse":["Junior Nurse","Senior Nurse"],
        "Doctor":{
            "Dermatology":"Doctor of Dermatology",
            "Internal medicine":"Doctor of Internal medicine",
            "Neurology":"Doctor of Neurology",
            "Obstetrics and gynecology":"Doctor of Obstetrics and gynecology",
            "Ophthalmology":"Doctor of Ophthalmology",
            "Pediatrics":"Doctor of Pediatrics",
            "Psychiatry":"Doctor of Psychiatry",
            "Radiation oncology":"Doctor of Radiation oncology"
        },
    }
    organization = [
        "Universiti Kebangsaan Malaysia Medical Centre (PPUKM)",
        "Hospital Angkatan Tentera Tuanku Mizan",
        "Hospital Rehabilitasi Cheras",
        "Kuala Lumpur Hospital",
        "University Malaya Specialist Centre (UMSC)",
        "University Malaya Medical Centre",
        "Hospital Port Dickson",
        "Hospital Tampin",
        "Hospital Jelebu",
        "Hospital Jempol",
        "Hospital Rembau",
        "Hospital Jengka",
        "Hospital Muadzam Shah",
        "Hospital Sultan Haji Ahmad Shah, Temerloh",
        "Hospital Cameron Highlands",
        "Hospital Kuala Penyu",
        "Hospital Kudat",
        "Hospital Lahad Datu",
        "Hospital Mesra Bukit Padang",
        "Hospital Papar",
        "Hospital Ranau",
        "Hospital Semporna",
        "Hospital Sipitang",
        "Hospital Tambunan",
        "Hospital Kajang",
        "Hospital Kuala Kubu Baru",
        "Hospital Selayang",
        "Hospital Serdang",
        "Hospital Sungai Buloh",
        "Hospital Tanjung Karang",
    ]
    blocks = [
        "Block North",
        "Block East",
        "Block South",
        "Block West",
        "Central Building"
    ]
    institute = [
        "Universiti Malaya (UM)",
        "Universiti Sains Malaysia (USM)",
        "Universiti Kebangsaan Malaysia (UKM)",
        "Universiti Putra Malaysia (UPM)",
        "Universiti Teknologi Malaysia (UTM)",
        "Universiti Teknologi MARA (UiTM)",
        "Universiti Islam Antarabangsa Malaysia (UIAM)",
        "Universiti Utara Malaysia (UUM)",
        "Universiti Malaysia Sarawak (UNIMAS)",
        "Universiti Malaysia Sabah (UMS)",
        "Universiti Pendidikan Sultan Idris (UPSI)",
        "Universiti Sains Islam Malaysia (USIM)",
        "Universiti Malaysia Terengganu (UMT)",
        "Universiti Tun Hussein Onn Malaysia (UTHM)",
        "Universiti Teknikal Malaysia Melaka (UTeM)",
        "Universiti Malaysia Pahang (UMP)",
        "Universiti Malaysia Perlis (UniMAP)",
        "Sultan Zainal Abidin (UniSZA)",
        "Universiti Malaysia Kelantan (UMK)",
        "Universiti Pertahanan Nasional Malaysia, (UPNM)",
        "Multimedia University (MMU), Cyberjaya",
        "Universiti Tenaga Nasional (UNITEN)",
        "Universiti Tun Abdul Razak (UniRAZAK)",
        "Universiti Teknologi Petronas (UTP)",
        "International Medical University (IMU)",
        "Universiti Selangor (UNISEL)",
        "Open University Malaysia (OUM)",
        "Malaysia University of Science & Technology (MUST)",
        "AIMST University",
        "Universiti Tunku Abdul Rahman (UTAR)",
        "Universiti Kuala Lumpur (UniKL)",
        "Wawasan Open University",
        "Albukhary International University",
        "Al-Madinah International University (MEDIU)",
        "International Centre for Education in Islamic Finance (INCEIF)",
        "Limkokwing University of Creative Technology",
        "Management and Science University (MSU)",
        "Asia e University (AeU)",
        "UCSI University",
        "Quest International University Perak",
        "INTI International University (IIU)",
        "Taylor’s University",
        "Sunway University",
        "Manipal International University",
        "Perdana University",
        "HELP University",
        "UNITAR International University",
        "Raffles University Iskandar (RUI)",
        "Malaysia Institute of Supply Chain Innovation (MISI)",
        "Nilai University",
        "SEGi University",
        "Asia Pacific University of Technology and Innovation (APU)",
        "Binary University of Management and Entrepreneurship",
        "Infrastructure University Kuala Lumpur (IUKL)",
        "Asia Metropolitan University",
        "Putra Business School",
        "Global NXT University",
        "MAHSA University",
        "International University of Malaya-Wales",
        "University Malaysia of Computer Science and Engineering",
        "Universiti Islam Malaysia, Cyberjaya",
        "DRB-HICOM University of Automotive Malaysia",
        "Asia School of Business",
        "City University",
        "Meritus University",
        "Universiti Sultan Azlan Shan",
        "Universiti Islam Antarabangsa Sultan Abdul Halim Mu’adzam Shah",
    ]
    drugs = [
        ["DRG00001", "Atorvastatin",                    30],
        ["DRG00002", "Levothyroxine",                   35],
        ["DRG00003", "Lisinopril",                      20],
        ["DRG00004", "Metformin",                       34],
        ["DRG00005", "Amlodipine",                      32],
        ["DRG00006", "Metoprolol",                      35],
        ["DRG00007", "Albuterol",                       31],
        ["DRG00008", "Omeprazole",                      32],
        ["DRG00009", "Losartan",                        23],
        ["DRG00010", "Simvastatin",                     43],
        ["DRG00011", "Gabapentin",                      23],
        ["DRG00012", "Hydrochlorothiazide",             28],
        ["DRG00013", "Sertraline",                      15],
        ["DRG00014", "Montelukast",                     18],
        ["DRG00015", "Fluticasone",                     38],
        ["DRG00016", "Amoxicillin",                     30],
        ["DRG00017", "Furosemide",                      35],
        ["DRG00018", "Pantoprazole",                    20],
        ["DRG00019", "Prednisone",                      34],
        ["DRG00020", "Escitalopram",                    32],
        ["DRG00021", "Fluoxetine",                      35],
        ["DRG00022", "Dextroamphetamine",               31],
        ["DRG00023", "Insulin Glargine",                32],
        ["DRG00024", "Bupropion",                       23],
        ["DRG00025", "Ibuprofen",                       43],
        ["DRG00026", "Rosuvastatin",                    30],
        ["DRG00027", "Pravastatin Sodium",              35],
        ["DRG00028", "Trazodone",                       20],
        ["DRG00029", "Tamsulosin",                      34],
        ["DRG00030", "Carvedilol",                      32],
        ["DRG00031", "Meloxicam",                       35],
        ["DRG00032", "Citalopram",                      31],
        ["DRG00033", "Duloxetine",                      32],
        ["DRG00034", "Alprazolam",                      23],
        ["DRG00035", "Potassium",                       43],
        ["DRG00036", "Clopidogrel",                     30],
        ["DRG00037", "Atenolol",                        35],
        ["DRG00038", "Cyclobenzaprine",                 20],
        ["DRG00039", "Allopurinol",                     34],
        ["DRG00040", "Venlafaxine",                     32],
        ["DRG00041", "Warfarin",                        35],
        ["DRG00042", "Propranolol",                     31],
        ["DRG00043", "Cetirizine",                      32],
        ["DRG00044", "Estradiol",                       23],
        ["DRG00045", "Lorazepam",                       43],
        ["DRG00046", "Quetiapine",                      24],
        ["DRG00047", "Zolpidem Tartrate",               43],
        ["DRG00048", "Ergocalciferol",                  52],
        ["DRG00049", "Budesonide",                      20],
        ["DRG00050", "Ethinyl Estradiol/Norethindrone", 38],
    ]
    supplies = [
        ["INS00001", "Small", "Adhesive tape"],
        ["INS00002", "Small", "Elastic wrap bandages"],
        ["INS00003", "Small", "Bandage strips and 'butterfly' bandages in assorted sizes"],
        ["INS00004", "Small", "Super glue"],
        ["INS00005", "Small", "Rubber tourniquet or 16 French catheter"],
        ["INS00006", "Small", "Nonstick sterile bandages and roller gauze in assorted sizes"],
        ["INS00007", "Small", "Eye shield or pad"],
        ["INS00008", "Small", "Large triangular bandage (may be used as a sling)"],
        ["INS00009", "Small", "Aluminum finger splint"],
        ["INS00010", "Small", "Instant cold packs"],
        ["INS00011", "Small", "Cotton balls and cotton-tipped swabs"],
        ["INS00012", "Small", "Disposable nonlatex examination gloves, several pairs"],
        ["INS00013", "Small", "Duct tape"],
        ["INS00014", "Small", "Petroleum jelly or other lubricant"],
        ["INS00015", "Small", "Plastic bags, assorted sizes"],
        ["INS00016", "Small", "Safety pins in assorted sizes"],
        ["INS00017", "Small", "Scissors and tweezers"],
        ["INS00018", "Small", "Hand sanitizer"],
        ["INS00019", "Small", "Antibiotic ointment"],
        ["INS00020", "Small", "Antiseptic solution and towelettes"],
        ["INS00021", "Small", "Eyewash solution"],
        ["INS00022", "Small", "Thermometer"],
        ["INS00023", "Small", "Turkey baster or other bulb suction device for flushing wounds"],
        ["INS00024", "Small", "Sterile saline for irrigation, flushing"],
        ["INS00025", "Small", "Breathing barrier (surgical mask)"],
        ["INS00026", "Small", "Syringe, medicine cup or spoon"],
        ["INS00027", "Small", "First-aid manual"],
        ["INS00028", "Small", "Hydrogen peroxide to disinfect"],
        ["INS00029", "Small", "Aloe vera gel"],
        ["INS00030", "Small", "Calamine lotion"],
        ["INS00031", "Small", "Anti-diarrhea medication"],
        ["INS00032", "Small", "Laxative"],
        ["INS00033", "Small", "Antacids"],
        ["INS00034", "Small", "Antihistamine, such as diphenhydramine"],
        ["INS00035", "Small", "Hydrocortisone cream"],
        ["INS00036", "Small", "Cough and cold medications"],
        ["INS00037", "Small", "Personal medications that don't need refrigeration"],
        ["INS00038", "Small", "Auto-injector of epinephrine, if prescribed by your doctor"],
        ["INS00039", "Small", "Pain relievers, such as acetaminophen (Tylenol, others), ibuprofen (Advil, Motrin IB, others)"],
    ]

    def generateGenderedName(self,gender="",lastName=""):
        if not gender:
            gender = random.choice(["male","female"])
        firstName = random.choice(self.firstName[gender])
        if not lastName:
            lastName = random.choice(self.lastName)
        return [firstName,lastName, gender]

    def generateAddress(self,state="",city=""):
        if not state:
            state = random.choice(self.Addresses["states"])
        if (not city) and (self.Addresses["state_city"][state]):
            city = random.choice(self.Addresses["state_city"][state])
        name = random.randint(1,80)
        road = random.choice(self.Addresses["street"])
        road_m, road_n = random.randint(1,50),random.randint(1,50)
        name_tmp = random.choice(self.Address_Template["name"])
        road_tmp = random.choice(self.Address_Template["street"])
        if city:
            sequence = [
                name_tmp.format(name),
                road_tmp.format(road, road_m, road_n),
                city,
                state
            ]
        else:
            sequence = [
                name_tmp.format(name),
                road_tmp.format(road, road_m, road_n),
                state
            ]
        return ", ".join(sequence)

    def generatePhoneNum(self):
        output = "01"
        length = random.randint(8,9)
        for i in range(length):
            output += f"{random.randint(0,9)}"
        return output

    def generateDate(self,yearStart=1940, yearStop=2021):
        year = random.randint(yearStart,yearStop)
        month = random.randint(1,12)
        while True:
            day = random.randint(1,30)
            if not (month == 2 and day > 28):
                return [year, month, day]

    def generateID(self,prefixLength=0,suffixLength=0,prefix="",suffix="",length=8):
        numLength = length
        output = ""
        if prefix:
            numLength -= len(prefix)
            output += prefix
        else:
            numLength -= prefixLength
            for i in range(prefixLength):
                output += chr(random.randint(65,90))
        
        if suffix:
            numLength -= len(suffix)
        else:
            numLength -= suffixLength
            for i in range(suffixLength):
                suffix += chr(random.randint(65,90))

        for i in range(numLength):
            output += f"{random.randint(0,9)}"
        
        return output + suffix

    def generatePrice(self,highest=8000,lowest=3000):
        return f"{random.randint(highest,lowest)}.{random.randint(0,9)}{random.randint(0,9)}"

    def generatePositionClinic(self,positionType=None):
        if not positionType:
            positionType = random.choice(["Misc","Nurse","Doctor"])
        if positionType == "Doctor":
            clinic = random.choice(self.clinics)
            return [self.position[positionType][clinic], clinic, positionType]
        else:
            return [random.choice(self.position[positionType]), None, positionType]

    def generateWorkingExp(self,staff_start,staff_birth,organization="",position="",start=None,duration=0):
        #if no length
        if staff_start[0] - staff_birth[0] < 27:
            return None
        if (random.randint(0,1)):
            year_range_start = staff_birth[0] + 25
            year_range_end = staff_start[0]-1
            if not start:
                start = self.generateDate(year_range_start,year_range_end)
            if not organization:
                organization = random.choice(self.organization)
            if not position:
                position, clinic, position_type = self.generatePositionClinic()
            if not duration:
                duration = random.randint(start[0], staff_start[0] - 1) * 364
            return [organization,position,start,duration]
        else:
            return None

    def generateQualifications(self,birthdate,positionType,clinic,position):
        title = random.choice(["BsC of ", "BsC Hons of ", "Master of "])
        institude = random.choice(self.institute)
        date = self.generateDate(birthdate[0]+24,birthdate[0]+25)
        if positionType == "Misc":
            qualification = title + random.choice(["Medication Management","Healthcare Management","Medication","Hospital Management"])
        elif positionType == "Nurse":
            qualification = title + "Nursing"
        else:
            qualification = title + random.choice(["Bio Chemistry", "Medication", clinic])
        return date, institude, qualification

    def addDate(self,date,day):
        while True:
            date[2] += day
            if (date[1] in (1,3,5,7,8,10,12)) and (date[2] > 31):
                date[1] += 1
                date[2] -= 31
            elif (date[1] in (4,6,9,11)) and (date[2] > 30):
                date[1] += 1
                date[2] -= 30
            elif (date[1] == 2) and (date[0] % 4) and (date[2] > 29):
                date[1] += 1
                date[2] -= 29
            elif (date[1] == 2) and (not (date[0] % 4)) and (date[2] > 28):
                date[1] += 1
                date[2] -= 28
            if date[1] > 12:
                date[0] += 1
                date[1] -= 12
            if (date[1] <= 12):
                condition1 = (date[1] in (1,3,5,7,8,10,12)) and (date[2]<=31)
                condition2 = (date[1] in (4,6,9,11)) and (date[2]<=30)
                leap = not (date[0] % 4)
                if leap:
                    condition3 = (date[2]<=29)
                else:
                    condition3 = (date[2]<=28)
                if condition1 or condition2 or condition3:
                    return date

    def generateTime(self,start_hr=8,end_hr=19):
        time = [
            random.randint(start_hr,end_hr),
            random.randint(0,60),
            random.randint(0,60)
        ]
        return time

    def generateSuppliers(self, n=50):
        data = {}
        names = []
        while len(data) <= n:
            supplierID = self.generateID(prefix="SYR")
            supplierName = random.choice(self.lastName) + random.choice(["Pharmacy SDN BHD","Medication SDN BHD","Medical Supplies SDN BHD","Medicals SDN BHD","Laboratories SDN BHD","Chemicals SDN BHD"])
            if supplierName in names:
                continue
            names.append(supplierName)
            supplierAddress = self.generateAddress()
            supplierTelephone = self.generatePhoneNum()
            supplierFax = self.generateID(prefix="03",length=10)
            data[supplierID] = {
                "name":supplierName,
                "address":supplierAddress,
                "telephone":supplierTelephone,
                "fax":supplierFax,
            }
        return data



s = CommonSources()

def generatePatient(patientmax=100):
    data = {}
    while len(data) < patientmax:
        #GENERATE ID
        pid = s.generateID(prefix="PT")
        if pid in data:
            continue

        #Generate Name Gender
        firstName, lastName, gender = s.generateGenderedName()

        #Generate Address
        address = s.generateAddress()

        #generate Birthdate
        birthdate = s.generateDate(1940, 2020)

        #generate Telephone
        if birthdate[0] <= 2011:
            telephone = s.generatePhoneNum()
        else:
            telephone = None

        #generate Martial Status
        if birthdate[0] >= 2000:
            marital = "Single"
        else:
            marital = random.choice(["Single","Married","Divorced","Widowed"])

        #generate Registered Date
        if birthdate[0] <= 2018:
            registerDate = s.generateDate(2018, 2020)
        else:
            registerDate = s.generateDate(birthdate[0], 2020)

        #generate next to kin
        ntk = []
        for i in ["Father","Mother","Sister","Brother","Spouse"]:
            #get gender
            if i in ["Father","Brother"]:
                ntk_gender = "male"
            elif i in ["Mother","Sister"]:
                ntk_gender = "female"
            elif gender == "male":
                ntk_gender = "female"
            else:
                ntk_gender = "male"
            #get names
            ntk_firstName, ntk_lastName, _ = s.generateGenderedName(gender=ntk_gender)
            #get lastname
            if i in ["Father","Brother","Sister"]:
                ntk_lastName = lastName
            #get address
            ntk_address = address
            if random.randint(0,1):
                ntk_address = s.generateAddress()
            #get telephone
            ntk_telephone = s.generatePhoneNum()
            
            #filters
            if marital == "Widowed" and i == "Spouse":
                continue
            if marital == "Divorced" and i == "Spouse":
                continue
            if marital == "Single" and i == "Spouse":
                continue
            if random.randint(0,1):
                ntk.append({
                    "firstName":ntk_firstName,
                    "lastName":ntk_lastName,
                    "relationship":i,
                    "address":ntk_address,
                    "telephone":ntk_telephone
                })
        data[pid] = {
            "firstName": firstName,
            "lastName":lastName,
            "address":address,
            "telephone":telephone,
            "birthdate":birthdate,
            "gender":gender,
            "marital":marital,
            "register":registerDate,
            "ntk":ntk.copy()
        }
    return data

def generateStaff(staffmax=100):
    data = {}
    while len(data) < staffmax:
        sid = s.generateID(prefix="SF")
        if sid in data:
            continue
        firstName, lastName, gender = s.generateGenderedName()
        address = s.generateAddress()
        phone = s.generatePhoneNum()
        birthdate = s.generateDate(1940,1980)
        nin = s.generateID()
        position, clinic, position_type = s.generatePositionClinic()
        if position == "Junior Nurse":
            salary = s.generatePrice(3000,5000)
            salary_scale = "SL"
        elif position_type in ("Medical Director","Personnel Officer"):
            salary = s.generatePrice(7000,13000)
            salary_scale = "SH"
        else:
            salary = s.generatePrice(5000,9000)
            salary_scale = "SI"
        contract = random.choice(["long","short"])
        start = s.generateDate(birthdate[0]+25, 2015)
        wexp = []
        for i in range(3):
            exp = s.generateWorkingExp(staff_start=start,staff_birth=birthdate)
            if exp: wexp.append(exp)
        q_date, q_institute, q_type = s.generateQualifications(birthdate, position_type, clinic, position)
        data[sid] = {
            "firstName":firstName,
            "lastName":lastName,
            "address":address,
            "telephone":phone,
            "birthdate":birthdate,
            "gender":gender,
            "NIN":nin,
            "position":position,
            "positionType":position_type,
            "clinic":clinic,
            "salary":salary,
            "salaryScale":salary_scale,
            "contract":contract,
            "contractStart":start,
            "wexp":wexp.copy(),
            "qualification_date":q_date,
            "qualification_type":q_type,
            "qualification_institute":q_institute
        }
        if contract == "short":
            duration = random.randint(30, 100)
            data[sid]["duration"] = duration
    return data

def generateOPTIPTAppointment(patients, staffs):
    ipt = {}
    opt = {}
    appointment = {}
    for pid in patients:
        patient = patients[pid]
        date = patient["register"]
        for i in range(3):
            if random.randint(0,1):
                #outpatient
                while True:
                    clinic = random.choice(s.clinics)
                    if not (clinic in s.clinic_reason):
                        continue
                    if (clinic == "Obstetrics and gynecology") and (patient["gender"] == "male"):
                        continue
                    if (clinic == "Obstetrics and gynecology") and (patient["marital"] != "Married"):
                        continue
                    if (clinic == "Pediatrics") and (patient["birthdate"][0] < 2010):
                        continue
                    reason = random.choice(s.clinic_reason[clinic])
                    break
                opt[pid] = {
                    "date":date,
                    "reason":reason,
                    "clinic":clinic
                }
                staff_ids = [s for s in staffs]
                while True:
                    staff_id = random.choice(staff_ids)
                    if staffs[staff_id]["positionType"] in ("Doctor","Nurse"):
                        sid = staff_id
                        break
                appointment[s.generateID(prefix="APM")] = {
                    "PID":pid,
                    "SID":sid,
                    "date":date,
                    "room":s.generateID(prefix="CON"),
                    "time":s.generateTime(),
                }
            else:
                #inpatient
                in_date = date
                in_date[2] += random.randint(0,1)
                if in_date[2] >= 31:
                    in_date[2] = 1
                    in_date[1] += 1
                if in_date[1] >= 13:
                    in_date[0] += 1
                    in_date[1] = 1
                expected_duration = random.randint(7,14)
                out_date = s.addDate(in_date, expected_duration + random.randint(0,1))
                ward_type = random.choice(s.clinics)
                ipt[pid] = {
                    "waitDate":date,
                    "inDate":in_date,
                    "expectedDuration":expected_duration,
                    "outDate":None if out_date[0] >= 2021 else out_date,
                }
                staff_ids = [s for s in staffs]
                while True:
                    staff_id = random.choice(staff_ids)
                    if staffs[staff_id]["positionType"] in ("Doctor","Nurse"):
                        sid = staff_id
                        break
                appointment[s.generateID(prefix="APM")] = {
                    "PID":pid,
                    "SID":sid,
                    "date":date,
                    "room":s.generateID(prefix="CON"),
                    "time":s.generateTime(),
                }
                date = out_date
            if date[0] >= 2021:
                break
            date = s.generateDate(date[0],2020)
    return ipt,opt,appointment

def generateTreatmentDrug(ipts, opts):
    data = {}
    
    for ipt_id, ipt_data in ipts.items():
        ptr_id = s.generateID(prefix="PTR")
        ptr_unit = random.randint(1,6)
        ptr_drug, _, _ = random.choice(s.drugs)
        for j in range(3):
            ptr_start_date = ipt_data["inDate"]
            ptr_duration = ipt_data["expectedDuration"]
            if j == 0:
                data[ptr_id] = {
                    "unitsPerDay":ptr_unit,
                    "start":ptr_start_date,
                    "duration":ptr_duration,
                    "drug":ptr_drug,
                    "patient":ipt_id
                }
            elif random.randint(0,1):
                break

    for opt_id, opt_data in opts.items():
        ptr_id = s.generateID(prefix="PTR")
        ptr_unit = random.randint(1,6)
        ptr_drug, _, _ = random.choice(s.drugs)
        for j in range(3):
            ptr_start_date = opt_data["date"]
            ptr_duration = random.randint(5,14)
            if j == 0:
                data[ptr_id] = {
                    "unitsPerDay":ptr_unit,
                    "start":ptr_start_date,
                    "duration":ptr_duration,
                    "drug":ptr_drug,
                    "patient":opt_id
                }
            elif random.randint(0,1):
                break

    return data

def generateClinics():
    data = {}

    for clinic in s.clinics:
        clinic_id = s.generateID(prefix="CLN")
        clinic_name = clinic
        data[clinic_id] = {
            "name": clinic_name
        }
    
    return data

def generateWards(clinics, staffs, n=10):
    data = {}

    clinics_values = list(clinics.values())
    
    clinic_index = 0
    for _ in range(n):
        clinic_data = clinics_values[clinic_index]

        ward_id = s.generateID(prefix="WAD")
        ward_ext = s.generateID(length=4)
        ward_name = clinic_data["name"]
        ward_location = random.choice(s.blocks)
        
        def get_new_random_staff():
            return random.choice(list(staffs.items()))
        staff_id, staff_data = get_new_random_staff()
        while staff_data["positionType"] != "Nurse":
            staff_id, staff_data = get_new_random_staff()

        ward_nurse = staff_id

        data[ward_id] = {
            "ext": ward_ext,
            "name": ward_name,
            "location": ward_location,
            "nurse": ward_nurse
        }

        clinic_index += 1
        if clinic_index == len(clinics):
            clinic_index = 0
    
    return data

def generateBeds(wards, n = 240):
    data = {}

    wards_ids = list(wards.keys())

    ward_index = 0
    for _ in range(n):
        ward_id = wards_ids[ward_index]

        bed_id = s.generateID(prefix="BED")
        bed_type = ""
        bed_ward = ward_id
        data[bed_id] = {
            "type": bed_type,
            "ward": bed_ward
        }

        ward_index += 1
        if ward_index == len(wards):
            ward_index = 0

    return data

def generateSupplySuppliers():
    suppliers = s.generateSuppliers()
    for i in suppliers:
        supplier = suppliers[i]
        supplier["drugs"] = []
        supplier["equipments"] = []
    supplier_index = 0
    drug_index = 0
    supplier_key = list(suppliers.keys())[supplier_index]
    while drug_index < len(s.drugs):
        suppliers[supplier_key]["drugs"].append(s.drugs[drug_index])
        supplier_index += 1
        drug_index += 1
        if supplier_index >= len(suppliers):
            supplier_index = 0
        supplier_key = list(suppliers.keys())[supplier_index]
    equipement_index = 0
    supplier_index = 0
    supplier_key = list(suppliers.keys())[supplier_index]
    while equipement_index < len(s.supplies):
        suppliers[supplier_key]["equipments"].append(s.supplies[equipement_index])
        equipement_index += 1
        supplier_index += 1
        supplier_key = list(suppliers.keys())[supplier_index]
    return suppliers
