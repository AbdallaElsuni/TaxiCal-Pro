__all__ = ['City', 'alabama_cities', 'alaska_cities', 'arizona_cities', 'arkansas_cities', 'california_cities', 'colorado_cities', 'connecticut_cities', 'delaware_cities', 'florida_cities', 'georgia_cities', 'hawaii_cities', 'idaho_cities', 'illinois_cities', 'indiana_cities', 'iowa_cities', 'kansas_cities', 'kentucky_cities', 'louisiana_cities', 'maine_cities', 'maryland_cities', 'massachusetts_cities', 'michigan_cities', 'minnesota_cities', 'mississippi_cities', 'missouri_cities', 'montana_cities', 'nebraska_cities', 'nevada_cities', 'new_hampshire_cities', 'new_jersey_cities', 'new_mexico_cities', 'new_york_cities', 'north_carolina_cities', 'north_dakota_cities', 'ohio_cities', 'oklahoma_cities', 'oregon_cities', 'pennsylvania_cities', 'rhode_island_cities', 'south_carolina_cities', 'south_dakota_cities', 'tennessee_cities', 'texas_cities', 'utah_cities', 'vermont_cities', 'virginia_cities', 'washington_cities', 'west_virginia_cities', 'wisconsin_cities', 'wyoming_cities']

from enum import Enum
class CustomEnum(Enum):
    def __str__(self):
        return self.name
