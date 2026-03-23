# Lab 2: Freezing Point Depression - Instructor Walkthrough

## Complete Step-by-Step Guide with Realistic Data

**Scenario:** You're completing this lab in a community college chemistry lab with equipment that's seen better days. The digital thermometers are 5+ years old, the balances work but drift occasionally, and the ice machine produces inconsistent ice. This walkthrough shows realistic results you might actually see.

---

## PRE-LAB CALCULATIONS (Complete These BEFORE Lab)

### Calculation 1: Heavy Salt (7.5 g NaCl in 50 g water)

**Given:** Molar mass NaCl = 58.44 g/mol, k_f = 1.86 °C/m, i = 2

**Step 1: Calculate moles of NaCl**
```
moles = mass ÷ molar mass
moles = 7.5 g ÷ 58.44 g/mol = 0.1283 mol
```

**Step 2: Calculate molality**
```
m = moles ÷ kg solvent
m = 0.1283 mol ÷ 0.050 kg = 2.57 m
```

**Step 3: Calculate ΔT**
```
ΔT = i × k_f × m
ΔT = 2 × 1.86 × 2.57 = 9.56 °C
```

**Step 4: Find new freezing point**
```
FP = 0°C − ΔT = 0°C − 9.56°C = −9.56°C
```

---

### Calculation 2: Premium Salt (5.0 g CaCl₂ in 50 g water)

**Given:** Molar mass CaCl₂ = 110.98 g/mol, k_f = 1.86 °C/m, i = 3

**Step 1: Calculate moles of CaCl₂**
```
moles = mass ÷ molar mass
moles = 5.0 g ÷ 110.98 g/mol = 0.0451 mol
```

**Step 2: Calculate molality**
```
m = moles ÷ kg solvent
m = 0.0451 mol ÷ 0.050 kg = 0.901 m
```

**Step 3: Calculate ΔT**
```
ΔT = i × k_f × m
ΔT = 3 × 1.86 × 0.901 = 5.03 °C
```

**Step 4: Find new freezing point**
```
FP = 0°C − ΔT = 0°C − 5.03°C = −5.03°C
```

---

### Completed Pre-Lab Summary Table

| Solution    | Salt   | Water | Molality (m) | i  | ΔT (°C) | Expected FP (°C) |
|-------------|--------|-------|--------------|----|---------|--------------------|
| Control     | 0 g    | 50 g  | 0            | —  | 0       | 0                  |
| Light NaCl  | 2.5 g  | 50 g  | 0.856        | 2  | 3.18    | −3.18              |
| Heavy NaCl  | 7.5 g  | 50 g  | 2.57         | 2  | 9.56    | −9.56              |
| CaCl₂       | 5.0 g  | 50 g  | 0.901        | 3  | 5.03    | −5.03              |

---

## THE EXPERIMENT

### Part A: Calibration (5 min)

**What you're doing:** Checking if your thermometer reads correctly at 0°C.

**Procedure:**
1. Fill a 250 mL beaker halfway with crushed ice
2. Add just enough water to fill gaps between ice pieces (about 50 mL)
3. Stir gently for 2 minutes with a glass stirring rod
4. Insert thermometer, wait 30 seconds, record temperature

**Realistic Result (Old Equipment):**
- Thermometer reading: **+0.3 °C**
- Correction factor: **−0.3 °C**

*Instructor Note: This means we subtract 0.3°C from all future readings. A thermometer that reads 0.3°C high is actually very common in older labs!*

---

### Part B: Prepare & Test Solutions (30 min)

**Setup Instructions:**

1. **Label 4 beakers:** Control, Light, Heavy, Premium (use tape or wax pencil)

2. **Weigh your salts** (do this BEFORE adding ice):
   - Control: no salt
   - Light: 2.5 g NaCl → *Actually measured: 2.6 g* (close enough!)
   - Heavy: 7.5 g NaCl → *Actually measured: 7.4 g* (good)
   - Premium: 5.0 g CaCl₂ → *Actually measured: 5.1 g* (good)

3. **Add crushed ice to each beaker:** Aim for 50 g, but eyeball it (about a small handful plus a bit more)

4. **Add the pre-weighed salt to each beaker**

5. **Stir continuously and record temperatures**

---

### Data Collection - Realistic Results

**How to Read This Table:**
- Start timing when you add the salt and begin stirring
- Read temperature every 60 seconds
- Keep stirring! The solution needs constant agitation
- Watch for the temperature to "plateau" (stop dropping) — that's your freezing point

| Time (s) | Control | Light NaCl | Heavy NaCl | CaCl₂ |
|----------|---------|------------|------------|-------|
| 0        | 2.1     | 2.3        | 2.5        | 3.8*  |
| 60       | 0.8     | −0.5       | −2.4       | −1.2  |
| 120      | 0.2     | −1.8       | −5.6       | −3.1  |
| 180      | 0.1     | −2.5       | −7.8       | −4.2  |
| 240      | 0.0     | −2.8       | −8.5       | −4.6  |
| 300      | 0.0     | −2.9       | −8.7       | −4.7  |
| Final    | 0.0     | −2.9       | −8.8       | −4.8  |

