import decimal, datetime, sys
from decimal import Decimal
from dateutil.relativedelta import relativedelta

from TaxiCal.NestedDictionariesReader import nested_dictionary_reader
from TaxiCalCustomEnums import *
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
    def __str__(self):
        return self.name
class PaymentStatus(str, Enum):
    Paid = "Paid"
    UnPaid = "UnPaid"
    Capitalized = "Capitalized"
    NotSpecified = "NotSpecified"
    PartiallyPaid = "PartiallyPaid"
    InterestOnly = "InterestOnly"
    def __str__(self):
        return self.name
class MaritalStatus(str, Enum):
    Single = "Single"
    MarriedNonJoint = "MarriedNonJoint"
    MarriedJoint = "MarriedJoint"
    UnSpecified = "UnSpecified"
    def __str__(self):
        return self.name
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
from TaxiCal.LookUpInNestedDictionary import lookup_values_in_nested
def str_to_object(string, enums_list:list):
    financial_units_markers = {
        "MoneyInCents ": Money,
        "TaxInCents ": Tax,
        "LiabilityInCents ": Liability,
    }
    if isinstance(string, str):
        for marker, cls in financial_units_markers.items():
            if marker in string:
                stripped_string = string.replace(marker, "")
                try:
                    return cls(Decimal(stripped_string))
                except decimal.InvalidOperation:
                    pass
                except  ValueError:
                    return "Negative Financial unit crab."
        if "Decimal " in string:
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
    elif isinstance(obj, Tax):
        return f"TaxInCents {obj.amount}"
    elif isinstance(obj, Liability):
        return f"LiabilityInCents {obj.amount}"
    elif isinstance(obj, relativedelta):
        relativedelta_data = obj.__dict__.copy()
        relativedelta_data["ThisKeyIsReservedForTypesOnly"] = "relativedelta"
        return relativedelta_data
    elif isinstance(obj, datetime.datetime):
        the_iso_format = obj.isoformat()
        return f'''ThisIsADateTimeObject{the_iso_format}'''
    else:
        raise TypeError(f"Not serializable, bro, type is {type(obj)}")