class City(str, CustomEnum):
    UnSpecifiedCity = "UnSpecifiedCity"
    # California
    LosAngeles = "LosAngeles"
    SanDiego = "SanDiego"
    SanJose = "SanJose"
    SanFrancisco = "SanFrancisco"
    Fresno = "Fresno"
    Sacramento = "Sacramento"
    LongBeach = "LongBeach"
    Oakland = "Oakland"
    Bakersfield = "Bakersfield"
    Anaheim = "Anaheim"
    SantaAna = "SantaAna"
    Riverside = "Riverside"
    Stockton = "Stockton"
    ChulaVista = "ChulaVista"
    Irvine = "Irvine"
    Fremont = "Fremont"
    SanBernardino = "SanBernardino"
    Modesto = "Modesto"
    Fontana = "Fontana"
    Oxnard = "Oxnard"
    MorenoValley = "MorenoValley"
    HuntingtonBeach = "HuntingtonBeach"
    Glendale = "Glendale"
    SantaClarita = "SantaClarita"
    GardenGrove = "GardenGrove"
    Oceanside = "Oceanside"
    RanchoCucamonga = "RanchoCucamonga"
    SantaRosa = "SantaRosa"
    Ontario = "Ontario"
    ElkGrove = "ElkGrove"
    Corona = "Corona"
    Lancaster = "Lancaster"
    Palmdale = "Palmdale"
    Salinas = "Salinas"
    Hayward = "Hayward"
    Pomona = "Pomona"
    Escondido = "Escondido"
    Sunnyvale = "Sunnyvale"
    Torrance = "Torrance"
    Pasadena = "Pasadena"
    Orange = "Orange"
    Fullerton = "Fullerton"
    ThousandOaks = "ThousandOaks"
    Visalia = "Visalia"
    SimiValley = "SimiValley"
    Concord = "Concord"
    Roseville = "Roseville"
    Victorville = "Victorville"
    SantaClara = "SantaClara"
    Vallejo = "Vallejo"
    Berkeley = "Berkeley"
    ElMonte = "ElMonte"
    Downey = "Downey"
    CostaMesa = "CostaMesa"
    Inglewood = "Inglewood"
    Carlsbad = "Carlsbad"
    SanBuenaventura = "SanBuenaventura"
    Fairfield = "Fairfield"
    WestCovina = "WestCovina"
    Murrieta = "Murrieta"
    Richmond = "Richmond"
    Norwalk = "Norwalk"
    Antioch = "Antioch"
    Temecula = "Temecula"
    Burbank = "Burbank"
    DalyCity = "DalyCity"
    Rialto = "Rialto"
    SantaMaria = "SantaMaria"
    ElCajon = "ElCajon"
    SanMateo = "SanMateo"
    Clovis = "Clovis"
    Compton = "Compton"
    JurupaValley = "JurupaValley"
    Vista = "Vista"
    SouthGate = "SouthGate"
    MissionViejo = "MissionViejo"
    Vacaville = "Vacaville"
    Carson = "Carson"
    Hesperia = "Hesperia"
    Redding = "Redding"
    SantaMonica = "SantaMonica"
    Westminster = "Westminster"
    SantaBarbara = "SantaBarbara"
    Chico = "Chico"
    Whittier = "Whittier"
    NewportBeach = "NewportBeach"
    SanLeandro = "SanLeandro"
    Hawthorne = "Hawthorne"
    SanMarcos = "SanMarcos"
    CitrusHeights = "CitrusHeights"
    Alhambra = "Alhambra"
    Tracy = "Tracy"
    Livermore = "Livermore"
    BuenaPark = "BuenaPark"
    Lakewood = "Lakewood"
    Merced = "Merced"
    Hemet = "Hemet"
    Chino = "Chino"
    Menifee = "Menifee"
    LakeForest = "LakeForest"
    Napa = "Napa"
    RedwoodCity = "RedwoodCity"
    Bellflower = "Bellflower"
    Perris = "Perris"
    Folsom = "Folsom"
    Tustin = "Tustin"
    Lynwood = "Lynwood"
    AppleValley = "AppleValley"
    Manteca = "Manteca"
    BaldwinPark = "BaldwinPark"
    ChinoHills = "ChinoHills"
    Upland = "Upland"
    MountainView = "MountainView"
    NapaValley = "NapaValley"
    Camarillo = "Camarillo"
    Davis = "Davis"
    YorbaLinda = "YorbaLinda"
    WalnutCreek = "WalnutCreek"
    Redlands = "Redlands"
    PaloAlto = "PaloAlto"
    RedondoBeach = "RedondoBeach"
    # New York State
    NewYorkCity = "NewYorkCity"
    Buffalo = "Buffalo"
    Rochester = "Rochester"
    Yonkers = "Yonkers"
    Syracuse = "Syracuse"
    Albany = "Albany"
    NewRochelle = "NewRochelle"
    MountVernon = "MountVernon"
    Schenectady = "Schenectady"
    Utica = "Utica"
    WhitePlains = "WhitePlains"
    Hempstead = "Hempstead"
    Troy = "Troy"
    NiagaraFalls = "NiagaraFalls"
    Binghamton = "Binghamton"
    Freeport = "Freeport"
    ValleyStream = "ValleyStream"
    # Texas
    Houston = "Houston"
    SanAntonio = "SanAntonio"
    Dallas = "Dallas"
    Austin = "Austin"
    FortWorth = "FortWorth"
    ElPaso = "ElPaso"
    Arlington = "Arlington"
    CorpusChristi = "CorpusChristi"
    Plano = "Plano"
    Laredo = "Laredo"
    Lubbock = "Lubbock"
    Garland = "Garland"
    Irving = "Irving"
    Amarillo = "Amarillo"
    GrandPrairie = "GrandPrairie"
    McKinney = "McKinney"
    Frisco = "Frisco"
    Brownsville = "Brownsville"
    PasadenaTexas = "PasadenaTexas"
    Killeen = "Killeen"
    McAllen = "McAllen"
    Mesquite = "Mesquite"
    Midland = "Midland"
    Denton = "Denton"
    Waco = "Waco"
    Carrollton = "Carrollton"
    RoundRock = "RoundRock"
    Abilene = "Abilene"
    Odessa = "Odessa"
    Pearland = "Pearland"
    Richardson = "Richardson"
    SugarLand = "SugarLand"
    Beaumont = "Beaumont"
    CollegeStation = "CollegeStation"
    Lewisville = "Lewisville"
    LeagueCity = "LeagueCity"
    Tyler = "Tyler"
    WichitaFalls = "WichitaFalls"
    Allen = "Allen"
    SanAngelo = "SanAngelo"
    Edinburg = "Edinburg"
    Conroe = "Conroe"
    Bryan = "Bryan"
    Mission = "Mission"
    NewBraunfels = "NewBraunfels"
    Longview = "Longview"
    Pharr = "Pharr"
    Baytown = "Baytown"
    FlowerMound = "FlowerMound"
    CedarPark = "CedarPark"
    Temple = "Temple"
    MissouriCity = "MissouriCity"
    Georgetown = "Georgetown"
    NorthRichlandHills = "NorthRichlandHills"
    Mansfield = "Mansfield"
    Victoria = "Victoria"
    Harlingen = "Harlingen"
    Rowlett = "Rowlett"
    Pflugerville = "Pflugerville"
    Spring = "Spring"
    Euless = "Euless"
    DeSoto = "DeSoto"
    Grapevine = "Grapevine"
    Galveston = "Galveston"
    Bedford = "Bedford"
    CedarHill = "CedarHill"
    TexasCity = "TexasCity"
    HaltomCity = "HaltomCity"
    TheWoodlands = "TheWoodlands"
    # Minnesota
    Minneapolis = "Minneapolis"
    SaintPaul = "SaintPaul"
    RochesterMN = "RochesterMN"
    Duluth = "Duluth"
    BloomingtonMinnesota = "BloomingtonMinnesota"
    BrooklynPark = "BrooklynPark"
    Plymouth = "Plymouth"
    Woodbury = "Woodbury"
    MapleGrove = "MapleGrove"
    SaintCloud = "SaintCloud"
    Eagan = "Eagan"
    EdenPrairie = "EdenPrairie"
    CoonRapids = "CoonRapids"
    Burnsville = "Burnsville"
    Blaine = "Blaine"
    Lakeville = "Lakeville"
    Minnetonka = "Minnetonka"
    AppleValleyMinnesota = "AppleValleyMinnesota"
    StLouisPark = "StLouisPark"
    Moorhead = "Moorhead"
    # Alabama
    Birmingham = "Birmingham"
    Montgomery = "Montgomery"
    Huntsville = "Huntsville"
    Mobile = "Mobile"
    Tuscaloosa = "Tuscaloosa"
    Hoover = "Hoover"
    Dothan = "Dothan"
    Auburn = "Auburn"
    Decatur = "Decatur"
    Madison = "Madison"
    FlorenceAlabama = "FlorenceAlabama"
    Prattville = "Prattville"
    Gadsden = "Gadsden"
    VestaviaHills = "VestaviaHills"
    PhenixCity = "PhenixCity"
    # Alaska
    Anchorage = "Anchorage"
    Fairbanks = "Fairbanks"
    Juneau = "Juneau"
    Sitka = "Sitka"
    Ketchikan = "Ketchikan"
    Wasilla = "Wasilla"
    Kenai = "Kenai"
    Palmer = "Palmer"
    Kodiak = "Kodiak"
    Bethel = "Bethel"
    # Arizona
    Phoenix = "Phoenix"
    Tucson = "Tucson"
    Mesa = "Mesa"
    Chandler = "Chandler"
    Scottsdale = "Scottsdale"
    Gilbert = "Gilbert"
    Tempe = "Tempe"
    PeoriaArizona = "PeoriaArizona"
    Surprise = "Surprise"
    Yuma = "Yuma"
    Goodyear = "Goodyear"
    Flagstaff = "Flagstaff"
    LakeHavasuCity = "LakeHavasuCity"
    Avondale = "Avondale"
    CasaGrande = "CasaGrande"
    # Arkansas
    LittleRock = "LittleRock"
    FortSmith = "FortSmith"
    Fayetteville = "Fayetteville"
    Springdale = "Springdale"
    Jonesboro = "Jonesboro"
    Conway = "Conway"
    Rogers = "Rogers"
    PineBluff = "PineBluff"
    Bentonville = "Bentonville"
    HotSprings = "HotSprings"
    # Colorado
    Denver = "Denver"
    ColoradoSprings = "ColoradoSprings"
    Aurora = "Aurora"
    FortCollins = "FortCollins"
    LakewoodColorado = "LakewoodColorado"
    Thornton = "Thornton"
    Arvada = "Arvada"
    WestminsterColorado = "WestminsterColorado"
    Centennial = "Centennial"
    Boulder = "Boulder"

    # Connecticut
    Bridgeport = "Bridgeport"
    NewHaven = "NewHaven"
    Stamford = "Stamford"
    Hartford = "Hartford"
    Waterbury = "Waterbury"
    NorwalkConnecticut = "NorwalkConnecticut"
    Danbury = "Danbury"
    NewBritain = "NewBritain"
    Meriden = "Meriden"
    Bristol = "Bristol"

    # Delaware
    Wilmington = "Wilmington"
    Dover = "Dover"
    NewarkDelaware = "NewarkDelaware"  # To prevent confusion with Newark, NJ
    Middletown = "Middletown"
    Smyrna = "Smyrna"
    # Florida
    Jacksonville = "Jacksonville"
    Miami = "Miami"
    Tampa = "Tampa"
    Orlando = "Orlando"
    StPetersburg = "StPetersburg"
    Hialeah = "Hialeah"
    Tallahassee = "Tallahassee"
    FortLauderdale = "FortLauderdale"
    PortStLucie = "PortStLucie"
    CapeCoral = "CapeCoral"
    PembrokePines = "PembrokePines"
    HollywoodFL = "HollywoodFL"  # To avoid confusion with Hollywood, CA
    Miramar = "Miramar"
    Gainesville = "Gainesville"
    CoralSprings = "CoralSprings"

    # Georgia
    Atlanta = "Atlanta"
    ColumbusGA = "ColumbusGA"  # To avoid confusion with Columbus, OH
    Augusta = "Augusta"
    Macon = "Macon"
    Savannah = "Savannah"
    Athens = "Athens"
    SandySprings = "SandySprings"
    RoswellGeorgia = "RoswellGeorgia"
    JohnsCreek = "JohnsCreek"
    WarnerRobins = "WarnerRobins"

    # Hawaii
    Honolulu = "Honolulu"
    Hilo = "Hilo"
    Kailua = "Kailua"
    Kaneohe = "Kaneohe"
    Kahului = "Kahului"
    PearlCity = "PearlCity"
    Waipahu = "Waipahu"
    Mililani = "Mililani"
    Kihei = "Kihei"
    Lihue = "Lihue"
    # Idaho
    Boise = "Boise"
    MeridianIdaho = "MeridianIdaho"
    Nampa = "Nampa"
    IdahoFalls = "IdahoFalls"
    Pocatello = "Pocatello"
    Caldwell = "Caldwell"
    CoeurdAlene = "CoeurdAlene"
    TwinFalls = "TwinFalls"
    PostFalls = "PostFalls"
    Rexburg = "Rexburg"

    # Illinois
    Chicago = "Chicago"
    AuroraIL = "AuroraIL"  # To avoid confusion with Aurora, CO
    Rockford = "Rockford"
    Joliet = "Joliet"
    Naperville = "Naperville"
    SpringfieldIL = "SpringfieldIL"  # To avoid confusion with Springfield, MA
    PeoriaIllinois = "PeoriaIllinois"
    Elgin = "Elgin"
    Waukegan = "Waukegan"
    Cicero = "Cicero"
    Champaign = "Champaign"

    # Indiana
    Indianapolis = "Indianapolis"
    FortWayne = "FortWayne"
    Evansville = "Evansville"
    SouthBend = "SouthBend"
    Carmel = "Carmel"
    Fishers = "Fishers"
    BloomingtonIndiana = "BloomingtonIndiana"
    Hammond = "Hammond"
    Gary = "Gary"
    Lafayette = "Lafayette"
    # Iowa
    DesMoines = "DesMoines"
    CedarRapids = "CedarRapids"
    Davenport = "Davenport"
    SiouxCity = "SiouxCity"
    Waterloo = "Waterloo"
    IowaCity = "IowaCity"
    CouncilBluffs = "CouncilBluffs"
    Ames = "Ames"
    Dubuque = "Dubuque"
    Ankeny = "Ankeny"

    # Kansas
    Wichita = "Wichita"
    OverlandPark = "OverlandPark"
    KansasCityKansas = "KansasCityKansas"  # To avoid confusion with Kansas City, MO
    Olathe = "Olathe"
    Topeka = "Topeka"
    Lawrence = "Lawrence"
    Shawnee = "Shawnee"
    Manhattan = "Manhattan"
    Lenexa = "Lenexa"
    Salina = "Salina"

    # Kentucky
    Louisville = "Louisville"
    Lexington = "Lexington"
    BowlingGreen = "BowlingGreen"
    Owensboro = "Owensboro"
    Covington = "Covington"
    Hopkinsville = "Hopkinsville"
    RichmondKentucky = "RichmondKentucky"  # To avoid confusion with Richmond, VA
    Florence = "Florence"
    GeorgetownKentucky = "GeorgetownKentucky"
    Nicholasville = "Nicholasville"
    # Louisiana
    NewOrleans = "NewOrleans"
    BatonRouge = "BatonRouge"
    Shreveport = "Shreveport"
    LafayetteLouisiana = "LafayetteLouisiana"
    LakeCharles = "LakeCharles"
    Kenner = "Kenner"
    BossierCity = "BossierCity"
    MonroeLouisiana = "MonroeLouisiana"
    AlexandriaLouisiana = "AlexandriaLouisiana"
    Houma = "Houma"

    # Maine
    PortlandMaine = "PortlandMaine"
    Lewiston = "Lewiston"
    Bangor = "Bangor"
    SouthPortland = "SouthPortland"
    AuburnMaine = "AuburnMaine"
    Biddeford = "Biddeford"
    Sanford = "Sanford"
    Saco = "Saco"
    AugustaMaine = "AugustaMaine"
    Westbrook = "Westbrook"

    # Maryland
    Baltimore = "Baltimore"
    ColumbiaMaryland = "ColumbiaMaryland"
    Germantown = "Germantown"
    SilverSpring = "SilverSpring"
    Waldorf = "Waldorf"
    GlenBurnie = "GlenBurnie"
    EllicottCity = "EllicottCity"
    Frederick = "Frederick"
    Rockville = "Rockville"
    Gaithersburg = "Gaithersburg"
    # Massachusetts
    Boston = "Boston"
    Worcester = "Worcester"
    SpringfieldMassachusetts = "SpringfieldMassachusetts"
    Cambridge = "Cambridge"
    Lowell = "Lowell"
    Brockton = "Brockton"
    Quincy = "Quincy"
    Lynn = "Lynn"
    NewBedford = "NewBedford"
    FallRiver = "FallRiver"

    # Michigan
    Detroit = "Detroit"
    GrandRapids = "GrandRapids"
    Warren = "Warren"
    SterlingHeights = "SterlingHeights"
    AnnArbor = "AnnArbor"
    Lansing = "Lansing"
    Dearborn = "Dearborn"
    Livonia = "Livonia"
    TroyMichigan = "TroyMichigan"
    FarmingtonHills = "FarmingtonHills"

    # Mississippi
    JacksonMississippi = "JacksonMississippi"
    Gulfport = "Gulfport"
    Southaven = "Southaven"
    Hattiesburg = "Hattiesburg"
    Biloxi = "Biloxi"
    MeridianMississippi = "MeridianMississippi"
    Tupelo = "Tupelo"
    GreenvilleMississippi = "GreenvilleMississippi"
    OliveBranch = "OliveBranch"
    HornLake = "HornLake"

    # Missouri
    KansasCityMissouri = "KansasCityMissouri"
    StLouis = "StLouis"
    SpringfieldMissouri = "SpringfieldMissouri"
    ColumbiaMissouri = "ColumbiaMissouri"
    Independence = "Independence"
    LeeSummit = "LeeSummit"
    OFallon = "OFallon"
    StJoseph = "StJoseph"
    StCharles = "StCharles"
    BlueSprings = "BlueSprings"

    # Montana
    Billings = "Billings"
    Missoula = "Missoula"
    GreatFalls = "GreatFalls"
    Bozeman = "Bozeman"
    Butte = "Butte"
    HelenaMontana = "HelenaMontana"
    Kalispell = "Kalispell"
    Havre = "Havre"
    Anaconda = "Anaconda"
    MilesCity = "MilesCity"

    # Nebraska
    Omaha = "Omaha"
    LincolnNebraska = "LincolnNebraska"
    BellevueNebraska = "BellevueNebraska"
    GrandIsland = "GrandIsland"
    Kearney = "Kearney"
    FremontNebraska = "FremontNebraska"
    Hastings = "Hastings"
    NorfolkNebraska = "NorfolkNebraska"
    NorthPlatte = "NorthPlatte"
    Papillion = "Papillion"
    # Nevada
    LasVegas = "LasVegas"
    Henderson = "Henderson"
    Reno = "Reno"
    NorthLasVegas = "NorthLasVegas"
    Sparks = "Sparks"
    CarsonCityNevada = "CarsonCityNevada"
    Fernley = "Fernley"
    Elko = "Elko"
    BoulderCity = "BoulderCity"
    MesquiteNevada = "MesquiteNevada"

    # New Hampshire
    ManchesterNewHampshire = "ManchesterNewHampshire"
    Nashua = "Nashua"
    ConcordNewHampshire = "ConcordNewHampshire"
    Derry = "Derry"
    RochesterNewHampshire = "RochesterNewHampshire"
    SalemNewHampshire = "SalemNewHampshire"
    DoverNewHampshire = "DoverNewHampshire"
    Merrimack = "Merrimack"
    Londonderry = "Londonderry"
    HudsonNewHampshire = "HudsonNewHampshire"

    # New Jersey
    NewarkNewJersey = "NewarkNewJersey"
    JerseyCity = "JerseyCity"
    Paterson = "Paterson"
    Elizabeth = "Elizabeth"
    Edison = "Edison"
    WoodbridgeTownship = "WoodbridgeTownship"
    LakewoodTownship = "LakewoodTownship"
    TomsRiver = "TomsRiver"
    HamiltonTownshipNewJersey = "HamiltonTownshipNewJersey"
    Trenton = "Trenton"
    # New Mexico
    Albuquerque = "Albuquerque"
    LasCruces = "LasCruces"
    RioRancho = "RioRancho"
    SantaFeNewMexico = "SantaFeNewMexico"
    RoswellNewMexico = "RoswellNewMexico"
    FarmingtonNewMexico = "FarmingtonNewMexico"
    ClovisNewMexico = "ClovisNewMexico"
    Hobbs = "Hobbs"
    Alamogordo = "Alamogordo"
    CarlsbadNewMexico = "CarlsbadNewMexico"

    # North Carolina
    Charlotte = "Charlotte"
    Raleigh = "Raleigh"
    Greensboro = "Greensboro"
    Durham = "Durham"
    WinstonSalem = "WinstonSalem"
    FayettevilleNorthCarolina = "FayettevilleNorthCarolina"
    Cary = "Cary"
    WilmingtonNorthCarolina = "WilmingtonNorthCarolina"
    HighPoint = "HighPoint"
    GreenvilleNorthCarolina = "GreenvilleNorthCarolina"

    # North Dakota
    Fargo = "Fargo"
    Bismarck = "Bismarck"
    GrandForks = "GrandForks"
    Minot = "Minot"
    WestFargo = "WestFargo"
    WillistonNorthDakota = "WillistonNorthDakota"
    Dickinson = "Dickinson"
    Mandan = "Mandan"
    Jamestown = "Jamestown"
    Wahpeton = "Wahpeton"

    # Ohio
    ColumbusOhio = "ColumbusOhio"
    Cleveland = "Cleveland"
    Cincinnati = "Cincinnati"
    Toledo = "Toledo"
    Akron = "Akron"
    Dayton = "Dayton"
    Parma = "Parma"
    CantonOhio = "CantonOhio"
    Youngstown = "Youngstown"
    Lorain = "Lorain"

    # Oklahoma
    OklahomaCity = "OklahomaCity"
    Tulsa = "Tulsa"
    Norman = "Norman"
    BrokenArrow = "BrokenArrow"
    Lawton = "Lawton"
    Edmond = "Edmond"
    Moore = "Moore"
    MidwestCity = "MidwestCity"
    Enid = "Enid"
    Stillwater = "Stillwater"

    # Oregon
    PortlandOregon = "PortlandOregon"
    SalemOregon = "SalemOregon"
    Eugene = "Eugene"
    Gresham = "Gresham"
    Hillsboro = "Hillsboro"
    Beaverton = "Beaverton"
    Bend = "Bend"
    Medford = "Medford"
    SpringfieldOregon = "SpringfieldOregon"
    Corvallis = "Corvallis"

    # Pennsylvania
    Philadelphia = "Philadelphia"
    Pittsburgh = "Pittsburgh"
    Allentown = "Allentown"
    Erie = "Erie"
    Reading = "Reading"
    Scranton = "Scranton"
    Bethlehem = "Bethlehem"
    LancasterPennsylvania = "LancasterPennsylvania"
    Levittown = "Levittown"
    Harrisburg = "Harrisburg"

    # Rhode Island
    Providence = "Providence"
    Cranston = "Cranston"
    Warwick = "Warwick"
    Pawtucket = "Pawtucket"
    EastProvidence = "EastProvidence"
    Woonsocket = "Woonsocket"
    Cumberland = "Cumberland"
    CoventryRhodeIsland = "CoventryRhodeIsland"
    NorthProvidence = "NorthProvidence"
    WestWarwick = "WestWarwick"

    # South Carolina
    ColumbiaSouthCarolina = "ColumbiaSouthCarolina"
    Charleston = "Charleston"
    NorthCharleston = "NorthCharleston"
    MountPleasant = "MountPleasant"
    RockHill = "RockHill"
    GreenvilleSouthCarolina = "GreenvilleSouthCarolina"
    Summerville = "Summerville"
    Sumter = "Sumter"
    GooseCreek = "GooseCreek"
    HiltonHeadIsland = "HiltonHeadIsland"

    # South Dakota
    SiouxFalls = "SiouxFalls"
    RapidCity = "RapidCity"
    Aberdeen = "Aberdeen"
    Watertown = "Watertown"
    Brookings = "Brookings"
    Mitchell = "Mitchell"
    Yankton = "Yankton"
    Pierre = "Pierre"
    Huron = "Huron"
    Vermillion = "Vermillion"

    # Tennessee
    Nashville = "Nashville"
    Memphis = "Memphis"
    Knoxville = "Knoxville"
    Chattanooga = "Chattanooga"
    Clarksville = "Clarksville"
    Murfreesboro = "Murfreesboro"
    FranklinTennessee = "FranklinTennessee"
    JohnsonCity = "JohnsonCity"
    JacksonTennessee = "JacksonTennessee"
    Hendersonville = "Hendersonville"

    # Utah
    SaltLakeCity = "SaltLakeCity"
    WestValleyCity = "WestValleyCity"
    Provo = "Provo"
    WestJordan = "WestJordan"
    Orem = "Orem"
    SandyUtah = "SandyUtah"
    Ogden = "Ogden"
    StGeorgeUtah = "StGeorgeUtah"
    Layton = "Layton"
    Taylorsville = "Taylorsville"

    # Vermont
    Burlington = "Burlington"
    Essex = "Essex"
    SouthBurlington = "SouthBurlington"
    Colchester = "Colchester"
    Rutland = "Rutland"
    Bennington = "Bennington"
    Milton = "Milton"
    Barre = "Barre"
    WillistonVermont = "WillistonVermont"
    HartfordVermont = "HartfordVermont"

    # Virginia
    VirginiaBeach = "VirginiaBeach"
    Norfolk = "Norfolk"
    Chesapeake = "Chesapeake"
    RichmondVirginia = "RichmondVirginia"
    NewportNews = "NewportNews"
    AlexandriaVirginia = "AlexandriaVirginia"
    Hampton = "Hampton"
    Roanoke = "Roanoke"
    PortsmouthVirginia = "PortsmouthVirginia"
    Suffolk = "Suffolk"

    # Washington
    Seattle = "Seattle"
    Spokane = "Spokane"
    Tacoma = "Tacoma"
    VancouverWashington = "VancouverWashington"
    BellevueWashington = "BellevueWashington"
    Kent = "Kent"
    Everett = "Everett"
    Renton = "Renton"
    FederalWay = "FederalWay"
    SpokaneValley = "SpokaneValley"

    # West Virginia
    CharlestonWestVirginia = "CharlestonWestVirginia"
    Huntington = "Huntington"
    Parkersburg = "Parkersburg"
    Morgantown = "Morgantown"
    Wheeling = "Wheeling"
    Beckley = "Beckley"
    Fairmont = "Fairmont"
    Martinsburg = "Martinsburg"
    Clarksburg = "Clarksburg"
    Weirton = "Weirton"

    # Wisconsin
    Milwaukee = "Milwaukee"
    MadisonWisconsin = "MadisonWisconsin"
    GreenBay = "GreenBay"
    Kenosha = "Kenosha"
    Racine = "Racine"
    Appleton = "Appleton"
    Waukesha = "Waukesha"
    EauClaire = "EauClaire"
    Oshkosh = "Oshkosh"
    Janesville = "Janesville"

    # Wyoming
    Cheyenne = "Cheyenne"
    Casper = "Casper"
    Laramie = "Laramie"
    Gillette = "Gillette"
    RockSprings = "RockSprings"
    Sheridan = "Sheridan"
    Evanston = "Evanston"
    Riverton = "Riverton"
    Cody = "Cody"
    JacksonWyoming = "JacksonWyoming"