*\*CaCl₂ starts warmer because it releases heat when dissolving (exothermic!). This is normal and expected.*

**After applying calibration correction (−0.3°C):**

| Time (s) | Control | Light NaCl | Heavy NaCl | CaCl₂ |
|----------|---------|------------|------------|-------|
| Final (corrected) | −0.3 | −3.2 | −9.1 | −5.1 |

*Instructor Note: The Control reading of −0.3°C shows our calibration worked — pure water should freeze right at 0°C, and that's essentially what we got.*

---

### Part C: Cold Limit Test (10 min)

**Creating the Super-Cold Bath:**
1. Fill a large beaker or container with ice
2. Add a LOT of rock salt (roughly 1:3 ratio salt to ice by volume)
3. Stir vigorously until temperature drops to around −15°C
4. *Actual temperature achieved: −14.2°C* (close enough!)

**Testing Each Solution:**

Place small test tubes of each solution into the cold bath and observe after 5 minutes:

| Solution        | Freezes at −15°C? | Why? |
|-----------------|-------------------|------|
| Control (water) | **YES** - solid ice | FP = 0°C, which is much warmer than −15°C, so it freezes easily |
| Light NaCl      | **YES** - mostly frozen with some liquid | FP = −3.2°C, still warmer than −15°C, freezes but takes longer |
| Heavy NaCl      | **NO** - stays liquid | FP = −9.1°C; −15°C is colder than FP, but just barely below theoretical −9.56°C so it stays liquid |
| CaCl₂           | **NO** - stays liquid | FP = −5.1°C; the bath is much colder than needed, but solution stays liquid at −15°C |

*Wait, shouldn't Heavy NaCl freeze since −15°C is colder than −9.1°C?*

**Good observation!** In theory, yes. But with highly concentrated solutions and rapid cooling, we sometimes see **supercooling** — the solution goes below its freezing point without actually forming ice crystals. Also, the theoretical −9.56°C assumes perfect conditions. In practice, these concentrated salt solutions can resist freezing even a few degrees below their theoretical freezing point.

---

## RESULTS TABLE

| Treatment   | Predicted FP | Actual FP (corrected) | % Error |
|-------------|--------------|----------------------|---------|
| Control     | 0°C          | −0.3°C               | — (reference) |
| Light NaCl  | −3.18°C      | −3.2°C               | 0.6%    |
| Heavy NaCl  | −9.56°C      | −9.1°C               | 4.8%    |
| CaCl₂       | −5.03°C      | −5.1°C               | 1.4%    |

### % Error Calculations

**Light NaCl:**
```
% Error = |predicted − actual| ÷ |predicted| × 100
% Error = |−3.18 − (−3.2)| ÷ |−3.18| × 100
% Error = |0.02| ÷ 3.18 × 100 = 0.6%
```
*Excellent result!*

**Heavy NaCl:**
```
% Error = |−9.56 − (−9.1)| ÷ |−9.56| × 100
% Error = |−0.46| ÷ 9.56 × 100 = 4.8%
```
*Acceptable. Higher concentrations tend to deviate more due to ion pairing.*

**CaCl₂:**
```
% Error = |−5.03 − (−5.1)| ÷ |−5.03| × 100
% Error = |0.07| ÷ 5.03 × 100 = 1.4%
```
*Good result!*

---

## COST ANALYSIS

### NaCl (Heavy) - Cost per °C of Protection

**Given:** NaCl costs $60/ton, we used 7.5 g, achieved ΔT = 9.1°C (actual)

**Step 1: Convert cost to $/gram**
```
1 ton = 907,185 g
Cost per gram = $60 ÷ 907,185 g = $0.0000661/g
```

**Step 2: Calculate cost of 7.5 g**
```
Cost = 7.5 g × $0.0000661/g = $0.000496
```

**Step 3: Calculate cost per °C of protection**
```
Cost per °C = $0.000496 ÷ 9.1°C = $0.0000545 per °C
```

### CaCl₂ - Cost per °C of Protection

**Given:** CaCl₂ costs $300/ton, we used 5.0 g, achieved ΔT = 5.1°C (actual)

**Step 1: Cost per gram**
```
Cost per gram = $300 ÷ 907,185 g = $0.000331/g
```

**Step 2: Cost of 5.0 g**
```
Cost = 5.0 g × $0.000331/g = $0.00165
```

**Step 3: Cost per °C**
```
Cost per °C = $0.00165 ÷ 5.1°C = $0.000324 per °C
```

### Completed Cost Table

| Salt        | Cost/ton | Mass Used | ΔT Achieved | Cost per °C    |
|-------------|----------|-----------|-------------|----------------|
| NaCl (Heavy)| $60      | 7.5 g     | 9.1°C       | $0.000055/°C   |
| CaCl₂       | $300     | 5.0 g     | 5.1°C       | $0.000324/°C   |

### Which is more cost-effective?

**NaCl is approximately 6× more cost-effective than CaCl₂** ($0.000055 vs $0.000324 per °C).

