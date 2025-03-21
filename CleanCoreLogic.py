import decimal, datetime, sys
from decimal import Decimal
from enum import Enum
from dateutil.relativedelta import relativedelta

from TaxiCal.LookUpInNestedDictionary import lookup_values_in_nested



class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    JPY = "JPY"
    GBP = "GBP"
    AUD = "AUD"
    CAD = "CAD"
    CHF = "CHF"
    CNY = "CNY"
    SEK = "SEK"
    NZD = "NZD"
    MXN = "MXN"
    SGD = "SGD"
    HKD = "HKD"
    NOK = "NOK"
    KRW = "KRW"
    TRY = "TRY"
    INR = "INR"
    BRL = "BRL"
    ZAR = "ZAR"
    RUB = "RUB"
class PaymentStatus(str, Enum):
    Paid = "Paid"
    UnPaid = "UnPaid"
    Capitalized = "Capitalized"
    NotSpecified = "NotSpecified"
    PartiallyPaid = "PartiallyPaid"
    InterestOnly = "InterestOnly"
class StandardFinancialUnit:
    def __init__(self, amount=Decimal("0"), currency=Currency.USD):
        if amount >= Decimal("0"):
            self.amount = Decimal(str(amount))
        else:
            raise ValueError("Standard Financial Unit cannot be negative.")
        currencies = {
            Currency.USD: {"Major": "dollar", "Minor": "cent"},
            Currency.EUR: {"Major": "euro", "Minor": "cent"},
            Currency.JPY: {"Major": "yen", "Minor": None},  # No minor unit
            Currency.GBP: {"Major": "pound", "Minor": "pence"},
            Currency.AUD: {"Major": "dollar", "Minor": "cent"},
            Currency.CAD: {"Major": "dollar", "Minor": "cent"},
            Currency.CHF: {"Major": "franc", "Minor": "rappen"},
            Currency.CNY: {"Major": "yuan", "Minor": "fen"},
            Currency.SEK: {"Major": "krona", "Minor": "öre"},
            Currency.NZD: {"Major": "dollar", "Minor": "cent"},
            Currency.MXN: {"Major": "peso", "Minor": "centavo"},
            Currency.SGD: {"Major": "dollar", "Minor": "cent"},
            Currency.HKD: {"Major": "dollar", "Minor": "cent"},
            Currency.NOK: {"Major": "krone", "Minor": "øre"},
            Currency.KRW: {"Major": "won", "Minor": None},  # No minor unit
            Currency.TRY: {"Major": "lira", "Minor": "kuruş"},
            Currency.INR: {"Major": "rupee", "Minor": "paisa"},
            Currency.BRL: {"Major": "real", "Minor": "centavo"},
            Currency.ZAR: {"Major": "rand", "Minor": "cent"},
            Currency.RUB: {"Major": "ruble", "Minor": "kopeck"},
        }
        if currency in currencies:
            self.currency = currency
        else:
            raise NotImplementedError()
    @property
    def major(self):
        if self.currency not in [Currency.JPY, Currency.KRW]:
            if self.amount != Decimal("Infinity"):
                x, _ = divmod(self.amount, Decimal("100"))
                return int(x)
            else:
                return sys.maxsize
        else:
            return int(self.amount)
    @property
    def minor(self):
        if self.currency not in [Currency.JPY, Currency.KRW]:
            if self.amount != Decimal("Infinity"):
                _, y = divmod(self.amount, Decimal("100"))
                return int(y)
            else:
                return 0
    @property
    def major_symbol(self):
        major_symbols = {
            Currency.USD: "$",
            Currency.EUR: "€",
            Currency.JPY: "¥",
            Currency.GBP: "£",
            Currency.AUD: "$",
            Currency.CAD: "$",
            Currency.CHF: "Fr",
            Currency.CNY: "¥",
            Currency.SEK: "kr",
            Currency.NZD: "$",
            Currency.MXN: "$",
            Currency.SGD: "$",
            Currency.HKD: "$",
            Currency.NOK: "kr",
            Currency.KRW: "₩",
            Currency.TRY: "₺",
            Currency.INR: "₹",
            Currency.BRL: "R$",
            Currency.ZAR: "R",
            Currency.RUB: "₽",
        }
        for currency, symbol in major_symbols.items():
            if self.currency == currency:
                return symbol
    @property
    def minor_symbol(self):
        minor_symbols = {
            Currency.USD: "¢",
            Currency.EUR: None,  # No unique minor symbol
            Currency.JPY: None,  # No minor unit
            Currency.GBP: "p",
            Currency.AUD: "¢",
            Currency.CAD: "¢",
            Currency.CHF: None,  # No unique minor symbol
            Currency.CNY: None,  # No well-known minor symbol
            Currency.SEK: None,  # No well-known minor symbol
            Currency.NZD: "¢",
            Currency.MXN: None,  # No well-known minor symbol
            Currency.SGD: "¢",
            Currency.HKD: "¢",
            Currency.NOK: None,  # No well-known minor symbol
            Currency.KRW: None,  # No minor unit
            Currency.TRY: None,  # No well-known minor symbol
            Currency.INR: None,  # No well-known minor symbol
            Currency.BRL: None,  # No well-known minor symbol
            Currency.ZAR: None,  # No well-known minor symbol
            Currency.RUB: None,  # No well-known minor symbol
        }
        for currency, symbol in minor_symbols.items():
            if self.currency == currency:
                return symbol
    def __str__(self):
        if self.minor is not None:
            if self.major > 0 or self.minor == 0:
                if type(self.major_symbol) is str:
                    if self.major_symbol.isalpha():
                        return f'''{self.major}.{self.minor:02} {self.major_symbol}'''
                    else:
                        return f'''{self.major_symbol}{self.major}.{self.minor:02}'''
                if self.major_symbol is None:
                    return f'''{self.major}.{self.minor:02} {self.currency}(s)'''
            else:
                if self.minor_symbol is not None:
                    return f'''{self.minor}{self.minor_symbol}'''
                else:
                    if type(self.major_symbol) is str:
                        if self.major_symbol.isalpha():
                            return f'''0.{self.minor:02} {self.major_symbol}'''
                        else:
                            return f'''{self.major_symbol}0.{self.minor:02}'''
                    if self.major_symbol is None:
                        return f'''0.{self.minor:02} {self.currency}(s)'''
        else:
            return f'''{self.major_symbol}{self.major}'''
    def __gt__(self, other):
        if isinstance(other, StandardFinancialUnit):
            if other.currency == self.currency:
                if self.amount > other.amount:
                    return True
                else:
                    return False
            else:
                return NotImplemented
    def __lt__(self, other):
        if isinstance(other, StandardFinancialUnit):
            if other.currency == self.currency:
                if self.amount < other.amount:
                    return True
                else:
                    return False
            else:
                return NotImplemented
    def __ge__(self, other):
        if isinstance(other, StandardFinancialUnit):
            if other.currency == self.currency:
                if self.amount >= other.amount:
                    return True
                else:
                    return False
            else:
                return NotImplemented
    def __le__(self, other):
        if isinstance(other, StandardFinancialUnit):
            if other.currency == self.currency:
                if self.amount <= other.amount:
                    return True
                else:
                    return False
            else:
                return NotImplemented
    def __eq__(self, other):
        if isinstance(other, StandardFinancialUnit):
            if other.currency == self.currency:
                if self.amount == other.amount:
                    return True
                else:
                    return False
            else:
                return NotImplemented
    def __ne__(self, other):
        if isinstance(other, StandardFinancialUnit):
            if other.currency == self.currency:
                if self.amount != other.amount:
                    return True
                else:
                    return False
            else:
                return NotImplemented
    def __add__(self, other):
        if isinstance(other, StandardFinancialUnit):
            if other.currency == self.currency:
                return self.__class__((self.amount + other.amount), self.currency)
            else:
                return NotImplemented
    def __sub__(self, other):
        if isinstance(other, StandardFinancialUnit):
            if other.currency == self.currency:
                if self >= other:
                    return self.__class__((self.amount - other.amount), self.currency)
                else:
                    raise ValueError("The subtrahend is greater than the minuend.")
            else:
                return NotImplemented
    def __truediv__(self, other):
        if not isinstance(other, StandardFinancialUnit):
            if other > 0:
                return self.__class__(self.amount / Decimal(str(other)), self.currency)
            elif other == 0:
                raise ZeroDivisionError
            else:
                raise ValueError("Standard Financial Unit cannot be negative.")

    def __mul__(self, other):
        if not isinstance(other, StandardFinancialUnit):
            if other >= 0:
                return self.__class__(self.amount * Decimal(str(other)), self.currency)
            else:
                raise ValueError("Standard Financial Unit cannot be negative.")
    def __iadd__(self, other):
        if isinstance(other, StandardFinancialUnit):
            if other.currency == self.currency:
                self.amount += other.amount
                return self
            else:
                return NotImplemented
    def __isub__(self, other):
        if isinstance(other, StandardFinancialUnit):
            if other.currency == self.currency:
                if self.amount >= other.amount:
                    self.amount -= other.amount
                    return self
                else:
                    raise ValueError("The subtrahend is greater than the minuend.")
            else:
                return NotImplemented
    def __imul__(self, other):
        if not isinstance(other, StandardFinancialUnit):
            if Decimal(str(other)) >= 0:
                self.amount *= Decimal(str(other))
                return self
            else:
                raise ValueError("Standard Financial Unit cannot be negative.")
    def __itruediv__(self, other):
        if not isinstance(other, StandardFinancialUnit):
            if Decimal(str(other)) > 0:
                self.amount /= Decimal(str(other))
                return self
            elif Decimal(str(other)) == 0:
                raise ZeroDivisionError
            else:
                raise ValueError("Standard Financial Unit cannot be negative.")