# Alabama
alabama_cities = [City.Birmingham, City.Montgomery, City.Huntsville, City.Mobile, City.Tuscaloosa,
                  City.Hoover, City.Dothan, City.Auburn, City.Decatur, City.Madison,
                  City.FlorenceAlabama, City.Prattville, City.Gadsden, City.VestaviaHills, City.PhenixCity]
# Alaska
alaska_cities = [City.Anchorage, City.Fairbanks, City.Juneau, City.Sitka, City.Ketchikan,
                City.Wasilla, City.Kenai, City.Palmer, City.Kodiak, City.Bethel]
# Arizona
arizona_cities = [City.Phoenix, City.Tucson, City.Mesa, City.Chandler, City.Scottsdale,
                 City.Gilbert, City.Tempe, City.PeoriaArizona, City.Surprise, City.Yuma,
                 City.Goodyear, City.Flagstaff, City.LakeHavasuCity, City.Avondale, City.CasaGrande]
# Arkansas
arkansas_cities = [City.LittleRock, City.FortSmith, City.Fayetteville, City.Springdale, City.Jonesboro,
                  City.Conway, City.Rogers, City.PineBluff, City.Bentonville, City.HotSprings]
# California
california_cities = [City.LosAngeles, City.SanDiego, City.SanJose, City.SanFrancisco, City.Fresno,
                    City.Sacramento, City.LongBeach, City.Oakland, City.Bakersfield, City.Anaheim,
                    City.SantaAna, City.Riverside, City.Stockton, City.ChulaVista, City.Irvine,
                    City.Fremont, City.SanBernardino, City.Modesto, City.Fontana, City.Oxnard,
                    City.MorenoValley, City.HuntingtonBeach, City.Glendale, City.SantaClarita, City.GardenGrove,
                    City.Oceanside, City.RanchoCucamonga, City.SantaRosa, City.Ontario, City.ElkGrove,
                    City.Corona, City.Lancaster, City.Palmdale, City.Salinas, City.Hayward,
                    City.Pomona, City.Escondido, City.Sunnyvale, City.Torrance, City.Pasadena,
                    City.Orange, City.Fullerton, City.ThousandOaks, City.Visalia, City.SimiValley,
                    City.Concord, City.Roseville, City.Victorville, City.SantaClara, City.Vallejo,
                    City.Berkeley, City.ElMonte, City.Downey, City.CostaMesa, City.Inglewood,
                    City.Carlsbad, City.SanBuenaventura, City.Fairfield, City.WestCovina, City.Murrieta,
                    City.Richmond, City.Norwalk, City.Antioch, City.Temecula, City.Burbank,
                    City.DalyCity, City.Rialto, City.SantaMaria, City.ElCajon, City.SanMateo,
                    City.Clovis, City.Compton, City.JurupaValley, City.Vista, City.SouthGate,
                    City.MissionViejo, City.Vacaville, City.Carson, City.Hesperia, City.Redding,
                    City.SantaMonica, City.Westminster, City.SantaBarbara, City.Chico, City.Whittier,
                    City.NewportBeach, City.SanLeandro, City.Hawthorne, City.SanMarcos, City.CitrusHeights,
                    City.Alhambra, City.Tracy, City.Livermore, City.BuenaPark, City.Lakewood,
                    City.Merced, City.Hemet, City.Chino, City.Menifee, City.LakeForest,
                    City.Napa, City.RedwoodCity, City.Bellflower, City.Perris, City.Folsom,
                    City.Tustin, City.Lynwood, City.AppleValley, City.Manteca, City.BaldwinPark,
                    City.ChinoHills, City.Upland, City.MountainView, City.NapaValley, City.Camarillo,
                    City.Davis, City.YorbaLinda, City.WalnutCreek, City.Redlands, City.PaloAlto,
                    City.RedondoBeach]