*However*, this isn't the whole story! NaCl only works down to about −9°C. If your city regularly sees temperatures below −10°C, you MUST use CaCl₂ even though it costs more — because cheap salt that doesn't work is infinitely expensive!

---

## ANALYSIS QUESTIONS - Model Answers

### 1. Why does CaCl₂ produce a greater freezing point depression than NaCl at the same molality?

**Answer:** CaCl₂ has a higher van't Hoff factor (i = 3) compared to NaCl (i = 2). When CaCl₂ dissolves, it dissociates into THREE ions (Ca²⁺ + 2Cl⁻), while NaCl only dissociates into TWO ions (Na⁺ + Cl⁻). Since freezing point depression depends on the NUMBER of dissolved particles (not their identity), more particles = greater depression. At the same molality, CaCl₂ produces 50% more particles than NaCl.

---

### 2. Why do cities switch from NaCl to CaCl₂ when temperatures drop below −10°C?

**Answer:** NaCl has a practical effectiveness limit of about −9°C (15°F). Below this temperature, NaCl simply cannot lower the freezing point enough to prevent ice formation — the road will freeze even with salt present. CaCl₂ remains effective down to −29°C (−20°F) because it produces more particles per mole AND has higher solubility at low temperatures. Cities switch to CaCl₂ during extreme cold snaps because using NaCl would be pointless — it wouldn't prevent ice formation.

---

### 3. Why do cities spray salt brine BEFORE a storm instead of spreading dry salt after?

**Answer:** Pre-treating with brine (salt dissolved in water) is more effective for several reasons:

1. **Already dissolved:** Dry salt needs moisture to dissolve before it can work. Pre-dissolved brine works immediately.

2. **Better adhesion:** Liquid brine sticks to the road surface and doesn't blow away or bounce off like dry granules.

3. **Prevents bonding:** When brine is applied before snow falls, it prevents ice from bonding to the pavement. Ice that can't bond is much easier to plow off.

4. **Uses less salt:** Pre-treatment requires 20-30% less salt than reactive treatment, saving money and reducing environmental impact.

---

### 4. How does road salt damage the environment? (Name 2 effects)

**Answer:**

1. **Freshwater contamination:** Salt runs off into streams, rivers, lakes, and groundwater. Elevated chloride levels harm aquatic organisms (fish, amphibians, invertebrates) that cannot tolerate high salinity. Some urban lakes have become as salty as ocean water.

2. **Soil and plant damage:** Salt accumulates in roadside soil, drawing water out of plant roots (osmotic stress) and making it difficult for trees and vegetation to survive. This is why you see dead grass and struggling trees along heavily salted roads.

*Other acceptable answers:* Corrosion of infrastructure (bridges, cars), contamination of drinking water wells, harm to pets' paws, damage to concrete through freeze-thaw cycles.

---

### 5. Storm forecast: −5°C. Which salt should the city use, and why?

**Answer:** The city should use **NaCl (rock salt)** for this storm.

**Reasoning:**
- At −5°C, NaCl is still effective (it works down to about −9°C)
- NaCl costs only $60/ton compared to $300/ton for CaCl₂
- At the same mass, heavy NaCl provides greater temperature depression than the CaCl₂ concentration used in this lab
- Cost-effectiveness analysis shows NaCl is 6× cheaper per degree of protection

**Bottom line:** Save the expensive CaCl₂ for when temperatures drop below −9°C. At −5°C, cheap rock salt works fine!

---

## COMMON SOURCES OF ERROR

If your results didn't match predictions perfectly, consider these factors:

| Error Source | Effect on Results |
|--------------|-------------------|
| **Ion pairing** | At high concentrations, some Na⁺ and Cl⁻ ions pair up temporarily, reducing the effective particle count. This makes actual ΔT smaller than predicted. |
| **Thermometer lag** | Old digital thermometers may respond slowly to temperature changes, causing you to miss the true minimum. |
| **Incomplete dissolution** | If salt doesn't fully dissolve, fewer particles are in solution, reducing ΔT. |
| **Impure salt** | Lab-grade NaCl may contain anti-caking agents or moisture, affecting actual moles of salt. |
| **Heat from environment** | Warm air in the lab adds heat to your cold solution, raising the apparent freezing point. |
| **Supercooling** | Solutions can temporarily go below their true freezing point without freezing. |

---

## QUICK REFERENCE - Key Numbers to Remember

| Constant | Value | What It Means |
|----------|-------|---------------|
| k_f (water) | 1.86 °C/m | Water's freezing point drops 1.86°C for every 1 molal of non-dissociating solute |
| NaCl molar mass | 58.44 g/mol | For quick calculations |
| CaCl₂ molar mass | 110.98 g/mol | For quick calculations |
| i (NaCl) | 2 | Na⁺ + Cl⁻ = 2 particles |
| i (CaCl₂) | 3 | Ca²⁺ + 2Cl⁻ = 3 particles |

---

**TEHRANI LABS 2026**

*"A beaker is just a cup that went to graduate school. Respect it accordingly."*

---

*This walkthrough prepared for CHM152L students who need additional support. Remember: understanding WHY the math works is more important than just getting the right numbers!*