class Money(StandardFinancialUnit):
    def pay(self, to_be_paid):
        if isinstance(to_be_paid, Liability):
            if to_be_paid.status != PaymentStatus.Paid:
                if self >= to_be_paid:
                    self.amount -= to_be_paid.amount
                    to_be_paid.paid()
                else:
                    raise ValueError("Liability is greater than fund.")
    def __repr__(self):
        return f"Money(Decimal('{self.amount}'))"
class Liability(StandardFinancialUnit):
    def __init__(self, amount=Decimal("0"), currency=Currency.USD, payment_status=PaymentStatus.UnPaid):
        super().__init__(amount, currency)
        self.status = payment_status
    def paid(self):
        self.amount = Decimal("0")
        self.status = PaymentStatus.Paid
class Tax(Liability):
    pass
class MaritalStatus(str, Enum):
    Single = "Single"
    MarriedNonJoint = "MarriedNonJoint"
    MarriedJoint = "MarriedJoint"
    UnSpecified = "UnSpecified"
class State(str, Enum):
    CityVariablesIndex = "CityVariablesHeader"
    UnSpecifiedState = "UnSpecifiedState"
    Alabama = "Alabama"
    Alaska = "Alaska"
    Arizona = "Arizona"
    Arkansas = "Arkansas"
    California = "California"
    Colorado = "Colorado"
    Connecticut = "Connecticut"
    Delaware = "Delaware"
    Florida = "Florida"
    Georgia = "Georgia"
    Hawaii = "Hawaii"
    Idaho = "Idaho"
    Illinois = "Illinois"
    Indiana = "Indiana"
    Iowa = "Iowa"
    Kansas = "Kansas"
    Kentucky = "Kentucky"
    Louisiana = "Louisiana"
    Maine = "Maine"
    Maryland = "Maryland"
    Massachusetts = "Massachusetts"
    Michigan = "Michigan"
    Minnesota = "Minnesota"
    Mississippi = "Mississippi"
    Missouri = "Missouri"
    Montana = "Montana"
    Nebraska = "Nebraska"
    Nevada = "Nevada"
    NewHampshire = "NewHampshire"
    NewJersey = "NewJersey"
    NewMexico = "NewMexico"
    NewYork = "NewYork"
    NorthCarolina = "NorthCarolina"
    NorthDakota = "NorthDakota"
    Ohio = "Ohio"
    Oklahoma = "Oklahoma"
    Oregon = "Oregon"
    Pennsylvania = "Pennsylvania"
    RhodeIsland = "RhodeIsland"
    SouthCarolina = "SouthCarolina"
    SouthDakota = "SouthDakota"
    Tennessee = "Tennessee"
    Texas = "Texas"
    Utah = "Utah"
    Vermont = "Vermont"
    Virginia = "Virginia"
    Washington = "Washington"
    WestVirginia = "WestVirginia"
    Wisconsin = "Wisconsin"
    Wyoming = "Wyoming"
def str_to_object(string, enums_list:list):
    if isinstance(string, str):
        if "MoneyInCents " in string:
            stripped_string = string.replace("MoneyInCents ", "")
            try:
                return Money(Decimal(stripped_string))
            except decimal.InvalidOperation:
                pass
            except  ValueError:
                return "Negative Money crab."
        elif "Decimal " in string:
            stripped_string = string.replace("Decimal ", "")
            try:
                return Decimal(stripped_string)
            except decimal.InvalidOperation:
                pass
        elif "ThisIsADateTimeObject" in string:
            the_iso_format = string.replace("ThisIsADateTimeObject", "")
            return datetime.datetime.fromisoformat(the_iso_format)
        elif string.isdigit():
            return int(string)
        for an_enum in enums_list:
            try:
                return an_enum[string]
            except KeyError:
                pass
        return string
def dict_to_object(dictionary, enums_list):
    if dictionary.get("ThisKeyIsReservedForTypesOnly") == "relativedelta":
        dictionary.pop("ThisKeyIsReservedForTypesOnly")
        valid_keys = {
            "years", "months", "days", "hours", "minutes", "seconds", "microseconds",
            "leapdays", "weeks", "year", "month", "day", "hour", "minute", "second",
            "microsecond", "yearday", "weekday", "nth"
        }
        filtered_data = {key: its_value for key, its_value in dictionary.items() if key in valid_keys}
        try:
            return relativedelta(**filtered_data)
        except TypeError:
            return dictionary
    if isinstance(dictionary, dict):
        keys_list = list(dictionary.keys())
        for key in keys_list:
            dictionary[str_to_object(key, enums_list)] = dictionary.pop(key)
        for key, value in dictionary.items():
            if isinstance(value, str):
                dictionary[key] = str_to_object(value, enums_list)
            elif isinstance(value, dict):
                dictionary[key] = dict_to_object(value, enums_list)
    return dictionary
