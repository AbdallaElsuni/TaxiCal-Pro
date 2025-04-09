__all__ = [
    "Currency", "PaymentStatus", "MaritalStatus", "State", "Variables",
    "Configurations", "TaxBaseType", "VariablesType", "TaxBase", "TaxationType",
    "TaxVariables", "NameType", "TaxCap", "TaxLimitType", "TaxCapType",
    "TaxBenefits", "Deduction", "VerifierConfigurations", "AdjustedIncomeSource",
    "Itemization", "ItemItemization", "ItemItemizationType", "ItemizationCapType",
    "ItemizationPhase", "Values", "VPerson", "InterValuesOperation", "LimitType",
    "StandardTaxName", "LocalIndex", "AGIType", "Preference", "SafetyPreference",
    "TaxPreference", "PreferredDeductionType", "Jurisdiction", "CheckResults",
    "Requirement", "ComparisonOperator", "RequirementsConfiguration",
    "RequirementsToMeet", "CustomEnum", "all_enums", "CarryOverRules", "CarryOverOffsetTarget",
    "CarryOverOffsetLimitType", "DynamicContextBasedValue", "TaxCreditData", "ValueType",
    "StandardTaxCreditName", "OffsetTargetType"
]

from enum import Enum
class CustomEnum(Enum):
    def __str__(self):
        return self.name
class Currency(str, CustomEnum):
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
class PaymentStatus(str, CustomEnum):
    Paid = "Paid"
    UnPaid = "UnPaid"
    Capitalized = "Capitalized"
    NotSpecified = "NotSpecified"
    PartiallyPaid = "PartiallyPaid"
    InterestOnly = "InterestOnly"
    def __str__(self):
        return self.name
class MaritalStatus(str, CustomEnum):
    Single = "Single"
    MarriedNonJoint = "MarriedNonJoint"
    MarriedJoint = "MarriedJoint"
    UnSpecified = "UnSpecified"
    def __str__(self):
        return self.name
class State(str, CustomEnum):
    CityVariablesIndex = "CityVariablesIndex"
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
class Variables(str, CustomEnum):
    Configurations = "Configurations"
    Taxes = "Taxes"
    TaxBenefits = "TaxBenefits"
class Configurations(str, CustomEnum):
    VariablesType = "VariablesType"
    TaxNameType = "TaxNameType"
    TaxName = "TaxName"
    TaxationType = "TaxationType"
    TaxBase = "TaxBase"
    TaxBaseType = "TaxBaseType"
    VerifierConfigurations = "VerifierConfigurations"
    AdjustedIncomeSource = "AdjustedIncomeSource"
    LastUpdated = "LastUpdated"
    HighestBracketCeiling = "HighestBracketCeiling"
    TheFlatRate = "TheFlatRate"
    TheFixedAmount = "TheFixedAmount"
    HaveCap = "HaveCap"
    HaveRequirements = "HaveRequirements"
    TaxCreditNameType = "TaxCreditNameType"
    TaxCreditName = "TaxCreditName"
    TaxCreditValue = "TaxCreditValue"
    TaxCreditValueType = "TaxCreditValueType"
class TaxBaseType(str, CustomEnum):
    VPersonBase = "VPersonBase"
    CustomBase = "CustomBase"
class VariablesType(str, CustomEnum):
    FederalVariables = "FederalVariables"
    StateVariables = "StateVariables"
    CityVariables = "CityVariables"
    LocalVariables = "LocalVariables"
    CustomVariables = "CustomVariables"
class TaxBase(str,CustomEnum):
    CustomBase = "CustomBase"
class TaxationType(str, CustomEnum):
    ProgressiveRate = "ProgressiveRate"
    FlatRate = "FlatRate"
    FixedAmount = "FixedAmount"
class TaxVariables(str, CustomEnum):
    TaxConfigurations = "TaxConfigurations"
    BracketCeilings = "BracketCeilings"
    Rates = "Rates"
    OtherTaxes = "OtherTaxes"
    TaxBenefits = "TaxBenefits"
    TaxCaps = "TaxCaps"
    TaxRequirements = "TaxRequirements"
class NameType(str, CustomEnum):
    StandardName = "StandardName"
    CustomName = "CustomName"
class TaxCap(str, CustomEnum):
    TaxLimitType = "TaxLimitType"
    TaxCapType = "TaxCapType"
class TaxLimitType(str, CustomEnum):
    UpperLimitTaxCap = "UpperLimitTaxCap"
    LowerLimitTaxCap = "LowerLimitTaxCap"
class TaxCapType(str, CustomEnum):
    TaxFixedCap = "TaxFixedCap"
    TaxDynamicCap = "TaxDynamicCap"