# Colorado
colorado_cities = [City.Denver, City.ColoradoSprings, City.Aurora, City.FortCollins, City.LakewoodColorado,
                  City.Thornton, City.Arvada, City.WestminsterColorado, City.Centennial, City.Boulder]
# Connecticut
connecticut_cities = [City.Bridgeport, City.NewHaven, City.Stamford, City.Hartford, City.Waterbury,
                     City.NorwalkConnecticut, City.Danbury, City.NewBritain, City.Meriden, City.Bristol]
# Delaware
delaware_cities = [City.Wilmington, City.Dover, City.NewarkDelaware, City.Middletown, City.Smyrna]
# Florida
florida_cities = [City.Jacksonville, City.Miami, City.Tampa, City.Orlando, City.StPetersburg,
                 City.Hialeah, City.Tallahassee, City.FortLauderdale, City.PortStLucie, City.CapeCoral,
                 City.PembrokePines, City.HollywoodFL, City.Miramar, City.Gainesville, City.CoralSprings]
# Georgia
georgia_cities = [City.Atlanta, City.ColumbusGA, City.Augusta, City.Macon, City.Savannah,
                 City.Athens, City.SandySprings, City.RoswellGeorgia, City.JohnsCreek, City.WarnerRobins]
# Hawaii
hawaii_cities = [City.Honolulu, City.Hilo, City.Kailua, City.Kaneohe, City.Kahului,
                City.PearlCity, City.Waipahu, City.Mililani, City.Kihei, City.Lihue]