def list_to_object(a_list, enums_list):
    if isinstance(a_list, list):
        for i in range(len(a_list)):
            if isinstance(a_list[i], str):
                a_list[i] = str_to_object(a_list[i], enums_list)
            elif isinstance(a_list[i], dict):
                a_list[i] = dict_to_object(a_list[i], enums_list)
            elif isinstance(a_list[i], list):
                a_list[i] = list_to_object(a_list[i], enums_list)
        return a_list
def restore_objects(something, enums_list):
    if isinstance(something, str):
        return str_to_object(something, enums_list)
    elif isinstance(something, dict):
        return dict_to_object(something, enums_list)
    elif isinstance(something, list):
        return list_to_object(something, enums_list)
def smart_serializer(obj):
    if isinstance(obj, Decimal):
        return f"Decimal {obj}"
    elif isinstance(obj, Money):
        return f"MoneyInCents {obj.amount}"
    elif isinstance(obj, relativedelta):
        relativedelta_data = obj.__dict__.copy()
        relativedelta_data["ThisKeyIsReservedForTypesOnly"] = "relativedelta"
        return relativedelta_data
    elif isinstance(obj, datetime.datetime):
        the_iso_format = obj.isoformat()
        return f'''ThisIsADateTimeObject{the_iso_format}'''
    else:
        raise TypeError(f"Not serializable, bro, type is {type(obj)}")
class Variables(str, Enum):
    Configurations = "Configurations"
    Taxes = "Data"
    TaxBenefits = "TaxBenefits"
class Configurations(str, Enum):
    VariablesType = "VariablesType"
    TaxNameType = "TaxNameType"
    TaxName = "TaxName"
    TaxationType = "TaxationType"
    TaxBase = "TaxBase"
    VerifierConfigurations = "VerifierConfigurations"
    AdjustedIncomeSource = "AdjustedIncomeSource"
    LastUpdated = "LastUpdated"
class VariablesType(str, Enum):
    FederalVariables = "FederalVariables"
    StateVariables = "StateVariables"
    CityVariables = "CityVariables"
    LocalVariables = "LocalVariables"
    CustomVariables = "CustomVariables"
class TaxBase(str,Enum):
    CustomBase = "CustomBase"
class TaxationType(str, Enum):
    Progressive = "Progressive"
    Flat = "Flat"
    FixedAmount = "FixedAmount"
class TaxVariables(str, Enum):
    Configurations = "Configurations"
    BracketCeilings = "BracketCeilings"
    Rates = "Rates"
    OtherTaxes = "OtherTaxes"
    TaxBenefits = "TaxBenefits"
class TaxNameType(str, Enum):
    StandardName = "StandardName"
    CustomName = "CustomName"
class TaxBenefits(str, Enum):
    Deduction = "Deduction"
    Exemption = "Exemption"
    Credit = "Credit"
    Deferral = "Deferral"
class Deduction(str, Enum):
    Itemization = "Itemization"
    StandardDeduction = "StandardDeduction"
    ItemizedDeduction = "ItemizedDeduction"
class VerifierConfigurations(str, Enum):
    RequiredVerifierVersion = "RequiredVerifierVersion"
    SupportsForwardCompatibility = "SupportsForwardCompatibility"
    SupportsBackwardCompatibility = "SupportsBackwardCompatibility"
class AdjustedIncomeSource(str, Enum):
    FromState = "FromState"
    FromFederal = "FromFederal"
    FromCity = "FromCity"
    FromLocal = "FromLocal"
    FromTaxSpecificTaxBenefits = "FromTaxSpecificTaxBenefits"
class Itemization(str, Enum):
    MortgageInterest = "MortgageInterest"
    PropertyTaxItemization = "PropertyTaxItemization"
    MedicalAndDentalExpenses = "MedicalAndDentalExpenses"
    SALT = "SALT"
    PublicCashDonations = "PublicCashDonations"
    PrivateCashDonations = "PrivateCashDonations"
    PublicNonCashDonations = "PublicNonCashDonations"
    PublicCapitalGainsDonations = "PublicCapitalGainsDonations"
    PrivateCapitalGainsDonations = "PrivateCapitalGainsDonations"
    InvestmentInterestExpense = "InvestmentInterestExpense"
    CasualtyAndTheftLoses = "CasualtyAndTheftLoses"
    UnReimbursedEmployeeExpense = "UnReimbursedEmployeeExpense"
    TaxPreparationFees = "TaxPreparationFees"
    TotalDonations = "TotalDonations"
class ItemItemization(str, Enum):
    DeductibleValue = "DeductibleValue"
    Note = "Note"
    CarryForwardTimeLimit = "CarryForwardTimeLimit"
    LimitType = "LimitType"
    CapsAppliedCount = "CapsAppliedCount"
    ItemizationCaps = "ItemizationCaps"
    ItemizationCap = "ItemizationCap"
    ItemizationCapType = "ItemizationCapType"
    ItemItemizationType = "ItemItemizationType"
    ReceiverCode = "ReceiverCode"
    ReceivingCode = "ReceivingCode"
    HaveBaseAGIDependentFeeders = "HaveBaseAGIDependentFeeders"
class ItemItemizationType(str, Enum):
    Direct = "Direct"
    Feeder = "Feeder"
    Receiver = "Receiver"
class ItemizationCapType(str, Enum):
    FixedCap = "FixedCap"
    DynamicCap = "DynamicCap"
class ItemizationPhase(str, Enum):
    FirstPhase = "FirstPhase"
    SecondPhase = "SecondPhase"
    ThirdPhase = "ThirdPhase"
    PreBaseAGIA1 = "PreBaseAGIA1"
    PreBaseAGIA2 = "PreBaseAGIA2"
    PreBaseAGIA3 = "PreBaseAGIA3"
    PreBaseAGIB = "PreBaseAGIB"
    PostBaseAGIA1 = "PostBaseAGIA1"
    PostBaseAGIA2 = "PostBaseAGIA2"
    PostBaseAGIA3 = "PostBaseAGIA3"
    PostBaseAGIB = "PostBaseAGIB"
class Values(str, Enum):
    DynamicValue = "DynamicValue"
    FixedValue = "FixedValue"
    SmartValueA = "SmartValueA"
    SmartValueB = "SmartValueB"
    InterValuesOperation = "InterValuesOperation"