class TaxBenefits(str, CustomEnum):
    Deduction = "Deduction"
    Exemption = "Exemption"
    TaxCredit = "TaxCredit"
    CarryOver = "CarryOver"
class Deduction(str, CustomEnum):
    Itemization = "Itemization"
    StandardDeduction = "StandardDeduction"
    ItemizedDeduction = "ItemizedDeduction"
class VerifierConfigurations(str, CustomEnum):
    RequiredVerifierVersion = "RequiredVerifierVersion"
    SupportsForwardCompatibility = "SupportsForwardCompatibility"
    SupportsBackwardCompatibility = "SupportsBackwardCompatibility"
class AdjustedIncomeSource(str, CustomEnum):
    FromState = "FromState"
    FromFederal = "FromFederal"
    FromCity = "FromCity"
    FromLocal = "FromLocal"
    FromTaxSpecificTaxBenefits = "FromTaxSpecificTaxBenefits"
class Itemization(str, CustomEnum):
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
    CharitableContributions = "CharitableContributions"
class ItemItemization(str, CustomEnum):
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
    FeederSpecificCode = "FeederSpecificCode"
    CarryOverSetOfRules = "CarryOverSetOfRules"
class ItemItemizationType(str, CustomEnum):
    Direct = "Direct"
    Feeder = "Feeder"
    Receiver = "Receiver"
class ItemizationCapType(str, CustomEnum):
    FixedCap = "FixedCap"
    DynamicCap = "DynamicCap"
class ItemizationPhase(str, CustomEnum):
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
class Values(str, CustomEnum):
    DynamicValue = "DynamicValue"
    FixedValue = "FixedValue"
    SmartValueA = "SmartValueA"
    SmartValueB = "SmartValueB"
    InterValuesOperation = "InterValuesOperation"
class VPerson(str, CustomEnum):
    VStatus = "VStatus"
    VState = 'VState'
    VCity = "VCity"
    VPreference = "VPreference"
    VVariablesIndex = "VVariablesIndex"
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
    VOwnedVehiclesCount = "VOwnedVehiclesCount"
    VOwnedVehiclesPrice = "VOwnedVehiclesPrice"
    VStandardTax = "VStandardTax"

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

class InterValuesOperation(str, CustomEnum):
    Addition = "Addition"
    Subtraction = "Subtraction"
    Multiplication = "Multiplication"
    Division = "Division"
    FloorSubtraction = "FloorSubtraction"
    ReturnTheGreaterValue = "ReturnTheGreaterValue"
    ReturnTheLesserValue = "ReturnTheLesserValue"
class LimitType(str, CustomEnum):
    UpperLimit = "UpperLimit"
    LowerLimit = "LowerLimit"
class StandardTaxName(str, CustomEnum):
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
class LocalIndex(str, CustomEnum):
    FederalVariablesIndex = "FederalVariablesIndex"
    StatesVariablesIndex = "StatesVariablesIndex"
    CitiesVariablesIndex = "CitiesVariablesIndex"
    MunicipalitiesVariablesIndex = "MunicipalitiesVariablesIndex"
class AGIType(str, CustomEnum):
    FederalAGI = "FederalAGI"
    StateAGI = "StateAGI"
    CityAGI = "CityAGI"
    CustomAGI = "CustomAGI"
class Preference(str, CustomEnum):
    TaxPreference = "TaxPreference"
    SafetyPreference = "SafetyPreference"
class SafetyPreference(str, CustomEnum):
    PreferFollowingUltraSafety = "PreferFollowingUltraSafety"
    PreferFollowingSafety = "PreferFollowingSafety"
    PreferIgnoringSafety = "PreferIgnoringSafety"
    AlertForSafety = "AlertForSafety"
class TaxPreference(str, CustomEnum):
    PreferredDeductionType = "PreferredDeductionType"
class PreferredDeductionType(str, CustomEnum):
    PreferStandardized = "PreferStandardized"
    PreferItemized = "PreferItemized"
    PreferAuto = "PreferAuto"
class Jurisdiction(str, CustomEnum):
    Federal = "Federal"
    State = "State"
    City = "City"
    Local = "Local"
    County = "County"
    Municipal = "Municipal"
    GlobalSettings = "GlobalSettings"
class CheckResults(str, CustomEnum):
    ViabilityForChecking = "ViabilityForChecking"
    Integrity = "Integrity"
    IntegrityFailureCode = "IntegrityFailureCode"
    Safety = "Safety"
    UltraSafety = "UltraSafety"
    SafetyFailureCode = "SafetyFailureCode"