# Idaho
idaho_cities = [City.Boise, City.MeridianIdaho, City.Nampa, City.IdahoFalls, City.Pocatello,
               City.Caldwell, City.CoeurdAlene, City.TwinFalls, City.PostFalls, City.Rexburg]
# Illinois
illinois_cities = [City.Chicago, City.AuroraIL, City.Rockford, City.Joliet, City.Naperville,
                  City.SpringfieldIL, City.PeoriaIllinois, City.Elgin, City.Waukegan, City.Cicero,
                  City.Champaign]
# Indiana
indiana_cities = [City.Indianapolis, City.FortWayne, City.Evansville, City.SouthBend, City.Carmel,
                 City.Fishers, City.BloomingtonIndiana, City.Hammond, City.Gary, City.Lafayette]
# Iowa
iowa_cities = [City.DesMoines, City.CedarRapids, City.Davenport, City.SiouxCity, City.Waterloo,
              City.IowaCity, City.CouncilBluffs, City.Ames, City.Dubuque, City.Ankeny]
# Kansas
kansas_cities = [City.Wichita, City.OverlandPark, City.KansasCityKansas, City.Olathe, City.Topeka,
                City.Lawrence, City.Shawnee, City.Manhattan, City.Lenexa, City.Salina]
# Kentucky
kentucky_cities = [City.Louisville, City.Lexington, City.BowlingGreen, City.Owensboro, City.Covington,
                  City.Hopkinsville, City.RichmondKentucky, City.Florence, City.GeorgetownKentucky, City.Nicholasville]