class VPerson(str, Enum):
    VGrossIncome = "VGrossIncome"
    VTotalInvestmentInterestExpense = "VTotalInvestmentInterestExpense"
    VTotalDebtBasedInvestmentEarnings = "VTotalDebtBasedInvestmentEarnings"
    VAdjustedIncome = "VAdjustedIncome"
    VPropertyValue = "VPropertyValue"
    VWealth = "VWealth"
    VCapitalGain = "VCapitalGain"
    VCustomBase = "VCustomBase"
    VTotalItemized = "VTotalItemized"
    VTotalInvestmentExpense = "VTotalInvestmentExpense"
    VMedicalExpenses = "VMedicalExpenses"
    VCharitableContributions = "VCharitableContributions"
    VMortgageInterest = "VMortgageInterest"
    VPropertyTaxes = "VPropertyTaxes"
    VStudentLoanInterest = "VStudentLoanInterest"
    VJobExpenses = "VJobExpenses"
    VEducationExpenses = "VEducationExpenses"
    VRetirementContributions = "VRetirementContributions"
    VChildcareExpenses = "VChildcareExpenses"
    VHealthInsurancePremiums = "VHealthInsurancePremiums"
    VBusinessExpenses = "VBusinessExpenses"
    VRentalExpenses = "VRentalExpenses"
    VAlimonyPaid = "VAlimonyPaid"
    VGamblingLosses = "VGamblingLosses"
    VMovingExpenses = "VMovingExpenses"
    VPublicCashDonations = "VPublicCashDonations"
    VPrivateCashDonations = "VPrivateCashDonations"
    VPublicNonCashDonations = "VPublicNonCashDonations"
    VPublicCapitalGainsDonations = "VPublicCapitalGainsDonations"
    VPrivateCapitalGainsDonations = "VPrivateCapitalGainsDonations"
    VInvestmentInterestExpense = "VInvestmentInterestExpense"
    VSALT = "VSALT"

    VCurrentBaseAGI = "VCurrentBaseAGI"
    VCurrentFinalAGI = "VCurrentFinalAGI"

    VFederalBaseAGI = "VFederalBaseAGI"
    VFederalFinalAGI = "VFederalFinalAGI"

    VStateBaseAGI = "VStateBaseAGI"
    VStateFinalAGI = "VStateFinalAGI"

    VCityBaseAGI = "VCityBaseAGI"
    VCityFinalAGI = "VCityFinalAGI"

    VLocalBaseAGI = "VLocalBaseAGI"
    VLocalFinalAGI = "VLocalFinalAGI"
class InterValuesOperation(str, Enum):
    Addition = "Addition"
    Subtraction = "Subtraction"
    Multiplication = "Multiplication"
    Division = "Division"
    FloorSubtraction = "FloorSubtraction"
class LimitType(str, Enum):
    UpperLimit = "UpperLimit"
    LowerLimit = "LowerLimit"
class StandardTaxName(str, Enum):
    # Income Taxes
    FederalIncomeTax = "FederalIncomeTax"
    StateIncomeTax = "StateIncomeTax"
    LocalIncomeTax = "LocalIncomeTax"

    # Payroll Taxes
    SocialSecurityTax = "SocialSecurityTax"
    MedicareTax = "MedicareTax"
    AdditionalMedicareTax = "AdditionalMedicareTax"
    FederalUnemploymentTax = "FederalUnemploymentTax"
    StateUnemploymentTax = "StateUnemploymentTax"

    # Corporate Taxes
    CorporateIncomeTax = "CorporateIncomeTax"
    GrossReceiptsTax = "GrossReceiptsTax"

    # Sales & Consumption Taxes
    SalesTax = "SalesTax"
    UseTax = "UseTax"
    ValueAddedTax = "ValueAddedTax"
    ExciseTax = "ExciseTax"

    # Property & Wealth Taxes
    RealEstatePropertyTax = "RealEstatePropertyTax"
    PersonalPropertyTax = "PersonalPropertyTax"
    EstateTax = "EstateTax"
    InheritanceTax = "InheritanceTax"
    GiftTax = "GiftTax"

    # Capital & Investment Taxes
    CapitalGainsTax = "CapitalGainsTax"
    DividendTax = "DividendTax"
    NetInvestmentIncomeTax = "NetInvestmentIncomeTax"

    # Other Taxes
    SinTax = "SinTax"
    CarbonTax = "CarbonTax"
    LuxuryTax = "LuxuryTax"
    ImportDuty = "ImportDuty"
class LocalIndex(str, Enum):
    FederalVariablesIndex = "FederalVariablesIndex"
    StatesVariablesIndex = "StatesVariablesIndex"
    CitiesVariablesIndex = "CitiesVariablesIndex"
    MunicipalitiesVariablesIndex = "MunicipalitiesVariablesIndex"
class AGIType(str, Enum):
    FederalAGI = "FederalAGI"
    StateAGI = "StateAGI"
    CityAGI = "CityAGI"
    CustomAGI = "CustomAGI"
all_enums = [Currency,
             PaymentStatus,
             MaritalStatus,
             State,
             Variables,
             Configurations,
             TaxationType,
             TaxVariables, TaxBenefits,
             Deduction,
             VerifierConfigurations,
             AdjustedIncomeSource,
             Itemization,
             ItemItemization,
             ItemizationCapType,
             Values,
             VPerson,
             InterValuesOperation,
             LimitType,
             TaxNameType,
             StandardTaxName,
             ]