UnKnown = 'UnKnown'
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
                Configurations.TaxationType: TaxationType.ProgressiveRate,
                Configurations.TaxBase: VPerson.VFederalFinalAGI,
                Configurations.TheFlatRate: Decimal("0.05"),
                Configurations.HighestBracketCeiling: 7,
                Configurations.TheFixedAmount: Money(Decimal("7987654")),
                Configurations.HaveCap: False,
                Configurations.AdjustedIncomeSource: None, # Redundant #ForRemoval
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
        2: {
            TaxVariables.Configurations: {
                Configurations.TaxNameType: TaxNameType.CustomName,
                Configurations.TaxName: "The Tomato Tax",
                Configurations.TaxationType: TaxationType.FixedAmount,
                Configurations.TheFixedAmount: Tax(Decimal("15000")),
                Configurations.HaveCap: False
            },
        },
        3: {
            TaxVariables.Configurations: {
                Configurations.TaxNameType : TaxNameType.CustomName,
                Configurations.TaxName: "Moda Fag",
                Configurations.TaxationType: TaxationType.FlatRate,
                Configurations.TaxBase: VPerson.VFederalFinalAGI,
                Configurations.TheFlatRate: Decimal("0.01"),
                Configurations.HaveCap: True,
            },
            TaxVariables.TaxCaps: {
                1: {
                    TaxCap.TaxLimitType: TaxLimitType.UpperLimitTaxCap,
                    TaxCap.TaxCapType: TaxCapType.TaxFixedCap,
                    Values.FixedValue: Money(Decimal("100000"))
                },
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
                    ItemItemization.FeederSpecificCode: 0,
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
                    ItemItemization.FeederSpecificCode: 0,
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
                    ItemItemization.FeederSpecificCode: 1,
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
                    ItemItemization.FeederSpecificCode: 2,
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
                    ItemItemization.FeederSpecificCode: 3,
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
                    ItemItemization.FeederSpecificCode: 4,
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
standard_user_preference = {
    Preference.TaxPreference:{
        TaxPreference.PreferredDeductionType: {
            Jurisdiction.Federal: PreferredDeductionType.PreferAuto,
            Jurisdiction.State: PreferredDeductionType.PreferAuto,
            Jurisdiction.County: PreferredDeductionType.PreferAuto,
            Jurisdiction.Local: PreferredDeductionType.PreferAuto,
            Jurisdiction.City: PreferredDeductionType.PreferAuto,
            Jurisdiction.Municipal: PreferredDeductionType.PreferAuto,
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
                Configurations.TaxationType: TaxationType.ProgressiveRate,
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
new_york_variables = {
    Variables.Configurations: {
        Configurations.VerifierConfigurations: {
            VerifierConfigurations.RequiredVerifierVersion: 1,
            VerifierConfigurations.SupportsForwardCompatibility: True,
            VerifierConfigurations.SupportsBackwardCompatibility: False,
        },
        Configurations.VariablesType: VariablesType.StateVariables,
        Configurations.LastUpdated: datetime.datetime(2025, 3, 31)
    },
    Variables.Taxes: {
        1: {
            TaxVariables.Configurations: {
                Configurations.TaxNameType: TaxNameType.StandardName,
                Configurations.TaxName: StandardTaxName.StateIncomeTax,
                Configurations.TaxationType: TaxationType.ProgressiveRate,
                Configurations.TaxBase: VPerson.VStateFinalAGI,
                Configurations.AdjustedIncomeSource: AdjustedIncomeSource.FromState,
            },
            TaxVariables.BracketCeilings: {
                MaritalStatus.Single: {
                    1: Money(Decimal("850000")),
                    2: Money(Decimal("1170000")),
                    3: Money(Decimal("1390000")),
                    4: Money(Decimal("2140000")),
                    5: Money(Decimal("8065000")),
                    6: Money(Decimal("21540000")),
                    7: Money(Decimal("107755000")),
                    8: Money(Decimal("500000000")),
                    9: Money(Decimal("Infinity")),
                },
                MaritalStatus.MarriedJoint: {
                    1: Money(Decimal("1715000")),
                    2: Money(Decimal("2360000")),
                    3: Money(Decimal("2790000")),
                    4: Money(Decimal("4280000")),
                    5: Money(Decimal("16155000")),
                    6: Money(Decimal("32320000")),
                    7: Money(Decimal("215400000")),
                    8: Money(Decimal("500000000")),
                    9: Money(Decimal("Infinity")),
                },
                MaritalStatus.MarriedNonJoint: {  # Copy of Single
                    1: Money(Decimal("850000")),
                    2: Money(Decimal("1170000")),
                    3: Money(Decimal("1390000")),
                    4: Money(Decimal("2140000")),
                    5: Money(Decimal("8065000")),
                    6: Money(Decimal("21540000")),
                    7: Money(Decimal("107755000")),
                    8: Money(Decimal("500000000")),
                    9: Money(Decimal("Infinity")),
                },
            },
            TaxVariables.Rates: {
                1: Decimal("0.04"),
                2: Decimal("0.045"),
                3: Decimal("0.0525"),
                4: Decimal("0.059"),
                5: Decimal("0.0597"),
                6: Decimal("0.0633"),
                7: Decimal("0.0685"),
                8: Decimal("0.103"),
                9: Decimal("0.109"),
            },
        },
    },
    Variables.TaxBenefits: {
        TaxBenefits.Deduction: {
            Deduction.StandardDeduction: {
                MaritalStatus.Single: Money(Decimal("800000")),
                MaritalStatus.MarriedJoint: Money(Decimal("1605000")),
                MaritalStatus.MarriedNonJoint: Money(Decimal("800000")),
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
                            Values.FixedValue: Money(Decimal("10000000")),
                        },
                    },
                },
                Itemization.MedicalAndDentalExpenses: {
                    ItemItemization.ItemItemizationType: ItemItemizationType.Direct,
                    ItemItemization.DeductibleValue: VPerson.VMedicalExpenses,
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.LowerLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.SmartValueA: VPerson.VFederalBaseAGI,
                            Values.SmartValueB: Decimal("0.075"),
                            Values.InterValuesOperation: InterValuesOperation.Multiplication,
                        },
                    },
                },
                Itemization.CharitableContributions: {
                    ItemItemization.ItemItemizationType: ItemItemizationType.Direct,
                    ItemItemization.DeductibleValue: VPerson.VCharitableContributions,
                    ItemItemization.CapsAppliedCount: 1,
                    ItemItemization.ItemizationCaps: {
                        1: {
                            ItemItemization.LimitType: LimitType.UpperLimit,
                            ItemItemization.ItemizationCapType: ItemizationCapType.DynamicCap,
                            Values.SmartValueA: VPerson.VFederalBaseAGI,
                            Values.SmartValueB: Decimal("0.60"),
                            Values.InterValuesOperation: InterValuesOperation.Multiplication,
                        },
                    },
                },
            },
        },
        TaxBenefits.Exemption: {
            MaritalStatus.Single: Money(Decimal("0")),  # NY does not have a personal exemption
            MaritalStatus.MarriedJoint: Money(Decimal("0")),
            MaritalStatus.MarriedNonJoint: Money(Decimal("0")),
        },
    },
}
default_variables_index = {
    LocalIndex.FederalVariablesIndex: standard_variables,
    LocalIndex.StatesVariablesIndex: {
        State.California: california_variables,
        State.NewYork: new_york_variables
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
    VPerson.VStateFinalAGI: {
        "attribute name": "federal_final_agi",
        "default value": Money()
    },
    VPerson.VStateBaseAGI:{
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

class Person:
    def __init__(self, first_name:str="", last_name:str="", marital_status:MaritalStatus=MaritalStatus.UnSpecified, age:int=0, income:Money=Money(Decimal("0")), state:State=State.UnSpecifiedState,
                 attributes=None, variables_index=None, preference_settings=None):
        if attributes is None:
            attributes = {}
        if variables_index is None:
            variables_index = default_variables_index
        if preference_settings is None:
            preference_settings = standard_user_preference
        self.first = first_name
        self.last = last_name
        self.status = marital_status
        self.age = age
        self.income = income
        self.state = state
        self.variables_index = variables_index
        self.preference = preference_settings
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
    def federal_variables(self):
        return self.variables_index[LocalIndex.FederalVariablesIndex]
    @property
    def state_variables(self):
        # noinspection PyTypeChecker
        return self.variables_index[LocalIndex.StatesVariablesIndex][self.state]
    @property
    def city_variables(self):
        return self.variables_index[LocalIndex.CitiesVariablesIndex]
    @property
    def municipal_variables(self):
        return self.variables_index[LocalIndex.MunicipalitiesVariablesIndex]
    @property
    def federal_standardized_deductions(self):
        return calculate_tax_benefits_when_standardized(self, self.federal_variables)
    @property
    def federal_itemized_deductions(self):
        return calculate_tax_benefits_when_itemizing(self, self.federal_variables)
    @property
    def federal_deductions(self):
        preference = self.preference[Preference.TaxPreference][TaxPreference.PreferredDeductionType][Jurisdiction.Federal]
        if preference == PreferredDeductionType.PreferAuto:
            return max(self.federal_standardized_deductions, self.federal_itemized_deductions)
        elif preference == PreferredDeductionType.PreferStandardized:
            return self.federal_standardized_deductions
        elif preference == PreferredDeductionType.PreferItemized:
            return self.federal_itemized_deductions
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

    @property
    def state_standardized_deductions(self):
        return calculate_tax_benefits_when_standardized(self, self.state_variables)

    @property
    def state_itemized_deductions(self):
        return calculate_tax_benefits_when_itemizing(self, self.state_variables)

    @property
    def state_deductions(self):
        preference = self.preference[Preference.TaxPreference][TaxPreference.PreferredDeductionType][
            Jurisdiction.State]
        if preference == PreferredDeductionType.PreferAuto:
            return max(self.state_standardized_deductions, self.state_itemized_deductions)
        elif preference == PreferredDeductionType.PreferStandardized:
            return self.state_standardized_deductions
        elif preference == PreferredDeductionType.PreferItemized:
            return self.state_itemized_deductions

    @property
    def state_base_agi(self):
        # noinspection PyTypeChecker
        items = self.state_variables[Variables.TaxBenefits][TaxBenefits.Deduction][Deduction.Itemization]
        pre_base_agi_itemization = calculate_pre_base_agi_itemization(items, self, vperson_to_person_attributes)
        if self.income >= pre_base_agi_itemization:
            return self.income - pre_base_agi_itemization
        else:
            return Money()

    @property
    def state_final_agi(self):
        if self.income >= self.state_deductions:
            return self.income - self.state_deductions
        else:
            return Money()

    @property
    def city_standardized_deductions(self):
        return calculate_tax_benefits_when_standardized(self, self.city_variables)

    @property
    def city_itemized_deductions(self):
        return calculate_tax_benefits_when_itemizing(self, self.city_variables)

    @property
    def city_deductions(self):
        preference = self.preference[Preference.TaxPreference][TaxPreference.PreferredDeductionType][
            Jurisdiction.State]
        if preference == PreferredDeductionType.PreferAuto:
            return max(self.city_standardized_deductions, self.city_itemized_deductions)
        elif preference == PreferredDeductionType.PreferStandardized:
            return self.city_standardized_deductions
        elif preference == PreferredDeductionType.PreferItemized:
            return self.city_itemized_deductions

    @property
    def city_base_agi(self):
        # noinspection PyTypeChecker
        items = self.city_variables[Variables.TaxBenefits][TaxBenefits.Deduction][Deduction.Itemization]
        pre_base_agi_itemization = calculate_pre_base_agi_itemization(items, self, vperson_to_person_attributes)
        if self.income >= pre_base_agi_itemization:
            return self.income - pre_base_agi_itemization
        else:
            return Money()

    @property
    def city_final_agi(self):
        if self.income >= self.city_deductions:
            return self.income - self.city_deductions
        else:
            return Money()

    @property
    def municipal_standardized_deductions(self):
        return calculate_tax_benefits_when_standardized(self, self.municipal_variables)

    @property
    def municipal_itemized_deductions(self):
        return calculate_tax_benefits_when_itemizing(self, self.municipal_variables)

    @property
    def municipal_deductions(self):
        preference = self.preference[Preference.TaxPreference][TaxPreference.PreferredDeductionType][
            Jurisdiction.State]
        if preference == PreferredDeductionType.PreferAuto:
            return max(self.municipal_standardized_deductions, self.municipal_itemized_deductions)
        elif preference == PreferredDeductionType.PreferStandardized:
            return self.municipal_standardized_deductions
        elif preference == PreferredDeductionType.PreferItemized:
            return self.municipal_itemized_deductions

    @property
    def municipal_base_agi(self):
        # noinspection PyTypeChecker
        items = self.municipal_variables[Variables.TaxBenefits][TaxBenefits.Deduction][Deduction.Itemization]
        pre_base_agi_itemization = calculate_pre_base_agi_itemization(items, self, vperson_to_person_attributes)
        if self.income >= pre_base_agi_itemization:
            return self.income - pre_base_agi_itemization
        else:
            return Money()

    @property
    def municipal_final_agi(self):
        if self.income >= self.municipal_deductions:
            return self.income - self.municipal_deductions
        else:
            return Money()
def verify_variables_viability_and_integrity(variables:dict, break_for_ultra_safety=False):
    result = {
        CheckResults.ViabilityForChecking: False,
        CheckResults.Integrity: True,
        CheckResults.IntegrityFailureCode: None,
        CheckResults.Safety: True,
        CheckResults.UltraSafety: True,
        CheckResults.SafetyFailureCode: None,
    }
    verifier_version = 1
    required_verifier_version = variables.get(Variables.Configurations, {}).get(Configurations.VerifierConfigurations, {}).get(VerifierConfigurations.RequiredVerifierVersion)
    if verifier_version == required_verifier_version:
        result[CheckResults.ViabilityForChecking] = True
    else:
        if verifier_version > required_verifier_version:
            forward_compatibility = variables.get(Variables.Configurations, {}).get(Configurations.VerifierConfigurations, {}).get(VerifierConfigurations.SupportsForwardCompatibility)
            if forward_compatibility:
                result[CheckResults.ViabilityForChecking] = True
        else:
            backward_compatibility = variables.get(Variables.Configurations, {}).get(Configurations.VerifierConfigurations, {}).get(VerifierConfigurations.SupportsBackwardCompatibility)
            if backward_compatibility:
                result[CheckResults.ViabilityForChecking] = True
    if result[CheckResults.ViabilityForChecking]:
        if variables.get(Variables.Taxes):
            if isinstance(variables.get(Variables.Taxes), dict):
                taxes_verification_result = verify_taxes_integrity(variables.get(Variables.Taxes, {}),break_for_ultra_safety)
                if not taxes_verification_result[CheckResults.Integrity] or not taxes_verification_result[CheckResults.Safety]:
                    result = taxes_verification_result
            else:
                result[CheckResults.IntegrityFailureCode] = "Taxes are not a dictionary"
                result[CheckResults.Integrity] = False
                result[CheckResults.Safety] = False
                result[CheckResults.SafetyFailureCode] = "Failure due to Integrity failure."
        else:
            result[CheckResults.IntegrityFailureCode] = "Taxes are missing."
            result[CheckResults.Integrity] = False
            result[CheckResults.Safety] = False
            result[CheckResults.SafetyFailureCode] = "Failure due to Integrity failure."
        if variables.get(Variables.TaxBenefits):
            if isinstance(variables.get(Variables.TaxBenefits), dict):
                tax_benefits_verification_result = verify_tax_benefits(variables.get(Variables.TaxBenefits),break_for_ultra_safety)
                if not tax_benefits_verification_result[CheckResults.Integrity] or not tax_benefits_verification_result[CheckResults.Safety]:
                    result = tax_benefits_verification_result
            else:
                result[CheckResults.IntegrityFailureCode] = "Tax Benefits are not a dictionary"
                result[CheckResults.Integrity] = False
                result[CheckResults.Safety] = False
                result[CheckResults.SafetyFailureCode] = "Failure due to Integrity failure."
        else:
            result[CheckResults.IntegrityFailureCode] = "Tax Benefits are missing."
            result[CheckResults.Integrity] = False
            result[CheckResults.Safety] = False
            result[CheckResults.SafetyFailureCode] = "Failure due to Integrity failure."
    else:
        result = {
        CheckResults.ViabilityForChecking: False,
        CheckResults.Integrity: UnKnown,
        CheckResults.IntegrityFailureCode: None,
        CheckResults.Safety: UnKnown,
        CheckResults.UltraSafety: UnKnown,
        CheckResults.SafetyFailureCode: None,
    }
    return result
def verify_taxes_integrity(taxes:dict, break_for_ultra_safety=False):
    result = {
        CheckResults.Integrity: True,
        CheckResults.IntegrityFailureCode: None,
        CheckResults.Safety: True,
        CheckResults.UltraSafety: True,
        CheckResults.SafetyFailureCode: None,
    }
    for tax_name ,tax in taxes.items():
        if isinstance(tax, dict):
            tax_result = verify_a_tax_integrity(tax)
            if not break_for_ultra_safety:
                if not tax_result[CheckResults.Integrity] or not tax_result[CheckResults.Safety]:
                    result = tax_result
                    break
            if break_for_ultra_safety and not tax_result[CheckResults.UltraSafety]:
                result = tax_result
                break
        else:
            result[CheckResults.Integrity] = False
            result[CheckResults.IntegrityFailureCode] = f'''Tax named "{tax_name}" is not a dictionary.'''
    if not result[CheckResults.Integrity]:
        result[CheckResults.Safety] = False
        result[CheckResults.UltraSafety] = False
    return result
def verify_a_tax_integrity(tax:dict, break_for_ultra_safety=False):
    result = {
        CheckResults.Integrity: True,
        CheckResults.IntegrityFailureCode: None,
        CheckResults.Safety: True,
        CheckResults.UltraSafety: True,
        CheckResults.SafetyFailureCode: None,
    }
    while True:
        tax_name_type = tax.get(TaxVariables.Configurations, {}).get(Configurations.TaxNameType)
        tax_name = tax.get(TaxVariables.Configurations, {}).get(Configurations.TaxName)
        if not isinstance(tax_name_type, TaxNameType):
            result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Tax name type is not of class TaxNameType."
            result[CheckResults.Integrity] = False
            break
        if tax_name_type == TaxNameType.StandardName and not isinstance(tax_name, StandardTaxName):
            result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Tax name type is set to standard, while name is custom."
            result[CheckResults.Integrity] = False
            break
        if tax_name_type == TaxNameType.CustomName and not isinstance(tax_name, str):
            result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Tax name type is set to custom, but name is not a string"
            result[CheckResults.Integrity] = False
            break
        have_cap = tax.get(TaxVariables.Configurations, {}).get(Configurations.HaveCap)
        if not isinstance(have_cap, bool):
            result[CheckResults.IntegrityFailureCode] = f"{tax_name}: HaveCap value is missing or not a bool."
            result[CheckResults.Integrity] = False
            break
        taxation_type = tax.get(TaxVariables.Configurations, {}).get(Configurations.TaxationType)
        if taxation_type == TaxationType.ProgressiveRate:
            tax_base = tax.get(TaxVariables.Configurations, {}).get(Configurations.TaxBase)
            if not isinstance(tax_base, VPerson):
                result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Tax base is not a VPerson."
                result[CheckResults.Integrity] = False
                break
            highest_bracket_ceil = tax.get(TaxVariables.Configurations, {}).get(Configurations.HighestBracketCeiling)
            if not isinstance(highest_bracket_ceil, int):
                result[CheckResults.IntegrityFailureCode] = f"{tax_name}: highest bracket ceil is missing or not an int."
                result[CheckResults.Integrity] = False
                break
            if not tax.get(TaxVariables.BracketCeilings):
                result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Taxation type is progressive, but there are no bracket ceilings."
                result[CheckResults.Integrity] = False
                break
            if not tax.get(TaxVariables.Rates):
                result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Taxation type is progressive, but there are no rates."
                result[CheckResults.Integrity] = False
                break
            for status in [MaritalStatus.Single, MaritalStatus.MarriedJoint, MaritalStatus.MarriedNonJoint]:
                if isinstance(tax.get(TaxVariables.BracketCeilings).get(status), dict):
                    if not highest_bracket_ceil == len(tax.get(TaxVariables.BracketCeilings).get(status)):
                        result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Alleged highest tax bracket is not equal to len of brackets ceilings"
                        result[CheckResults.Integrity] = False
                        break
                else:
                    result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Bracket ceilings for status {status} is missing."
                    result[CheckResults.Integrity] = False
                    break
                order = highest_bracket_ceil
                while order > 1:
                    current_ceil = tax.get(TaxVariables.BracketCeilings, {}).get(status, {}).get(order)
                    upcoming_smaller_ceil = tax.get(TaxVariables.BracketCeilings, {}).get(status, {}).get(order - 1)
                    if not current_ceil > upcoming_smaller_ceil:
                        result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Bracket ceilings for status {status} are disordered."
                        result[CheckResults.Integrity] = False
                        break
                    # noinspection PyUnreachableCode
                    if not isinstance(current_ceil, Money) or not isinstance(upcoming_smaller_ceil, Money):
                        result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Brackets ceilings are not of money class."
                        result[CheckResults.Integrity] = False
                        break
                    order -= 1
            if not result[CheckResults.Integrity]:
                break
            order = highest_bracket_ceil
            while order > 1:
                current_rate = tax.get(TaxVariables.Rates, {}).get(order)
                upcoming_smaller_rate = tax.get(TaxVariables.Rates, {}).get(order-1)
                # noinspection PyUnreachableCode
                if not isinstance(current_rate, Decimal) or not isinstance(upcoming_smaller_rate, Decimal):
                    result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Rates are not Decimal."
                    result[CheckResults.Integrity] = False
                    break
                if not current_rate > upcoming_smaller_rate:
                    result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Rates are disordered."
                    result[CheckResults.Integrity] = False
                    break
                if current_rate >= Decimal("1") or upcoming_smaller_rate >= Decimal("1"):
                    result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Rate is equal to or greater than 100%."
                    result[CheckResults.Integrity] = False
                    break
                order-=1
        elif taxation_type == TaxationType.FlatRate:
            tax_base = tax.get(TaxVariables.Configurations, {}).get(Configurations.TaxBase)
            if not isinstance(tax_base, VPerson):
                result[CheckResults.IntegrityFailureCode] = f"{tax_name}: Tax base is not a VPerson."
                result[CheckResults.Integrity] = False
            the_flat_rate = tax.get(TaxVariables.Configurations, {}).get(Configurations.TheFlatRate)
            if not isinstance(the_flat_rate, Decimal):
                result[CheckResults.IntegrityFailureCode] = f"{tax_name}: the flat rate is not a decimal or maybe missing."
                result[CheckResults.Integrity] = False
        elif taxation_type == TaxationType.FixedAmount:
            the_fixed_amount = tax.get(TaxVariables.Configurations, {}).get(Configurations.TheFixedAmount)
            if not isinstance(the_fixed_amount, Tax):
                result[CheckResults.IntegrityFailureCode] = f"{tax_name}: fixed amount is not of class Tax."
                result[CheckResults.Integrity] = False
        if tax[TaxVariables.Configurations][Configurations.HaveCap]:
            tax_cap_verification_result = verify_a_tax_caps(tax)
            if not tax_cap_verification_result[CheckResults.Integrity] or not tax_cap_verification_result[CheckResults.Safety]:
                result = tax_cap_verification_result
                break
            if break_for_ultra_safety and not tax_cap_verification_result[CheckResults.UltraSafety]:
                result = tax_cap_verification_result
                break
        break

    return result
def verify_a_tax_caps(tax:dict, break_for_ultra_safety=False):
    result = {
        CheckResults.Integrity: True,
        CheckResults.IntegrityFailureCode: None,
        CheckResults.Safety: True,
        CheckResults.UltraSafety: True,
        CheckResults.SafetyFailureCode: None,
    }
    caps = tax.get(TaxVariables.TaxCaps, {})
    for cap in caps.values():
        cap_verification_result = verify_a_tax_cap(cap)
        if not cap_verification_result[CheckResults.Integrity] or not cap_verification_result[CheckResults.Safety]:
            result = cap_verification_result
            break
        if break_for_ultra_safety and not cap_verification_result[CheckResults.UltraSafety]:
            result = cap_verification_result
            break
    return result
def verify_a_tax_cap(cap:dict, break_for_ultra_safety=False):
    result = {
        CheckResults.Integrity: True,
        CheckResults.IntegrityFailureCode: None,
        CheckResults.Safety: True,
        CheckResults.UltraSafety: True,
        CheckResults.SafetyFailureCode: None,
    }
    limit_type = cap.get(TaxCap.TaxLimitType)
    cap_type = cap.get(TaxCap.TaxCapType)
    while result[CheckResults.Integrity] and result[CheckResults.Safety]:
        if not isinstance(limit_type, TaxLimitType):
            result[CheckResults.IntegrityFailureCode] = f"Limit type is not of class LimitType: {limit_type}"
            result[CheckResults.Integrity] = False
        if not  isinstance(cap_type, TaxCapType):
            result[CheckResults.IntegrityFailureCode] = f"Cap type is not of class CapType: {cap_type}"
            result[CheckResults.Integrity] = False
        if cap_type == TaxCapType.TaxFixedCap:
            fixed_cap = cap.get(Values.FixedValue)
            if not isinstance(fixed_cap, StandardFinancialUnit):
                result[CheckResults.IntegrityFailureCode] = f"Fixed cap is not of class Standard Financial Unit: {fixed_cap}"
                result[CheckResults.Integrity] = False
        elif cap_type == TaxCapType.TaxDynamicCap:
            one_dynamic = cap.get(Values.DynamicValue)
            if one_dynamic:
                if not isinstance(one_dynamic, VPerson):
                    result[CheckResults.IntegrityFailureCode] = f"Dynamic value is not of class VPerson: {one_dynamic}"
                    result[CheckResults.Integrity] = False
            else:
                smart_a = cap.get(Values.SmartValueA)
                smart_b = cap.get(Values.SmartValueB)
                operation = cap.get(Values.InterValuesOperation)
                smart_values_integrity_result = verify_smart_values_integrity(smart_a, smart_b, operation)
                if smart_values_integrity_result[CheckResults.Integrity] and smart_values_integrity_result[CheckResults.Safety]:
                    smart_values_safety_result = verify_smart_values_safety(smart_a, smart_b, operation)
                    if not smart_values_safety_result[CheckResults.Safety]:
                        result[CheckResults.Safety] = smart_values_safety_result[CheckResults.Safety]
                        result[CheckResults.UltraSafety] = smart_values_safety_result[CheckResults.UltraSafety]
                        result[CheckResults.SafetyFailureCode] = smart_values_safety_result[CheckResults.SafetyFailureCode]
                    if break_for_ultra_safety and not smart_values_safety_result[CheckResults.UltraSafety]:
                        result[CheckResults.UltraSafety] = smart_values_safety_result[CheckResults.UltraSafety]
                        result[CheckResults.SafetyFailureCode] = smart_values_safety_result[CheckResults.SafetyFailureCode]
                        break
                else:
                    result[CheckResults.Integrity] = smart_values_integrity_result[CheckResults.Integrity]
                    result[CheckResults.IntegrityFailureCode] = smart_values_integrity_result[CheckResults.IntegrityFailureCode]
        break
    return result
def directly_calculable(value):
    if any(isinstance(value, cls) for cls in [Decimal, StandardFinancialUnit]):
        return True
def verify_smart_values_integrity(value_a, value_b, operation):
    failure_code = None
    integrity = True
    while integrity:
        if not isinstance(operation, InterValuesOperation):
            failure_code = f"Operation is not of InterValuesOperation class: {operation}"
            integrity = False
        for a_value in [value_a, value_b]:
            if isinstance(a_value, dict):
                smart_values_result = verify_smart_values_integrity(a_value.get(Values.SmartValueA), a_value.get(Values.SmartValueB), a_value.get(Values.InterValuesOperation))
                if not smart_values_result[CheckResults.Integrity]:
                    failure_code = smart_values_result[CheckResults.IntegrityFailureCode]
                    integrity = False
            else:
                if not valid_direct_smart_value(a_value):
                    failure_code = f"Invalid direct smart value: {a_value}"
                    integrity = False
        break
    result = {
        CheckResults.Integrity: integrity,
        CheckResults.IntegrityFailureCode: failure_code,
    }
    return result
def valid_direct_smart_value(value):
    if any(isinstance(value, cls) for cls in [Decimal, StandardFinancialUnit, VPerson]):
        return True
def verify_smart_values_safety(value_a, value_b, operation):
    safety_failure_code = ""
    ultra_safety = True
    safety = True
    for a_value in [value_a, value_b]:
        if directly_calculable(a_value) and a_value <= Decimal("0"):
            safety_failure_code = f"A negative value is involved: {a_value}"
            ultra_safety = False
            safety = False
    while safety:
        if operation == InterValuesOperation.Division:
            if directly_calculable(value_b):
                if value_b == Decimal("0"):
                    safety_failure_code = f"Zero division expected: {value_a} divided by {value_b}"
                    ultra_safety = False
                    safety = False
            else:
                ultra_safety = False
        if operation == InterValuesOperation.Subtraction:
            if directly_calculable(value_a) and directly_calculable(value_b):
                if value_a < value_b:
                    safety_failure_code= f"A negative value is involved: Subtrahend is greater than minuend: {value_a} - {value_b}"
                    ultra_safety = False
                    safety = False
            elif directly_calculable(value_a):
                if not value_a > Decimal("0"):
                    safety_failure_code = f"A probable negative value is involved: Subtrahend is probably greater than minuend: {value_a} - {value_b}"
                    ultra_safety = False
                    safety = False
            elif directly_calculable(value_b):
                if value_b > Decimal("0"):
                    safety_failure_code = f"Operation might produce negative value: {value_a} - {value_b}, use floor subtraction for safety."
                    ultra_safety = False
        break
    result = {
        CheckResults.Safety: safety,
        CheckResults.UltraSafety: ultra_safety,
        CheckResults.SafetyFailureCode: safety_failure_code,
    }
    return result
def verify_tax_benefits(tax_benefits:dict, break_for_ultra_safety=False):
    result = {
        CheckResults.Integrity: True,
        CheckResults.IntegrityFailureCode: None,
        CheckResults.Safety: True,
        CheckResults.UltraSafety: True,
        CheckResults.SafetyFailureCode: None,
    }
    integrity = True
    while integrity:
        deductions = tax_benefits.get(TaxBenefits.Deduction)
        if isinstance(deductions, dict):
            standard_deduction = deductions.get(Deduction.StandardDeduction)
            standard_deduction_verification_result = verify_standard_deduction(standard_deduction)
            if not standard_deduction_verification_result[CheckResults.Integrity]:
                result[CheckResults.IntegrityFailureCode] = standard_deduction_verification_result[CheckResults.IntegrityFailureCode]
                integrity = False
            itemization = deductions.get(Deduction.Itemization)
            itemization_verification_result = verify_items(itemization, break_for_ultra_safety)
            if not itemization_verification_result[CheckResults.Integrity]:
                result = itemization_verification_result
                integrity = False
        else:
            result[CheckResults.IntegrityFailureCode] = f"Deduction is not a dictionary, instead {type(deductions)}"
            integrity = False
        exemption = tax_benefits.get(TaxBenefits.Exemption)
        exemption_verification_result = verify_exemption(exemption)
        if not exemption_verification_result[CheckResults.Integrity]:
            result[CheckResults.IntegrityFailureCode] = exemption_verification_result[CheckResults.IntegrityFailureCode]
            integrity = False
        break
    result[CheckResults.Integrity] = integrity
    return result
def verify_items(items:dict, break_for_ultra_safety=False):
    result = {
        CheckResults.Integrity: True,
        CheckResults.IntegrityFailureCode: None,
        CheckResults.Safety: True,
        CheckResults.UltraSafety: True,
        CheckResults.SafetyFailureCode: None,
    }
    feeders = []
    receivers = []
    integrity = True
    while integrity:
        for item_name ,item_data in items.items():
            itemization_type = item_data.get(ItemItemization.ItemItemizationType, {})
            if isinstance(itemization_type, ItemItemizationType):
                if itemization_type == ItemItemizationType.Feeder:
                    receiver_code = item_data.get(ItemItemization.ReceiverCode)
                    if isinstance(receiver_code, str):
                        if receiver_code not in feeders:
                            feeders.append(receiver_code)
                    else:
                        result[
                            CheckResults.IntegrityFailureCode] = f'''Receiver code "{receiver_code}" is not a string.'''
                        integrity = False
                        break
                    feeder_specific_code = item_data.get(ItemItemization.FeederSpecificCode)
                    if not isinstance(feeder_specific_code, int) and not isinstance(feeder_specific_code, str):
                        result[
                            CheckResults.IntegrityFailureCode] = f"Invalid Feeder specific code: {feeder_specific_code}"
                        integrity = False
                        break
                    deductible_source = item_data.get(ItemItemization.DeductibleValue)
                    if not isinstance(deductible_source, VPerson):
                        result[
                            CheckResults.IntegrityFailureCode] = f'''Deductible "{deductible_source}" is not of VPerson class.'''
                        integrity = False
                        break
                elif itemization_type == ItemItemizationType.Receiver:
                    receiving_code = item_data.get(ItemItemization.ReceivingCode)
                    if isinstance(receiving_code, str):
                        if receiving_code not in receivers:
                            receivers.append(receiving_code)
                    else:
                        result[
                            CheckResults.IntegrityFailureCode] = f'''Receiving code "{receiving_code}" is not a string.'''
                        integrity = False
                        break
            else:
                result[CheckResults.IntegrityFailureCode] = f'''Itemization type is not of ItemItemizationType class'''
                integrity = False
                break
            count_of_caps_applied = item_data.get(ItemItemization.CapsAppliedCount)
            caps_applied = item_data.get(ItemItemization.ItemizationCaps, {})
            if not isinstance(count_of_caps_applied, int):
                result[CheckResults.IntegrityFailureCode] = f'''Caps applied count({count_of_caps_applied}) is not an integer'''
                integrity = False
                break
            if not isinstance(caps_applied, dict):
                result[CheckResults.IntegrityFailureCode] = f'''Caps must be a dictionary, instead {type(caps_applied)}.'''
                integrity = False
                break
            if count_of_caps_applied != len(caps_applied):
                result[CheckResults.IntegrityFailureCode] = f'''Alleged count of caps is not equal to len of caps. {count_of_caps_applied} != {len(caps_applied)}'''
                integrity = False
                break
            for cap_number, cap_data in caps_applied.items():
                cap_verification_result = verify_itemization_cap(cap_data, break_for_ultra_safety)
                if not cap_verification_result[CheckResults.Integrity]:
                    result = cap_verification_result
                    result[CheckResults.IntegrityFailureCode] = f"Item name {item_name}: Cap number {cap_number}: " + result[CheckResults.IntegrityFailureCode]
                    integrity = False
                    break
            carry_forward = item_data.get(ItemItemization.CarryForwardTimeLimit)
            if carry_forward:
                if not isinstance(carry_forward, relativedelta) and not isinstance(carry_forward, datetime.datetime):
                    result[CheckResults.IntegrityFailureCode] = f"Carry-forward is not of relativedelta or datetime class, instead {type(carry_forward)}"
                    integrity = False
                    break
        if integrity:
            if feeders != receivers:
                result[
                    CheckResults.IntegrityFailureCode] = f"Feeders-receivers codes mismatch: Feeding codes: {feeders}, Receivers {receivers}"
                integrity = False
                break
        break
    result[CheckResults.Integrity] = integrity
    return result
def verify_itemization_cap(cap:dict, break_for_ultra_safety=False):
    result = {
        CheckResults.Integrity: True,
        CheckResults.IntegrityFailureCode: None,
        CheckResults.Safety: True,
        CheckResults.UltraSafety: True,
        CheckResults.SafetyFailureCode: None,
    }
    integrity = True
    while integrity:
        limit_type = cap.get(ItemItemization.LimitType)
        if not isinstance(limit_type, LimitType):
            result[CheckResults.IntegrityFailureCode] = "Itemization Cap Error: Limit type is not of LimitType class."
            integrity = False
        cap_type = cap.get(ItemItemization.ItemizationCapType)
        if isinstance(cap_type, ItemizationCapType):
            if cap_type == ItemizationCapType.FixedCap:
                the_fixed_cap = cap.get(Values.FixedValue)
                if the_fixed_cap:
                    if not isinstance(the_fixed_cap, StandardFinancialUnit):
                        result[CheckResults.IntegrityFailureCode] = "Itemization Cap Error: Fixed cap is not StandardFinancialUnit class."
                        integrity = False
                        break
                else:
                    result[CheckResults.IntegrityFailureCode] = "Itemization Cap Error: Fixed Cap is missing"
                    integrity = False
                    break
            elif cap_type == ItemizationCapType.DynamicCap:
                one_dynamic = cap.get(Values.DynamicValue)
                if one_dynamic:
                    if not isinstance(one_dynamic, StandardFinancialUnit) and not isinstance(one_dynamic, VPerson):
                        result[
                            CheckResults.IntegrityFailureCode] = "Itemization Cap Error: Dynamic cap is not StandardFinancialUnit class."
                        integrity = False
                        break
                else:
                    smart_a = cap.get(Values.SmartValueA)
                    smart_b = cap.get(Values.SmartValueB)
                    operation = cap.get(Values.InterValuesOperation)
                    integrity_verification_result = verify_smart_values_integrity(smart_a, smart_b, operation)
                    if integrity_verification_result[CheckResults.Integrity]:
                        safety_verification_result = verify_smart_values_safety(smart_a, smart_b, operation)
                        if not safety_verification_result[CheckResults.Safety]:
                            result[CheckResults.Safety] = False
                            result[CheckResults.UltraSafety] = False
                            result[CheckResults.SafetyFailureCode] = safety_verification_result[CheckResults.SafetyFailureCode]
                            result[CheckResults.IntegrityFailureCode] = "Itemization Cap Error: Smart values safety error."
                            integrity = False
                            break
                        elif not safety_verification_result[CheckResults.UltraSafety] and break_for_ultra_safety:
                            result[CheckResults.UltraSafety] = False
                            result[
                                CheckResults.IntegrityFailureCode] = "Itemization Cap Error: Smart values ultra safety error."
                            integrity = False
                            break
                    else:
                        result[
                            CheckResults.IntegrityFailureCode] = "Itemization Cap Error: Smart values integrity error."
                        integrity = False
                        break
        else:
            result[
                CheckResults.IntegrityFailureCode] = "Itemization Cap Error: Itemization cape type is not CapType class."
            integrity = False
            break
        break
    result[CheckResults.Integrity] = integrity
    return result
def verify_standard_deduction(standard_deduction:dict):
    result = {
        CheckResults.Integrity: True,
        CheckResults.IntegrityFailureCode: None,
    }
    if isinstance(standard_deduction, dict):
        for status in [MaritalStatus.Single, MaritalStatus.MarriedJoint, MaritalStatus.MarriedNonJoint]:
            if result[CheckResults.Integrity]:
                deduction_for_status = standard_deduction.get(status)
                if deduction_for_status:
                    if not isinstance(deduction_for_status, Money):
                        result[CheckResults.IntegrityFailureCode] = f"{status} standard deduction is not of Money class, instead {type(deduction_for_status)}"
                        result[CheckResults.Integrity] = False
                else:
                    result[CheckResults.IntegrityFailureCode] = f"{status} standard deduction is missing."
                    result[CheckResults.Integrity] = False

    else:
        result[CheckResults.IntegrityFailureCode] = f"Standard deductions is not a dictionary, instead {type(standard_deduction)}"
        result[CheckResults.Integrity] = False
    return result
def verify_exemption(exemption:dict):
    result = {
        CheckResults.Integrity: True,
        CheckResults.IntegrityFailureCode: None,
    }
    if isinstance(exemption, dict):
        for status in [MaritalStatus.Single, MaritalStatus.MarriedJoint, MaritalStatus.MarriedNonJoint]:
            if result[CheckResults.Integrity]:
                exemption_for_status = exemption.get(status)
                if exemption_for_status:
                    if not isinstance(exemption_for_status, Money):
                        result[
                            CheckResults.IntegrityFailureCode] = f"{status} exemption is not of Money class, instead {type(exemption_for_status)}"
                        result[CheckResults.Integrity] = False
                else:
                    result[CheckResults.IntegrityFailureCode] = f"{status} exemption is missing."
                    result[CheckResults.Integrity] = False
    else:
        result[
            CheckResults.IntegrityFailureCode] = f"Exemption is not a dictionary, instead {type(exemption)}"
        result[CheckResults.Integrity] = False
    return result
def vperson_to_person_attribute(vperson, person:Person, converter):
    if isinstance(vperson, VPerson):
        if vperson in converter:
            attribute_name = converter[vperson]["attribute name"]
            if hasattr(person, attribute_name):
                return getattr(person, attribute_name)
            else:
                return converter[vperson]["default value"]
def vperson_dictionary_to_person_attribute(variables:dict, person:Person, converter):
    for key, its_value in variables.items():
        if isinstance(its_value, VPerson):
            variables[key] = vperson_to_person_attribute(its_value, person, converter)
        elif isinstance(its_value, dict):
            variables[key] = vperson_dictionary_to_person_attribute(its_value, person, converter)
    return variables
def apply_raw_deductibles(dictionary:dict, person:Person, converter):
    for key, its_value in dictionary.items():
        if isinstance(its_value, dict):
            apply_raw_deductibles(its_value, person, converter)
        elif key == ItemItemization.DeductibleValue:
            dictionary[key] = vperson_to_person_attribute(its_value, person, converter)
    return dictionary
def calculate_pre_base_agi_itemization(items:dict, person:Person, converter=None):
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
                receiver_code = item[ItemItemization.ReceiverCode]
                feeder_specific_code = item[ItemItemization.FeederSpecificCode]
                if ledger.get(receiver_code):
                    ledger[receiver_code][feeder_specific_code] = calculate_item_directly(item, person, converter)
                else:
                    ledger[receiver_code] = {}
                    ledger[receiver_code][feeder_specific_code] = calculate_item_directly(item, person, converter)
    for item in items.values():
        if item[ItemItemization.ItemItemizationType] == ItemItemizationType.Receiver:
            if not item[ItemItemization.HaveBaseAGIDependentFeeders]:
                receiving_code = item[ItemItemization.ReceivingCode]
                total_received = sum(ledger[receiving_code].values(), StandardFinancialUnit())
                accumulated_from_receivers += calculate_item_directly(item, person, converter, True, total_received)
    return accumulated_directs+accumulated_from_receivers
def calculate_post_base_agi_itemization(items:dict, person:Person, converter):
    accumulated_directs = Money()
    accumulated_from_receivers = Money()
    ledger = {}
    for item in items.values():
        if item[ItemItemization.ItemItemizationType] == ItemItemizationType.Direct:
            accumulated_directs += calculate_item_directly(item, person, converter)
        elif item[ItemItemization.ItemItemizationType] == ItemItemizationType.Feeder:
            receiver_code = item[ItemItemization.ReceiverCode]
            feeder_specific_code = item[ItemItemization.FeederSpecificCode]
            if ledger.get(receiver_code):
                ledger[receiver_code][feeder_specific_code] = calculate_item_directly(item, person, converter)
            else:
                ledger[receiver_code] = {}
                ledger[receiver_code][feeder_specific_code] = calculate_item_directly(item, person, converter)
    for item in items.values():
        if item[ItemItemization.ItemItemizationType] == ItemItemizationType.Receiver:
            receiving_code = item[ItemItemization.ReceivingCode]
            total_received = sum(ledger[receiving_code].values(), StandardFinancialUnit())
            accumulated_from_receivers += calculate_item_directly(item, person, converter, True, total_received)
    return accumulated_directs + accumulated_from_receivers
def calculate_item_directly(item:dict, person:Person, converter, receiver=False, total_received=None):
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
def calculate_smart_values(a, b, operation, person:Person, converter):
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
def calculate_tax_benefits(person:Person, variables, converter):
    standard_deduction = calculate_tax_benefits_when_standardized(person, variables)
    itemized = calculate_post_base_agi_itemization(variables,person ,converter)
    preference = person.preference[Preference.TaxPreference][TaxPreference.PreferredDeductionType]
    if preference == PreferredDeductionType.PreferStandardized:
        return standard_deduction, Deduction.StandardDeduction
    elif preference == PreferredDeductionType.PreferItemized:
        return itemized, Deduction.ItemizedDeduction
    elif preference == PreferredDeductionType.PreferAuto:
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
def calculate_tax(tax:dict, person:Person, converter:dict):
    tax_value = Tax()
    taxation_type = tax[TaxVariables.Configurations][Configurations.TaxationType]
    if taxation_type == TaxationType.ProgressiveRate or taxation_type == TaxationType.FlatRate:
        tax_base = tax[TaxVariables.Configurations][Configurations.TaxBase]
        agi = vperson_to_person_attribute(tax_base, person, converter)
        if taxation_type == TaxationType.ProgressiveRate:
            brackets = tax[TaxVariables.BracketCeilings][person.status]
            highest_bracket = tax[TaxVariables.Configurations][Configurations.HighestBracketCeiling]
            bracket = find_bracket(agi, brackets, highest_bracket)
            rates = tax[TaxVariables.Rates]
            tax_value = apply_rate(brackets, bracket, rates, agi)
        else:
            flat_rate = tax[TaxVariables.Configurations][Configurations.TheFlatRate]
            tax_value = agi * flat_rate
    elif taxation_type == TaxationType.FixedAmount:
        tax_value = tax[TaxVariables.Configurations][Configurations.TheFixedAmount]
    if tax[TaxVariables.Configurations][Configurations.HaveCap]:
        caps = tax[TaxVariables.TaxCaps]
        tax_value = adjust_tax_value_for_its_caps(tax_value, caps, person, converter)
    return tax_value
def find_bracket(agi, brackets:dict, highest_bracket:int):
    bracket = highest_bracket
    while bracket > 1:
        if agi > brackets[bracket-1]:
            break
        else:
            bracket -= 1
    return bracket
def apply_rate(brackets ,bracket, rates, agi):
    accumulated_tax = Tax(Decimal("0"))
    order = bracket
    while order > 1:
        portion_to_tax = (agi-brackets[order-1])
        # print(f'''Portion: {portion_to_tax}, rate:{rates[order]}, added tax:{portion_to_tax*rates[order]}''')
        accumulated_tax += portion_to_tax*rates[order]
        agi = brackets[order-1]
        order-=1
    accumulated_tax += agi*rates[order]
    return accumulated_tax
def process_taxes(taxes:dict, person:Person, converter:dict):
    taxes_output = {}
    for tax in taxes.values():
        tax_name = str(tax[TaxVariables.Configurations][Configurations.TaxName]).replace("StandardTaxName.", "")
        tax_value = calculate_tax(tax, person, converter)
        taxes_output[tax_name] = tax_value
    return taxes_output
def calculate_tax_cap(cap:dict, person, converter):
    if cap[TaxCap.TaxCapType] == TaxCapType.TaxDynamicCap:
        if cap.get(Values.DynamicValue):
            cap_value =  vperson_to_person_attribute(cap[Values.DynamicValue], person, converter)
        else:
            cap_value = calculate_smart_values(cap[Values.SmartValueA], cap[Values.SmartValueB], cap[Values.InterValuesOperation], person, converter)
    else:
        cap_value = cap[Values.FixedValue]
    capping_method = cap[TaxCap.TaxLimitType]
    return cap_value, capping_method
def calculate_tax_caps(caps:dict, person, converter):
    upper_limits = []
    lower_limits = []
    for cap in caps.values():
        cap_result = calculate_tax_cap(cap, person, converter)
        if cap_result[1] == TaxLimitType.UpperLimitTaxCap:
            upper_limits.append(cap_result[0])
        elif cap_result[1] == TaxLimitType.LowerLimitTaxCap:
            lower_limits.append(cap_result[0])
    if not upper_limits:
        upper_limits.append(Money(Decimal("Infinity")))
    if not lower_limits:
        lower_limits.append(Money())
    return upper_limits, lower_limits
def adjust_tax_value_for_its_caps(tax_value, caps:dict, person:Person, converter:dict):
    processed_caps = calculate_tax_caps(caps, person, converter)
    upper_limits = processed_caps[0]
    lower_limits = processed_caps[1]
    smallest_upper_limit = min(upper_limits)
    greatest_lower_limit = max(lower_limits)
    if tax_value >= greatest_lower_limit:
        tax_value -= greatest_lower_limit
        tax_value = min(tax_value, smallest_upper_limit)
    else:
        tax_value = Tax()
    return tax_value

if __name__ == '__main__':
    p = Person()
    p.status = MaritalStatus.Single
    p.income = Money(Decimal("500000000"))
    setattr(p, "medical_expenses", Liability(Decimal("6000000")))  # $60,000
    setattr(p, "mortgage_interest", Liability(Decimal("200000000")))  # $2,000,000
    setattr(p, "property_taxes", Liability(Decimal("4000000")))  # $40,000
    setattr(p, "SALT", Money(Decimal("5000000")))  # $50,000
    setattr(p, "public_cash_donations", Money(Decimal("25000000")))  # $250,000
    setattr(p, "private_cash_donations", Money(Decimal("10000000")))  # $100,000
    setattr(p, "investment_interest_expense", Liability(Decimal("12000000")))  # $120,000
    setattr(p, "total_debt_based_investment_earnings", Money(Decimal("8000000")))  # $80,000 (caps investment deduction)
    # print(p.federal_final_agi)
    # noinspection PyTypeChecker
    # print(nested_dictionary_reader(process_taxes(standard_variables[Variables.Taxes], p, vperson_to_person_attributes)))
    p.state = State.California
    # print(verify_taxes_integrity(random_taxes))
    # print(p.state_final_agi)
    # p.state = State.NewYork
    # standard_user_preference[Preference.TaxPreference][TaxPreference.PreferredDeductionType][Jurisdiction.State] = PreferredDeductionType.PreferStandardized
    # print(p.federal_final_agi)
    # print(p.state_deductions)
    # noinspection PyTypeChecker
    # print(nested_dictionary_reader(my_items[Itemization.TotalDonations]))
    # print(nested_dictionary_reader(verify_items(my_items, True)))
    # print(nested_dictionary_reader(verify_variables_viability_and_integrity(standard_variables)))
    # print(getattr(p, "federal_final_agi"))
    from decimal import Decimal

    a_result = verify_variables_viability_and_integrity(new_york_variables, True)
    print(nested_dictionary_reader(a_result))

    test_smart_values = {
        Values.SmartValueA: {
            Values.SmartValueA: {
                Values.SmartValueA: Decimal(5),
                Values.SmartValueB: {
                    Values.SmartValueA: Decimal(2),
                    Values.SmartValueB: Decimal(3),
                    Values.InterValuesOperation: InterValuesOperation.Multiplication
                },
                Values.InterValuesOperation: InterValuesOperation.Addition
            },
            Values.SmartValueB: {
                Values.SmartValueA: {
                    Values.SmartValueA: {
                        Values.SmartValueA: Decimal(10),
                        Values.SmartValueB: Decimal(2),
                        Values.InterValuesOperation: InterValuesOperation.Multiplication
                    },
                    Values.SmartValueB: {
                        Values.SmartValueA: Decimal(4),
                        Values.SmartValueB: Decimal(2),
                        Values.InterValuesOperation: InterValuesOperation.Subtraction
                    },
                    Values.InterValuesOperation: InterValuesOperation.Addition
                },
                Values.SmartValueB: {
                    Values.SmartValueA: Decimal(8),
                    Values.SmartValueB: {
                        Values.SmartValueA: Decimal(3),
                        Values.SmartValueB: Decimal(1),
                        Values.InterValuesOperation: InterValuesOperation.Addition
                    },
                    Values.InterValuesOperation: InterValuesOperation.Multiplication
                },
                Values.InterValuesOperation: InterValuesOperation.Subtraction
            },
            Values.InterValuesOperation: InterValuesOperation.Multiplication
        },
        Values.SmartValueB: {
            Values.SmartValueA: {
                Values.SmartValueA: {
                    Values.SmartValueA: Decimal(6),
                    Values.SmartValueB: Decimal(2),
                    Values.InterValuesOperation: InterValuesOperation.Division
                },
                Values.SmartValueB: {
                    Values.SmartValueA: {
                        Values.SmartValueA: Decimal(4),
                        Values.SmartValueB: Decimal(2),
                        Values.InterValuesOperation: InterValuesOperation.Multiplication
                    },
                    Values.SmartValueB: {
                        Values.SmartValueA: Decimal(3),
                        Values.SmartValueB: Decimal(1),
                        Values.InterValuesOperation: InterValuesOperation.Subtraction
                    },
                    Values.InterValuesOperation: InterValuesOperation.FloorSubtraction
                },
                Values.InterValuesOperation: InterValuesOperation.Addition
            },
            Values.SmartValueB: {
                Values.SmartValueA: {
                    Values.SmartValueA: Decimal(7),
                    Values.SmartValueB: {
                        Values.SmartValueA: Decimal(2),
                        Values.SmartValueB: Decimal(5),
                        Values.InterValuesOperation: InterValuesOperation.Multiplication
                    },
                    Values.InterValuesOperation: InterValuesOperation.Subtraction
                },
                Values.SmartValueB: {
                    Values.SmartValueA: Decimal(9),
                    Values.SmartValueB: {
                        Values.SmartValueA: Decimal(3),
                        Values.SmartValueB: Decimal(1),
                        Values.InterValuesOperation: InterValuesOperation.Addition
                    },
                    Values.InterValuesOperation: InterValuesOperation.Division
                },
                Values.InterValuesOperation: InterValuesOperation.Multiplication
            },
            Values.InterValuesOperation: InterValuesOperation.Addition
        },
        Values.InterValuesOperation: InterValuesOperation.Subtraction
    }
    # a_damn_result = verify_taxes_integrity(random_taxes)
    # print(a_damn_result)

    # print(calculate_smart_values(test_smart_values[Values.SmartValueA], test_smart_values[Values.SmartValueB], test_smart_values[Values.InterValuesOperation], p, vperson_to_person_attributes))
    # print(verify_smart_values_integrity(test_smart_values[Values.SmartValueA], test_smart_values[Values.SmartValueB], test_smart_values[Values.InterValuesOperation]))

    # print(nested_dictionary_reader(process_taxes(some_taxes, p, vperson_to_person_attributes)))
    # import  json
    # with open("StandardVariablesParsed.json", "w") as f:
    #     # noinspection PyTypeChecker
    #     json.dump(standard_variables, f, default=smart_serializer)
    # with open("FurtherCorruptedVariables.json", "r") as f:
    #     loaded_raw = json.load(f)
    #
    # restored_back = restore_objects(loaded_raw, all_enums)
    # print(nested_dictionary_reader(verify_variables_viability_and_integrity(restored_back)))