# Louisiana
louisiana_cities = [City.NewOrleans, City.BatonRouge, City.Shreveport, City.LafayetteLouisiana, City.LakeCharles,
                   City.Kenner, City.BossierCity, City.MonroeLouisiana, City.AlexandriaLouisiana, City.Houma]
# Maine
maine_cities = [City.PortlandMaine, City.Lewiston, City.Bangor, City.SouthPortland, City.AuburnMaine,
               City.Biddeford, City.Sanford, City.Saco, City.AugustaMaine, City.Westbrook]
# Maryland
maryland_cities = [City.Baltimore, City.ColumbiaMaryland, City.Germantown, City.SilverSpring, City.Waldorf,
                  City.GlenBurnie, City.EllicottCity, City.Frederick, City.Rockville, City.Gaithersburg]
# Massachusetts
massachusetts_cities = [City.Boston, City.Worcester, City.SpringfieldMassachusetts, City.Cambridge, City.Lowell,
                       City.Brockton, City.Quincy, City.Lynn, City.NewBedford, City.FallRiver]
# Michigan
michigan_cities = [City.Detroit, City.GrandRapids, City.Warren, City.SterlingHeights, City.AnnArbor,
                  City.Lansing, City.Dearborn, City.Livonia, City.TroyMichigan, City.FarmingtonHills]