standard_variables = {
    Variables.Configurations: {
        Configurations.VerifierConfigurations: {
            VerifierConfigurations.RequiredVerifierVersion: 1,
            VerifierConfigurations.SupportsForwardCompatibility: True,
            VerifierConfigurations.SupportsBackwardCompatibility: False,
        },
        Configurations.VariablesType: VariablesType.FederalVariables,
        Configurations.LastUpdated: datetime.datetime(2025,3,18)
    },
    Variables.Taxes: {
        1: {
            TaxVariables.Configurations: {
                Configurations.TaxNameType: TaxNameType.StandardName,
                Configurations.TaxName: StandardTaxName.FederalIncomeTax,
                Configurations.TaxationType: TaxationType.Progressive,
                Configurations.TaxBase: VPerson.VFederalFinalAGI,
                Configurations.AdjustedIncomeSource: None,
            },
            TaxVariables.BracketCeilings: {
                MaritalStatus.Single: {
                    1: Money(Decimal("1192500")),
                    2: Money(Decimal("4847500")),
                    3: Money(Decimal("10335000")),
                    4: Money(Decimal("19730000")),
                    5: Money(Decimal("25052500")),
                    6: Money(Decimal("62635000")),
                    7: Money(Decimal("Infinity")),
                },
                MaritalStatus.MarriedJoint: {
                    1: Money(Decimal("2385000")),
                    2: Money(Decimal("9695000")),
                    3: Money(Decimal("20670000")),
                    4: Money(Decimal("39460000")),
                    5: Money(Decimal("50105000")),
                    6: Money(Decimal("75160000")),
                    7: Money(Decimal("Infinity")),
                },
                MaritalStatus.MarriedNonJoint: {  # Copy of Single
                    1: Money(Decimal("1192500")),
                    2: Money(Decimal("4847500")),
                    3: Money(Decimal("10335000")),
                    4: Money(Decimal("19730000")),
                    5: Money(Decimal("25052500")),
                    6: Money(Decimal("62635000")),
                    7: Money(Decimal("Infinity")),
                },
            },
            TaxVariables.Rates: {
                1: Decimal("0.10"),
                2: Decimal("0.12"),
                3: Decimal("0.22"),
                4: Decimal("0.24"),
                5: Decimal("0.32"),
                6: Decimal("0.35"),
                7: Decimal("0.37"),
            },
        },
    },
    Variables.TaxBenefits: {
        TaxBenefits.Deduction:{
            Deduction.StandardDeduction: {
                MaritalStatus.Single: Money(Decimal("1500000")),
                MaritalStatus.MarriedJoint: Money(Decimal("3000000")),
                MaritalStatus.MarriedNonJoint: Money(Decimal("1500000")),
            },
            Deduction.Itemization:{
                Itemization.MortgageInterest: {
                    ItemItemization.ItemItemizationType: ItemItemizationType.Direct,
                    ItemItemization.DeductibleValue: VPerson.VMortgageInterest,
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.ItemizationCaps:{
                        1: {
                        ItemItemization.LimitType: LimitType.UpperLimit,
                        ItemItemization.ItemizationCapType: ItemizationCapType.FixedCap,
                        Values.FixedValue: Money(Decimal("75000000")),
                        },
                    },
                    ItemItemization.Note: "Mortgages taken before 2018 have a cap of 1M, while after 2018 is capped at 750k.",
                },
                Itemization.MedicalAndDentalExpenses: {
                    ItemItemization.DeductibleValue: VPerson.VMedicalExpenses,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Direct,
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.ItemizationCaps:{
                        1:{
                            ItemItemization.LimitType: LimitType.LowerLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.SmartValueA: VPerson.VFederalBaseAGI,
                            Values.SmartValueB: Decimal("0.075"),
                            Values.InterValuesOperation: InterValuesOperation.Multiplication,
                            },
                        },
                    },
                Itemization.PropertyTaxItemization: {
                    ItemItemization.DeductibleValue: VPerson.VPropertyTaxes,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Feeder,
                    ItemItemization.ReceiverCode: "SALT",
                    ItemItemization.CapsAppliedCount: 0
                },
                Itemization.SALT: {
                    # ItemItemization.DeductibleValue: VPerson.VSALT,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Receiver,
                    ItemItemization.HaveBaseAGIDependentFeeders: False,
                    ItemItemization.ReceivingCode: "SALT",
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.UpperLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.FixedCap,
                            Values.FixedValue: Money(Decimal("1000000")),
                        },
                    },
                },
                Itemization.PublicCashDonations: {
                    ItemItemization.DeductibleValue: VPerson.VPublicCashDonations,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Feeder,
                    ItemItemization.ReceiverCode: "Donations",
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.CarryForwardTimeLimit: relativedelta(years=5),
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.UpperLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.SmartValueA: VPerson.VFederalBaseAGI,
                            Values.SmartValueB: Decimal("0.6"),
                            Values.InterValuesOperation: InterValuesOperation.Multiplication,
                        },
                    },
                },
                Itemization.PrivateCashDonations: {
                    ItemItemization.DeductibleValue: VPerson.VPrivateCashDonations,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Feeder,
                    ItemItemization.ReceiverCode: "Donations",
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.CarryForwardTimeLimit: relativedelta(years=5),
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.UpperLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.SmartValueA: VPerson.VFederalBaseAGI,
                            Values.SmartValueB: Decimal("0.3"),
                            Values.InterValuesOperation: InterValuesOperation.Multiplication,
                        },
                    },
                },
                Itemization.PublicNonCashDonations: {
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.DeductibleValue: VPerson.VPublicNonCashDonations,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Feeder,
                    ItemItemization.ReceiverCode: "Donations",
                    ItemItemization.CarryForwardTimeLimit: relativedelta(years=5),
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.UpperLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.SmartValueA: VPerson.VFederalBaseAGI,
                            Values.SmartValueB: Decimal("0.3"),
                            Values.InterValuesOperation: InterValuesOperation.Multiplication,
                        },
                    },
                    ItemItemization.Note: "Donation must be public, otherwise, it does not apply."
                },
                Itemization.PublicCapitalGainsDonations: {
                    ItemItemization.DeductibleValue: VPerson.VPublicCapitalGainsDonations,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Feeder,
                    ItemItemization.ReceiverCode: "Donations",
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.CarryForwardTimeLimit: relativedelta(years=5),
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.UpperLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.SmartValueA: VPerson.VFederalBaseAGI,
                            Values.SmartValueB: Decimal("0.3"),
                            Values.InterValuesOperation: InterValuesOperation.Multiplication,
                        },
                    },
                },
                Itemization.PrivateCapitalGainsDonations: {
                    ItemItemization.DeductibleValue: VPerson.VPrivateCapitalGainsDonations,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Feeder,
                    ItemItemization.ReceiverCode: "Donations",
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.CarryForwardTimeLimit: relativedelta(years=5),
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.UpperLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.SmartValueA: VPerson.VFederalBaseAGI,
                            Values.SmartValueB: Decimal("0.2"),
                            Values.InterValuesOperation: InterValuesOperation.Multiplication,
                        },
                    },
                },
                Itemization.InvestmentInterestExpense: {
                    ItemItemization.DeductibleValue: VPerson.VInvestmentInterestExpense,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Direct,
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.CarryForwardTimeLimit: datetime.datetime.max,
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.UpperLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.DynamicValue: VPerson.VTotalDebtBasedInvestmentEarnings,
                        },
                    },
                },
                Itemization.TotalDonations: {
                    # ItemItemization.DeductibleValue: VPerson.VInvestmentInterestExpense,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Receiver,
                    ItemItemization.ReceivingCode: "Donations",
                    ItemItemization.HaveBaseAGIDependentFeeders: True,
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.CarryForwardTimeLimit: relativedelta(years=5),
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.UpperLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.SmartValueA: VPerson.VFederalBaseAGI,
                            Values.SmartValueB: Decimal("0.6"),
                            Values.InterValuesOperation: InterValuesOperation.Multiplication,
                        },
                    },
                },
            },
        },
        TaxBenefits.Exemption:{
            MaritalStatus.Single: Money(),
            MaritalStatus.MarriedJoint: Money(),
            MaritalStatus.MarriedNonJoint: Money(),
        },
    },
}
california_variables = {
    Variables.Configurations: {
        Configurations.VerifierConfigurations: {
            VerifierConfigurations.RequiredVerifierVersion: 1,
            VerifierConfigurations.SupportsForwardCompatibility: True,
            VerifierConfigurations.SupportsBackwardCompatibility: False,
        },
        Configurations.VariablesType: VariablesType.StateVariables,
        Configurations.LastUpdated: datetime.datetime(2025, 3, 18)
    },
    Variables.Taxes: {
        1: {
            TaxVariables.Configurations: {
                Configurations.TaxNameType: TaxNameType.StandardName,
                Configurations.TaxName: StandardTaxName.StateIncomeTax,
                Configurations.TaxationType: TaxationType.Progressive,
                Configurations.TaxBase: VPerson.VStateFinalAGI,
                Configurations.AdjustedIncomeSource: AdjustedIncomeSource.FromState,
            },
            TaxVariables.BracketCeilings: {
                MaritalStatus.Single: {
                    1: Money(Decimal("932500")),
                    2: Money(Decimal("2210700")),
                    3: Money(Decimal("3489200")),
                    4: Money(Decimal("4843500")),
                    5: Money(Decimal("6121400")),
                    6: Money(Decimal("31268600")),
                    7: Money(Decimal("37522100")),
                    8: Money(Decimal("62536900")),
                    9: Money(Decimal("Infinity")),
                },
                MaritalStatus.MarriedJoint: {
                    1: Money(Decimal("1865000")),
                    2: Money(Decimal("4421400")),
                    3: Money(Decimal("6978400")),
                    4: Money(Decimal("9687000")),
                    5: Money(Decimal("12242800")),
                    6: Money(Decimal("62537200")),
                    7: Money(Decimal("75044200")),
                    8: Money(Decimal("125073800")),
                    9: Money(Decimal("Infinity")),
                },
                MaritalStatus.MarriedNonJoint: {  # Copy of Single
                    1: Money(Decimal("932500")),
                    2: Money(Decimal("2210700")),
                    3: Money(Decimal("3489200")),
                    4: Money(Decimal("4843500")),
                    5: Money(Decimal("6121400")),
                    6: Money(Decimal("31268600")),
                    7: Money(Decimal("37522100")),
                    8: Money(Decimal("62536900")),
                    9: Money(Decimal("Infinity")),
                },
            },
            TaxVariables.Rates: {
                1: Decimal("0.01"),
                2: Decimal("0.02"),
                3: Decimal("0.04"),
                4: Decimal("0.06"),
                5: Decimal("0.08"),
                6: Decimal("0.093"),
                7: Decimal("0.103"),
                8: Decimal("0.113"),
                9: Decimal("0.123"),
            },
        },
    },
    Variables.TaxBenefits: {
        TaxBenefits.Deduction: {
            Deduction.StandardDeduction: {
                MaritalStatus.Single: Money(Decimal("554000")),
                MaritalStatus.MarriedJoint: Money(Decimal("1108000")),
                MaritalStatus.MarriedNonJoint: Money(Decimal("554000")),
            },
            Deduction.Itemization: {
                Itemization.MortgageInterest: {
                    ItemItemization.ItemItemizationType: ItemItemizationType.Direct,
                    ItemItemization.DeductibleValue: VPerson.VMortgageInterest,
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.UpperLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.FixedCap,
                            Values.FixedValue: Money(Decimal("100000000")),
                        },
                    },
                    ItemItemization.Note: "California allows mortgage interest deduction up to $1M, unlike federal's $750k cap.",
                },
                Itemization.MedicalAndDentalExpenses: {
                    ItemItemization.DeductibleValue: VPerson.VMedicalExpenses,
                    ItemItemization.ItemItemizationType: ItemItemizationType.Direct,
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.LowerLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.SmartValueA: VPerson.VStateBaseAGI,
                            Values.SmartValueB: Decimal("0.075"),
                            Values.InterValuesOperation: InterValuesOperation.Multiplication,
                        },
                    },
                },
            },
        },
        TaxBenefits.Exemption: {
            MaritalStatus.Single: Money(Decimal("12900")),
            MaritalStatus.MarriedJoint: Money(Decimal("25800")),
            MaritalStatus.MarriedNonJoint: Money(Decimal("12900")),
        },
    },
}


