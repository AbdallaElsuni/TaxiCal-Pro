# TaxiCalPro

TaxiCalX is a modular and scalable tax calculation engine designed for handling **federal, state, and local taxes** efficiently. The system supports **progressive, flat, and fixed taxation** and allows for **custom tax deductions** with dynamic configurations.

## 🚀 Features
- **Fully Modular Tax Structure** – Easily add new tax jurisdictions (federal, state, city).
- **Feeder & Receiver Deduction System** – Enables flexible **AGI-based caps** for deductions.
- **Supports Standard & Custom Deductions** – `TaxNameType.StandardName` & `TaxNameType.CustomName`.
- **Dynamic Variables Indexing** – Uses `default_variables_index` for tax data management.
- **Multi-Currency Support** – Includes global currencies (`USD`, `EUR`, `JPY`, etc.).
- **Flexible Tax Brackets** – Handles progressive, flat, and fixed tax rates.
- **Automated Deduction Calculations** – Standard vs. itemized deductions.

## 📂 File Structure
```
📂 TaxiCalX
 ├── CleanCoreLogic.py    # Core tax calculation logic
 ├── StandardVariablesFormat.txt # Data structure for tax variables
 ├── Classes.py           # Enum and class definitions
```

## ⚙️ How It Works
### **1️⃣ Variables Index System**
The tax system dynamically loads variables from `default_variables_index`, which contains:
- `FederalVariablesIndex` – Federal tax configurations.
- `StatesVariablesIndex` – State-specific tax brackets, deductions.
- `CitiesVariablesIndex` – City-specific taxes.
- `MunicipalitiesVariablesIndex` – Local municipality taxes.

### **2️⃣ Feeder & Receiver Logic for Deductions**
- **Feeders** contribute deductions to a common **receiver**.
- **Receivers** apply AGI-based limits and calculate final deductions.
- Example: `PropertyTaxItemization` feeds into the `SALT` deduction cap.

### **3️⃣ Dynamic Tax Calculation**
- Standard vs. Itemized deductions **auto-selected**.
- Multi-phase deduction calculations **(pre-AGI, post-AGI processing)**.
- Uses **`calculate_tax_benefits()`** to determine the best deduction option.

## 📌 Example Usage
```python
from CleanCoreLogic import *

p = Person()
p.status = MaritalStatus.Single
p.income = Money(Decimal("500000000"))
setattr(p, "medical_expenses", Liability(Decimal("6000000")))
setattr(p, "mortgage_interest", Liability(Decimal("200000000")))
setattr(p, "property_taxes", Liability(Decimal("4000000")))

print(p.federal_deductions)
```

## 📜 License
Licensed under **MIT License** – Open-source, free to use & modify.

## 🛠️ Future Plans
- ✅ Add GUI interface
- ✅ Expand support for additional state/city tax variations
- ✅ Optimize computation performance for large datasets

---

TaxiCalX is designed for **efficiency, modularity, and accuracy**—making tax calculations easier than ever. 🚀