# Minnesota
minnesota_cities = [City.Minneapolis, City.SaintPaul, City.RochesterMN, City.Duluth, City.BloomingtonMinnesota,
                   City.BrooklynPark, City.Plymouth, City.Woodbury, City.MapleGrove, City.SaintCloud,
                   City.Eagan, City.EdenPrairie, City.CoonRapids, City.Burnsville, City.Blaine,
                   City.Lakeville, City.Minnetonka, City.AppleValleyMinnesota, City.StLouisPark, City.Moorhead]
# Mississippi
mississippi_cities = [City.JacksonMississippi, City.Gulfport, City.Southaven, City.Hattiesburg, City.Biloxi,
                     City.MeridianMississippi, City.Tupelo, City.GreenvilleMississippi, City.OliveBranch, City.HornLake]
# Missouri
missouri_cities = [City.KansasCityMissouri, City.StLouis, City.SpringfieldMissouri, City.ColumbiaMissouri, City.Independence,
                  City.LeeSummit, City.OFallon, City.StJoseph, City.StCharles, City.BlueSprings]
# Montana
montana_cities = [City.Billings, City.Missoula, City.GreatFalls, City.Bozeman, City.Butte,
                 City.HelenaMontana, City.Kalispell, City.Havre, City.Anaconda, City.MilesCity]
# Nebraska
nebraska_cities = [City.Omaha, City.LincolnNebraska, City.BellevueNebraska, City.GrandIsland, City.Kearney,
                  City.FremontNebraska, City.Hastings, City.NorfolkNebraska, City.NorthPlatte, City.Papillion]
# Nevada
nevada_cities = [City.LasVegas, City.Henderson, City.Reno, City.NorthLasVegas, City.Sparks,
                City.CarsonCityNevada, City.Fernley, City.Elko, City.BoulderCity, City.MesquiteNevada]
# New Hampshire
new_hampshire_cities = [City.ManchesterNewHampshire, City.Nashua, City.ConcordNewHampshire, City.Derry, City.RochesterNewHampshire,
                       City.SalemNewHampshire, City.DoverNewHampshire, City.Merrimack, City.Londonderry, City.HudsonNewHampshire]
# New Jersey
new_jersey_cities = [City.NewarkNewJersey, City.JerseyCity, City.Paterson, City.Elizabeth, City.Edison,
                    City.WoodbridgeTownship, City.LakewoodTownship, City.TomsRiver, City.HamiltonTownshipNewJersey, City.Trenton]
# New Mexico
new_mexico_cities = [City.Albuquerque, City.LasCruces, City.RioRancho, City.SantaFeNewMexico, City.RoswellNewMexico,
                    City.FarmingtonNewMexico, City.ClovisNewMexico, City.Hobbs, City.Alamogordo, City.CarlsbadNewMexico]
# New York
new_york_cities = [City.NewYorkCity, City.Buffalo, City.Rochester, City.Yonkers, City.Syracuse,
                  City.Albany, City.NewRochelle, City.MountVernon, City.Schenectady, City.Utica,
                  City.WhitePlains, City.Hempstead, City.Troy, City.NiagaraFalls, City.Binghamton,
                  City.Freeport, City.ValleyStream]
# North Carolina
north_carolina_cities = [City.Charlotte, City.Raleigh, City.Greensboro, City.Durham, City.WinstonSalem,
                        City.FayettevilleNorthCarolina, City.Cary, City.WilmingtonNorthCarolina, City.HighPoint, City.GreenvilleNorthCarolina]
# North Dakota
north_dakota_cities = [City.Fargo, City.Bismarck, City.GrandForks, City.Minot, City.WestFargo,
                      City.WillistonNorthDakota, City.Dickinson, City.Mandan, City.Jamestown, City.Wahpeton]
# Ohio
ohio_cities = [City.ColumbusOhio, City.Cleveland, City.Cincinnati, City.Toledo, City.Akron,
              City.Dayton, City.Parma, City.CantonOhio, City.Youngstown, City.Lorain]
# Oklahoma
oklahoma_cities = [City.OklahomaCity, City.Tulsa, City.Norman, City.BrokenArrow, City.Lawton,
                  City.Edmond, City.Moore, City.MidwestCity, City.Enid, City.Stillwater]
# Oregon (completed)
oregon_cities = [City.PortlandOregon, City.SalemOregon, City.Eugene, City.Gresham, City.Hillsboro,
                City.Beaverton, City.Bend, City.Medford, City.SpringfieldOregon, City.Corvallis]
# Pennsylvania
pennsylvania_cities = [City.Philadelphia, City.Pittsburgh, City.Allentown, City.Erie, City.Reading,
                      City.Scranton, City.Bethlehem, City.LancasterPennsylvania, City.Levittown, City.Harrisburg]