default_variables_index = {
    LocalIndex.FederalVariablesIndex: standard_variables,
    LocalIndex.StatesVariablesIndex: {
        State.California: california_variables
    },
    LocalIndex.CitiesVariablesIndex: {},
    LocalIndex.MunicipalitiesVariablesIndex: {},
}
vperson_to_person_attributes = {
    VPerson.VFederalFinalAGI: {
        "attribute name": "federal_final_agi",
        "default value": Money()
    },
    VPerson.VFederalBaseAGI:{
        "attribute name": "federal_base_agi",
        "default value": Money()
    },
    VPerson.VTotalItemized: {
        "attribute name": "total_itemized",
        "default value": Money()
    },
    VPerson.VTotalInvestmentExpense: {
        "attribute name": "total_investment_expense",
        "default value": Liability()
    },
    VPerson.VMedicalExpenses: {
        "attribute name": "medical_expenses",
        "default value": Liability()
    },
    VPerson.VCharitableContributions: {
        "attribute name": "charitable_contributions",
        "default value": Money()
    },
    VPerson.VMortgageInterest: {
        "attribute name": "mortgage_interest",
        "default value": Liability()
    },
    VPerson.VPropertyTaxes: {
        "attribute name": "property_taxes",
        "default value": Tax()
    },
    VPerson.VStudentLoanInterest: {
        "attribute name": "student_loan_interest",
        "default value": Liability()
    },
    VPerson.VJobExpenses: {
        "attribute name": "job_expenses",
        "default value": Liability()
    },
    VPerson.VEducationExpenses: {
        "attribute name": "education_expenses",
        "default value": Liability()
    },
    VPerson.VRetirementContributions: {
        "attribute name": "retirement_contributions",
        "default value": Money()
    },
    VPerson.VChildcareExpenses: {
        "attribute name": "childcare_expenses",
        "default value": Liability()
    },
    VPerson.VHealthInsurancePremiums: {
        "attribute name": "health_insurance_premiums",
        "default value": Money()
    },
    VPerson.VBusinessExpenses: {
        "attribute name": "business_expenses",
        "default value": Liability()
    },
    VPerson.VRentalExpenses: {
        "attribute name": "rental_expenses",
        "default value": Liability()
    },
    VPerson.VAlimonyPaid: {
        "attribute name": "alimony_paid",
        "default value": Money()
    },
    VPerson.VGamblingLosses: {
        "attribute name": "gambling_losses",
        "default value": Money()
    },
    VPerson.VMovingExpenses: {
        "attribute name": "moving_expenses",
        "default value": Liability()
    },
    VPerson.VPublicCashDonations: {
        "attribute name": "public_cash_donations",
        "default value": Money()
    },
    VPerson.VPrivateCashDonations: {
        "attribute name": "private_cash_donations",
        "default value": Money()
    },
    VPerson.VPublicNonCashDonations: {
        "attribute name": "public_non_cash_donations",
        "default value": Money()
    },
    VPerson.VPublicCapitalGainsDonations: {
        "attribute name": "public_capital_gains_donations",
        "default value": Money()
    },
    VPerson.VPrivateCapitalGainsDonations: {
        "attribute name": "private_capital_gains_donations",
        "default value": Money()
    },
    VPerson.VInvestmentInterestExpense: {
        "attribute name": "investment_interest_expense",
        "default value": Liability()
    },
    VPerson.VSALT: {
        "attribute name": "SALT",
        "default value": Tax()
    },
    VPerson.VTotalInvestmentInterestExpense: {
        "attribute name": "total_investment_interest_expense",
        "default value": Liability()
    },
    VPerson.VTotalDebtBasedInvestmentEarnings: {
        "attribute name": "total_debt_based_investment_earnings",
        "default value": Money()
    },
    VPerson.VGrossIncome: {
        "attribute name": "gross_income",
        "default value": Money()
    },
    VPerson.VAdjustedIncome: {
        "attribute name": "adjusted_income",
        "default value": Money()
    },
    VPerson.VPropertyValue: {
        "attribute name": "property_value",
        "default value": Money()
    },
    VPerson.VWealth: {
        "attribute name": "wealth",
        "default value": Money()
    },
    VPerson.VCapitalGain: {
        "attribute name": "capital_gain",
        "default value": Money()
    },
    VPerson.VCustomBase: {
        "attribute name": "custom_base",
        "default value": Money()
    }
}
def vperson_to_person_attribute(vperson, person, converter):
    if isinstance(vperson, VPerson):
        if vperson in converter:
            attribute_name = converter[vperson]["attribute name"]
            if hasattr(person, attribute_name):
                return getattr(person, attribute_name)
            else:
                return converter[vperson]["default value"]