class Requirement(str, CustomEnum):
    ValueInQuestion = "ValueInQuestion"
    ComparisonValue = "ComparisonValue"
    ComparisonOperator = "ComparisonOperator"
    RequirementsConfiguration = "RequirementsConfiguration"
class ComparisonOperator(str, CustomEnum):
    Equal = "Equal"
    NotEqual = "NotEqual"
    GreaterThan = "GreaterThan"
    LessThan = "LessThan"
    GreaterOrEqual = "GreaterOrEqual"
    LessOrEqual = "LessOrEqual"
class RequirementsConfiguration(str, CustomEnum):
    RequirementsToMeet = "RequirementsToMeet"
    SpecifiedRequirements = "SpecifiedRequirements"
    SpecifiedRequirementsCount = "SpecifiedRequirementsCount"
    RequirementNote = "RequirementNote"
class RequirementsToMeet(str, CustomEnum):
    MustMeetAll = "MustMeetAll"
    MustMeetAny = "MustMeetAny"
    MustMeetAnyOf = "MustMeetAnyOf"
    MustMeetSpecificCount = "MustMeetSpecificCount"
class CarryOverRules(str, CustomEnum):
    OffsetTargets = "OffsetTargets"
    HaveUseItOrLoseItAnnualAllocation = "HaveUseItOrLoseItAnnualAllocation"
    AnnualAllocation = "AnnualAllocation"
    OneTimeUse = "OneTimeUse"
class CarryOverOffsetTarget(str, CustomEnum):
    OffsetTargetType = "OffsetTargetType"
    OffsetTarget = "OffsetTarget"
    OffsetLimitType = "OffsetLimitType"
    OffsetLimit = "OffsetLimit"
class OffsetTargetType(str, CustomEnum):
    VPerson = "VPerson"
    StandardTax = "StandardTax"
    CustomTax = "CustomTax"
    CustomPersonAttribute = "CustomPersonAttribute"
class CarryOverOffsetLimitType (str, CustomEnum):
    DynamicOffsetLimit = "DynamicOffsetLimit"
    FixedOffsetLimit = "FixedOffsetLimit"
class DynamicContextBasedValue(str, CustomEnum):
    XCarryOver = "XCarryOver"
class TaxCreditData(str, CustomEnum):
    TaxCreditRequirements = "TaxCreditRequirements"
    TaxCreditConfigurations = "TaxCreditConfigurations"
class StandardTaxCreditName(str, CustomEnum):
    EarnedIncomeTaxCredit = "EarnedIncomeTaxCredit"
    ChildTaxCredit = "ChildTaxCredit"
    AmericanOpportunityTaxCredit = "AmericanOpportunityTaxCredit"
    LifetimeLearningCredit = "LifetimeLearningCredit"
    ChildAndDependentCareCredit = "ChildAndDependentCareCredit"
    SaversCredit = "SaversCredit"
    PremiumTaxCredit = "PremiumTaxCredit"
    ForeignTaxCredit = "ForeignTaxCredit"
    ResidentialEnergyEfficientPropertyCredit = "ResidentialEnergyEfficientPropertyCredit"
    AdoptionCredit = "AdoptionCredit"
    WorkOpportunityTaxCredit = "WorkOpportunityTaxCredit"
    ResearchAndDevelopmentTaxCredit = "ResearchAndDevelopmentTaxCredit"
    DisabledAccessCredit = "DisabledAccessCredit"
    EmployerProvidedChildcareCredit = "EmployerProvidedChildcareCredit"
class ValueType(str, CustomEnum):
    FixedValue = "FixedValue"
    DynamicValue = "DynamicValue"
    SmartValue = "SmartValue"

all_enums = [
    Currency, PaymentStatus, MaritalStatus, State, Variables, Configurations,
    TaxBaseType, VariablesType, TaxBase, TaxationType, TaxVariables, NameType,
    TaxCap, TaxLimitType, TaxCapType, TaxBenefits, Deduction, VerifierConfigurations,
    AdjustedIncomeSource, Itemization, ItemItemization, ItemItemizationType,
    ItemizationCapType, ItemizationPhase, Values, VPerson, InterValuesOperation,
    LimitType, StandardTaxName, LocalIndex, AGIType, Preference, SafetyPreference,
    TaxPreference, PreferredDeductionType, Jurisdiction, CheckResults, Requirement,
    ComparisonOperator, RequirementsConfiguration, RequirementsToMeet, CustomEnum,
    CarryOverRules, CarryOverOffsetTarget, CarryOverOffsetLimitType, DynamicContextBasedValue,
    TaxCreditData, ValueType, StandardTaxCreditName, OffsetTargetType
]

if __name__ == '__main__':
    for an_enum in all_enums:
        for mem in an_enum:
            if mem.name != mem:
                print(mem)