# Rhode Island
rhode_island_cities = [City.Providence, City.Cranston, City.Warwick, City.Pawtucket, City.EastProvidence,
                       City.Woonsocket, City.Cumberland, City.CoventryRhodeIsland, City.NorthProvidence, City.WestWarwick]
# South Carolina
south_carolina_cities = [City.ColumbiaSouthCarolina, City.Charleston, City.NorthCharleston, City.MountPleasant, City.RockHill,
                        City.GreenvilleSouthCarolina, City.Summerville, City.Sumter, City.GooseCreek, City.HiltonHeadIsland]
# South Dakota
south_dakota_cities = [City.SiouxFalls, City.RapidCity, City.Aberdeen, City.Watertown, City.Brookings,
                      City.Mitchell, City.Yankton, City.Pierre, City.Huron, City.Vermillion]
# Tennessee
tennessee_cities = [City.Nashville, City.Memphis, City.Knoxville, City.Chattanooga, City.Clarksville,
                   City.Murfreesboro, City.FranklinTennessee, City.JohnsonCity, City.JacksonTennessee, City.Hendersonville]
# Texas
texas_cities = [City.Houston, City.SanAntonio, City.Dallas, City.Austin, City.FortWorth,
               City.ElPaso, City.Arlington, City.CorpusChristi, City.Plano, City.Laredo,
               City.Lubbock, City.Garland, City.Irving, City.Amarillo, City.GrandPrairie,
               City.McKinney, City.Frisco, City.Brownsville, City.PasadenaTexas, City.Killeen,
               City.McAllen, City.Mesquite, City.Midland, City.Denton, City.Waco,
               City.Carrollton, City.RoundRock, City.Abilene, City.Odessa, City.Pearland,
               City.Richardson, City.SugarLand, City.Beaumont, City.CollegeStation, City.Lewisville,
               City.LeagueCity, City.Tyler, City.WichitaFalls, City.Allen, City.SanAngelo,
               City.Edinburg, City.Conroe, City.Bryan, City.Mission, City.NewBraunfels,
               City.Longview, City.Pharr, City.Baytown, City.FlowerMound, City.CedarPark,
               City.Temple, City.MissouriCity, City.Georgetown, City.NorthRichlandHills, City.Mansfield,
               City.Victoria, City.Harlingen, City.Rowlett, City.Pflugerville, City.Spring,
               City.Euless, City.DeSoto, City.Grapevine, City.Galveston, City.Bedford,
               City.CedarHill, City.TexasCity, City.HaltomCity, City.TheWoodlands]
# Utah
utah_cities = [City.SaltLakeCity, City.WestValleyCity, City.Provo, City.WestJordan, City.Orem,
              City.SandyUtah, City.Ogden, City.StGeorgeUtah, City.Layton, City.Taylorsville]
# Vermont
vermont_cities = [City.Burlington, City.Essex, City.SouthBurlington, City.Colchester, City.Rutland,
                 City.Bennington, City.Milton, City.Barre, City.WillistonVermont, City.HartfordVermont]
# Virginia
virginia_cities = [City.VirginiaBeach, City.Norfolk, City.Chesapeake, City.RichmondVirginia, City.NewportNews,
                  City.AlexandriaVirginia, City.Hampton, City.Roanoke, City.PortsmouthVirginia, City.Suffolk]
# Washington
washington_cities = [City.Seattle, City.Spokane, City.Tacoma, City.VancouverWashington, City.BellevueWashington,
                    City.Kent, City.Everett, City.Renton, City.FederalWay, City.SpokaneValley]
# West Virginia
west_virginia_cities = [City.CharlestonWestVirginia, City.Huntington, City.Parkersburg, City.Morgantown, City.Wheeling,
                       City.Beckley, City.Fairmont, City.Martinsburg, City.Clarksburg, City.Weirton]
# Wisconsin
wisconsin_cities = [City.Milwaukee, City.MadisonWisconsin, City.GreenBay, City.Kenosha, City.Racine,
                   City.Appleton, City.Waukesha, City.EauClaire, City.Oshkosh, City.Janesville]
# Wyoming
wyoming_cities = [City.Cheyenne, City.Casper, City.Laramie, City.Gillette, City.RockSprings,
                 City.Sheridan, City.Evanston, City.Riverton, City.Cody, City.JacksonWyoming]

exclude = ["__name__",
"__doc__",
"__package__",
"__loader__",
"__spec__",
"__annotations__",
"__builtins__",
"__file__",
"__cached__",
"Enum"]

if __name__ == '__main__':
    the_list = ['alabama_cities', 'alaska_cities', 'arizona_cities', 'arkansas_cities', 'california_cities',
                'colorado_cities', 'connecticut_cities', 'delaware_cities', 'florida_cities', 'georgia_cities',
                'hawaii_cities', 'idaho_cities', 'illinois_cities', 'indiana_cities', 'iowa_cities', 'kansas_cities',
                'kentucky_cities', 'louisiana_cities', 'maine_cities', 'maryland_cities', 'massachusetts_cities',
                'michigan_cities', 'minnesota_cities', 'mississippi_cities', 'missouri_cities', 'montana_cities',
                'nebraska_cities', 'nevada_cities', 'new_hampshire_cities', 'new_jersey_cities', 'new_mexico_cities',
                'new_york_cities', 'north_carolina_cities', 'north_dakota_cities', 'ohio_cities', 'oklahoma_cities',
                'oregon_cities', 'pennsylvania_cities', 'rhode_island_cities', 'south_carolina_cities',
                'south_dakota_cities', 'tennessee_cities', 'texas_cities', 'utah_cities', 'vermont_cities',
                'virginia_cities', 'washington_cities', 'west_virginia_cities', 'wisconsin_cities', 'wyoming_cities']
    all_cities = []
    for a_list in the_list:
        state_cities_list = globals()[a_list]
        for city in state_cities_list:
            all_cities.append(city)
    print(len(all_cities))

    all_vars = [name for name, value in globals().items() if str(name) not in exclude]
    filtered = []
    for item in all_vars:
        filtered.append(item)