def vperson_dictionary_to_person_attribute(variables:dict, person, converter):
    for key, its_value in variables.items():
        if isinstance(its_value, VPerson):
            variables[key] = vperson_to_person_attribute(its_value, person, converter)
        elif isinstance(its_value, dict):
            variables[key] = vperson_dictionary_to_person_attribute(its_value, person, converter)
    return variables
def apply_raw_deductibles(dictionary:dict, person, converter):
    for key, its_value in dictionary.items():
        if isinstance(its_value, dict):
            apply_raw_deductibles(its_value, person, converter)
        elif key == ItemItemization.DeductibleValue:
            dictionary[key] = vperson_to_person_attribute(its_value, person, converter)
    return dictionary
def calculate_pre_base_agi_itemization(items:dict, person, converter=None):
    if converter is None:
        converter = vperson_to_person_attributes
    base_agi_dependent_indicators = [VPerson.VFederalBaseAGI, VPerson.VCurrentBaseAGI, VPerson.VStateBaseAGI, VPerson.VCustomBase]
    accumulated_directs = Money()
    accumulated_from_receivers = Money()
    ledger = {}
    for item in items.values():
        if not lookup_values_in_nested(item, base_agi_dependent_indicators):
            if item[ItemItemization.ItemItemizationType] == ItemItemizationType.Direct:
                accumulated_directs += calculate_item_directly(item, person, converter)
            elif item[ItemItemization.ItemItemizationType] == ItemItemizationType.Feeder:
                if ledger.get(item[ItemItemization.ReceiverCode]):
                    ledger[item[ItemItemization.ReceiverCode]] += calculate_item_directly(item, person, converter)
                else:
                    ledger[item[ItemItemization.ReceiverCode]] = calculate_item_directly(item, person, converter)
    for item in items.values():
        if item[ItemItemization.ItemItemizationType] == ItemItemizationType.Receiver:
            if not item[ItemItemization.HaveBaseAGIDependentFeeders]:
                receiving_code = item[ItemItemization.ReceivingCode]
                total_received = ledger[receiving_code]
                accumulated_from_receivers += calculate_item_directly(item, person, converter, True, total_received)
    return accumulated_directs+accumulated_from_receivers
def calculate_post_base_agi_itemization(items:dict, person, converter):
    accumulated_directs = Money()
    accumulated_from_receivers = Money()
    ledger = {}
    for item in items.values():
        if item[ItemItemization.ItemItemizationType] == ItemItemizationType.Direct:
            accumulated_directs += calculate_item_directly(item, person, converter)
        elif item[ItemItemization.ItemItemizationType] == ItemItemizationType.Feeder:
            if ledger.get(item[ItemItemization.ReceiverCode]):
                ledger[item[ItemItemization.ReceiverCode]] += calculate_item_directly(item, person, converter)
            else:
                ledger[item[ItemItemization.ReceiverCode]] = calculate_item_directly(item, person, converter)
    for item in items.values():
        if item[ItemItemization.ItemItemizationType] == ItemItemizationType.Receiver:
            receiving_code = item[ItemItemization.ReceivingCode]
            total_received = ledger[receiving_code]
            accumulated_from_receivers += calculate_item_directly(item, person, converter, True, total_received)
    return accumulated_directs + accumulated_from_receivers
def calculate_item_directly(item:dict, person, converter, receiver=False, total_received=None):
    if ItemItemization.ItemizationCaps in item:
        caps = calculate_caps(item[ItemItemization.ItemizationCaps], person, converter)
        upper_limits = caps[0]
        lower_limits = caps[1]
        smallest_upper_limit = min(upper_limits)
        greatest_lower_limit = max(lower_limits)
    else:
        smallest_upper_limit = Money(Decimal("Infinity"))
        greatest_lower_limit = Money(Decimal("0"))
    if receiver:
        itemization_value = total_received
    else:
        itemization_value = vperson_to_person_attribute(item[ItemItemization.DeductibleValue], person, converter)
    if itemization_value >= greatest_lower_limit:
        itemization_value -= greatest_lower_limit
        itemization_value = min(itemization_value, smallest_upper_limit)
    else:
        itemization_value = Money()
    return itemization_value
def calculate_caps(caps:dict, person, converter):
    upper_limits = []
    lower_limits = []
    for cap in caps.values():
        cap_result = calculate_cap(cap, person, converter)
        if cap_result[1] == LimitType.UpperLimit:
            upper_limits.append(cap_result[0])
        elif cap_result[1] == LimitType.LowerLimit:
            lower_limits.append(cap_result[0])
    if not upper_limits:
        upper_limits.append(Money(Decimal("Infinity")))
    if not lower_limits:
        lower_limits.append(Money())
    return upper_limits, lower_limits
def calculate_cap(cap:dict, person, converter):
    if cap[ItemItemization.ItemizationCapType] == ItemizationCapType.DynamicCap:
        if cap.get(Values.DynamicValue):
            cap_value =  vperson_to_person_attribute(cap[Values.DynamicValue], person, converter)
        else:
            cap_value = calculate_smart_values(cap[Values.SmartValueA], cap[Values.SmartValueB], cap[Values.InterValuesOperation], person, converter)
    else:
        cap_value = cap[Values.FixedValue]
    capping_method = cap[ItemItemization.LimitType]
    return cap_value, capping_method
def calculate_smart_values(a, b, operation, person, converter):
    if isinstance(a, dict):
        a = calculate_smart_values(a[Values.SmartValueA], a[Values.SmartValueB], a[Values.InterValuesOperation], person, converter)
    elif isinstance(a, VPerson):
        a = vperson_to_person_attribute(a, person, converter)
    if isinstance(b, dict):
        b = calculate_smart_values(b[Values.SmartValueA], b[Values.SmartValueB], b[Values.InterValuesOperation], person, converter)
    elif isinstance(b, VPerson):
        b = vperson_to_person_attribute(b, person, converter)
    if operation == InterValuesOperation.Addition:
        results = a+b
    elif operation == InterValuesOperation.Subtraction:
        results = a-b
    elif operation == InterValuesOperation.Multiplication:
        results = a*b
    elif operation == InterValuesOperation.Division:
        results = a/b
    elif operation == InterValuesOperation.FloorSubtraction:
        if a >= b:
            results = a-b
        else:
            results = a-a
    else:
        raise TypeError
    return results
def calculate_tax_benefits(person, variables, converter):
    standard_deduction = calculate_tax_benefits_when_standardized(person, variables)
    itemized = calculate_post_base_agi_itemization(person, variables, converter)
    if standard_deduction >= itemized:
        return standard_deduction, Deduction.StandardDeduction
    else:
        return itemized, Deduction.ItemizedDeduction
def calculate_exemptions(person, variables):
    return variables[Variables.TaxBenefits][TaxBenefits.Exemption][person.status]
def calculate_tax_benefits_when_standardized(person, variables):
    standard_deduction = variables[Variables.TaxBenefits][TaxBenefits.Deduction][Deduction.StandardDeduction][person.status]
    exemption = calculate_exemptions(person, variables)
    return standard_deduction+exemption
def calculate_tax_benefits_when_itemizing(person, variables, converter=None):
    if converter is None:
        converter = vperson_to_person_attributes
    items = variables[Variables.TaxBenefits][TaxBenefits.Deduction][Deduction.Itemization]
    exemptions = calculate_exemptions(person, variables)
    itemizations = calculate_post_base_agi_itemization(items, person, converter)
    return exemptions + itemizations
