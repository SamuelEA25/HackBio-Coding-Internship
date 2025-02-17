# Function Scripts for DNA Translation, Logistic Growth and Hamming Distance Determination 
## 📌 Task Overview 
Here are four Python functions for various biological computations:  

- **`dna_to_protein`**: to translate DNA sequence into protein sequence.  
- **`generate_logistic_growth_curves`**: for generating multiple logistic growth curves with variations in lag and exponential phases.  
- **`time_to_80_percent_growth`**: to determines the time needed to reach 80% of the carrying capacity.  
- **`hamming_distance`**: for calculating the Hamming distance between pairs of usernames.  

## 🛠 Requirements  
- **Python 3.x**  

## 📥 Installation  
Clone this repository to your local machine:  
```bash
git clone https://github.com/SamuelEA25/HackBio-Coding-Internship.git
```

## 🚀 Testing the Function Script

Open your command line interface and locate the file directory for ```script1```:

```bash

cd path/to/script1
```

Enter the interactive mode for Python by entering this command:

```bash

python
```

Import the script (```script1```) and manually call each functions to test them

**1️⃣ Translate DNA to Protein:**

```python

from script1 import dna_to_protein
```

```python

dna = "TCCAGATCCACAAGCCCAACTTTCAACAAA"
print("Protein sequence:", dna_to_protein(dna))
```

**2️⃣ Generate Logistic Growth Curves:**

```python

from script1 import generate_logistic_growth_curves
```

```python

growth_curves = generate_logistic_growth_curves(num_curves=10, max_time=20)
print("Generated logistic growth curves:", growth_curves[:2])
```

**3️⃣ Calculate Time to 80% of Carrying Capacity:**

```python

from script1 import time_to_80_percent_growth
```

```python
K, P, r = 1000, 10, 0.1
time_to_80 = time_to_80_percent_growth(K, P, r)
print("Time to reach 80% of carrying capacity:", time_to_80)
```

**4️⃣ Compute Hamming Distance:**

```python

from script1 import hamming_distance
```

```python

distance1 = hamming_distance("AmakaMadubuike", "AmakaMadubuike")
distance2 = hamming_distance("Mirra", "mirr9")
distance3 = hamming_distance("PreciousGift", "PreciousGift")
distance4 = hamming_distance("SamuelEA", "Samuel18")
distance5 = hamming_distance("DrIhotu89", "Cyndy8436")
distance6 = hamming_distance("Saurabh", "Saurabh")
```

```python

print("Hamming Distance Results:")
print(f"AmakaMadubuike vs AmakaMadubuike: {distance1}")
print(f"Mirra vs mirr9: {distance2}")
print(f"PreciousGift vs PreciousGift: {distance3}")
print(f"SamuelEA vs Samuel18: {distance4}")
print(f"DrIhotu89 vs Cyndy8436: {distance5}")
print(f"Saurabh vs Saurabh: {distance6}")
```

## 📌 Team Members
**👤 [SamuelEA25](https://github.com/SamuelEA25)**
**👤 [@Ace-all](https://github.com/Ace-all)**
**👤 [@mirra-09](https://github.com/mirra-09)**
**👤 [@PliciousG](https://github.com/PliciousG)**
**👤 [Drihotu](https://github.com/Drihotu)**
**👤 [Saurabh1234556](https://github.com/Saurabh1234556)**
