# ECC_Simulation

A command-line program that **simulates Error Correcting Codes (ECC)** across different transmission mediums and environmental conditions.
The goal is to model how ECC algorithms behave when exposed to noise, hops, and variable error rates—letting you see which algorithms perform well, when, and why.

This project was created as part of *Basic Programming*, but is designed to serve as a learning tool for anyone curious about ECC behavior in imperfect real-world conditions.

---

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [ECC Methods](#ecc-methods)
* [Transmission Mediums](#transmission-mediums)
* [Environmental Variables](#environmental-variables)
* [Running the Program](#running-the-program)
* [Future Plans](#future-plans)

---

## Overview

This CLI application guides the user through selecting:

1. An **ECC method**
2. A **transmission medium**
3. Several **environmental variables** (noise level, hops, error multipliers, etc.)

The simulation uses Python’s `random` library to inject errors in unpredictable ways—mimicking real-world randomness in communication channels.
The intention is to observe how far different ECCs can be pushed before they fail, and how environmental conditions influence reliability.

---

## Features

✔ Interactive CLI prompts
✔ Multiple ECC methods to choose from
✔ Configurable environmental conditions
✔ Medium selection (e.g., copper wire, fiber, satellite radio, WiFi 7)
✔ Randomized error simulation
✔ Supports large test batches (up to 100,000 trials)

---

## ECC Methods

The user can choose from six ECC techniques:

1. **Parity Bit**
   Basic single-bit parity detection.

2. **Hamming Code**
   Single-error correction, double-error detection.

3. **Reed–Solomon Code**
   Robust symbol-level ECC used in CDs, DVDs, and satellite comms.

4. **Redundancy Code**
   Repeats data multiple times; simple but wasteful.

5. **Checksum Code**
   Uses a sum-based integrity check.

6. **No ECC**
   Baseline: raw transmission with no protection.

---

## Transmission Mediums

Users select one of eight mediums, each representing different real-world communication channels:

1. Copper Wire
2. Fiber Optic Cable
3. Coaxial Cable
4. Cat6 Ethernet Cable
5. Satellite Radio
6. 5G Network
7. FM Radio
8. WiFi 7

These selections can later be tied to unique noise profiles.

---

## Environmental Variables

After choosing ECC and medium, users configure:

| Prompt                        | Meaning                                                            |
| ----------------------------- | ------------------------------------------------------------------ |
| **Noise Level (0–3)**         | None, low, medium, or high environmental noise                     |
| **Hops (0–10)**               | How many relays the signal passes through                          |
| **Error-rate Multiplier**     | A decimal multiplier for exaggerating or scaling error probability |
| **Medium Length (1–1000 km)** | The simulated distance the signal travels                          |
| **Test Amount (1–100000)**    | Number of trials to run                                            |

---

## Running the Program

Clone and run:

```bash
git clone https://github.com/<your-username>/ECC_Simulation
cd ECC_Simulation
python main.py
```

You will be guided through all selections interactively.

---

## Future Plans

Planned enhancements include:

* Implementing actual ECC encode/decode logic
* Adding bit-flip simulation per hop
* Medium-specific noise profiles
* Gathering metrics (correction rates, residual errors, overhead, etc.)
* Exporting results to CSV
* Visualization tools
* Modular ECC method folder (`ecc_methods/`)