def calculate_tax():
    pass
class Person:
    def __init__(self, first_name:str="", last_name:str="", marital_status:MaritalStatus=MaritalStatus.UnSpecified, age:int=0, income:Money=Money(Decimal("0")), state:State=State.UnSpecifiedState,
                 attributes=None, variables_index=None):
        if attributes is None:
            attributes = {}
        if variables_index is None:
            variables_index = default_variables_index
        self.first = first_name
        self.last = last_name
        self.status = marital_status
        self.age = age
        self.income = income
        self.state = state
        self.variables_index = variables_index
        self.federal_variables = self.variables_index[LocalIndex.FederalVariablesIndex]
        self.state_variables = self.variables_index[LocalIndex.StatesVariablesIndex]
        self.city_variables = self.variables_index[LocalIndex.CitiesVariablesIndex]
        self.municipal_variables = self.variables_index[LocalIndex.MunicipalitiesVariablesIndex]
        self.slot0 = None
        self.slot1 = None
        self.slot2 = None
        viable_optional_attributes = {
            "total_itemized": Money,  # Always present
            "charitable_contributions": Money,
            "public_cash_donations": Money,
            "public_non_cash_donations": Money,
            "private_cash_donations": Money,
            "public_capital_gains_donations": Money,
            "private_capital_gains_donations": Money,
            "gambling_losses": Money,
            "alimony_paid": Money,
            "retirement_contributions": Money,
            "health_insurance_premiums": Money,
            "total_debt_based_investment_earnings": Money,
            "medical_expenses": Liability,
            "childcare_expenses": Liability,
            "job_expenses": Liability,
            "education_expenses": Liability,
            "student_loan_interest": Liability,
            "mortgage_interest": Liability,
            "total_investment_expense": Liability,
            "investment_interest_expense": Liability,
            "business_expenses": Liability,
            "rental_expenses": Liability,
            "moving_expenses": Liability,  # Limited eligibility under current laws
            "property_taxes": Tax,
            "SALT": Tax,
        }
        for key, its_value in attributes.items():
            if key in viable_optional_attributes and type(its_value) == viable_optional_attributes[key]:
                setattr(self, key, its_value)
    @property
    def federal_standardized_deductions(self):
        return calculate_tax_benefits_when_standardized(self, self.federal_variables)
    @property
    def federal_itemized_deductions(self):
        return calculate_tax_benefits_when_itemizing(self, self.federal_variables)
    @property
    def federal_deductions(self):
        return max(self.federal_standardized_deductions, self.federal_itemized_deductions)
    @property
    def federal_base_agi(self):
        # noinspection PyTypeChecker
        items = self.federal_variables[Variables.TaxBenefits][TaxBenefits.Deduction][Deduction.Itemization]
        pre_base_agi_itemization = calculate_pre_base_agi_itemization(items, self, vperson_to_person_attributes)
        if self.income >= pre_base_agi_itemization:
            return self.income - pre_base_agi_itemization
        else:
            return Money()
    @property
    def federal_final_agi(self):
        if self.income >= self.federal_deductions:
            return self.income - self.federal_deductions
        else:
            return Money()




p = Person()
p.status = MaritalStatus.Single
p.income = Money(Decimal("500000000"))
# Set attributes for the person
# setattr(p, "federal_base_agi", Money(Decimal("50000000")))  # $500,000
setattr(p, "medical_expenses", Liability(Decimal("6000000")))  # $60,000
setattr(p, "mortgage_interest", Liability(Decimal("200000000")))  # $2,000,000
setattr(p, "property_taxes", Liability(Decimal("4000000")))  # $40,000
setattr(p, "SALT", Money(Decimal("5000000")))  # $50,000
setattr(p, "public_cash_donations", Money(Decimal("25000000")))  # $250,000
setattr(p, "private_cash_donations", Money(Decimal("10000000")))  # $100,000
setattr(p, "investment_interest_expense", Liability(Decimal("12000000")))  # $120,000
setattr(p, "total_debt_based_investment_earnings", Money(Decimal("8000000")))  # $80,000 (caps investment deduction)
nested_smart_value = {
    Values.SmartValueA: {
        Values.SmartValueA: {
            Values.SmartValueA: {
                Values.SmartValueA: {
                    Values.SmartValueA: 5,
                    Values.SmartValueB: 3,
                    Values.InterValuesOperation: InterValuesOperation.Addition
                },
                Values.SmartValueB: {
                    Values.SmartValueA: 10,
                    Values.SmartValueB: 2,
                    Values.InterValuesOperation: InterValuesOperation.Multiplication
                },
                Values.InterValuesOperation: InterValuesOperation.Subtraction
            },
            Values.SmartValueB: {
                Values.SmartValueA: 8,
                Values.SmartValueB: {
                    Values.SmartValueA: 4,
                    Values.SmartValueB: 2,
                    Values.InterValuesOperation: InterValuesOperation.Division
                },
                Values.InterValuesOperation: InterValuesOperation.FloorSubtraction
            },
            Values.InterValuesOperation: InterValuesOperation.Multiplication
        },
        Values.SmartValueB: {
            Values.SmartValueA: {
                Values.SmartValueA: 7,
                Values.SmartValueB: {
                    Values.SmartValueA: {
                        Values.SmartValueA: 6,
                        Values.SmartValueB: 2,
                        Values.InterValuesOperation: InterValuesOperation.Subtraction
                    },
                    Values.SmartValueB: 3,
                    Values.InterValuesOperation: InterValuesOperation.Addition
                },
                Values.InterValuesOperation: InterValuesOperation.Multiplication
            },
            Values.SmartValueB: 9,
            Values.InterValuesOperation: InterValuesOperation.Division
        },
        Values.InterValuesOperation: InterValuesOperation.Subtraction
    },
    Values.SmartValueB: {
        Values.SmartValueA: {
            Values.SmartValueA: {
                Values.SmartValueA: 2,
                Values.SmartValueB: 3,
                Values.InterValuesOperation: InterValuesOperation.Multiplication
            },
            Values.SmartValueB: {
                Values.SmartValueA: {
                    Values.SmartValueA: 10,
                    Values.SmartValueB: 5,
                    Values.InterValuesOperation: InterValuesOperation.FloorSubtraction
                },
                Values.SmartValueB: 4,
                Values.InterValuesOperation: InterValuesOperation.Addition
            },
            Values.InterValuesOperation: InterValuesOperation.Subtraction
        },
        Values.SmartValueB: {
            Values.SmartValueA: {
                Values.SmartValueA: 20,
                Values.SmartValueB: 4,
                Values.InterValuesOperation: InterValuesOperation.Division
            },
            Values.SmartValueB: {
                Values.SmartValueA: 15,
                Values.SmartValueB: {
                    Values.SmartValueA: 6,
                    Values.SmartValueB: 3,
                    Values.InterValuesOperation: InterValuesOperation.Multiplication
                },
                Values.InterValuesOperation: InterValuesOperation.FloorSubtraction
            },
            Values.InterValuesOperation: InterValuesOperation.Multiplication
        },
        Values.InterValuesOperation: InterValuesOperation.Addition
    },
    Values.InterValuesOperation: InterValuesOperation.Division
}

