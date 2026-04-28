# Swiss Bond Market Tracker (CHF)

A Python-based tool to monitor yields and credit spreads in the Swiss Fixed Income market.

## Overview
This project tracks approximately 40 CHF-denominated bonds across three key sectors:
- **Government:** Swiss Confederation (Benchmark)
- **Financials (FIG):** Major Swiss banks (UBS, ZKB, etc.)
- **Corporates:** Industrial leaders (Nestle, Roche, etc.)

## Project Features
- **Spread Calculation:** Automated calculation of credit spreads over the government benchmark in basis points (bps).
- **Yield Curve Visualization:** Comparative analysis of yield movements over time.
- **Data Engineering:** Automated synthetic market data generation for simulation purposes.

## Latest Analysis Results
- **Bank Spread:** ~57.0 bps
- **Corporate Spread:** ~77.8 bps

## How to Run
1. Run `generate_bond_data.py` to create the dataset.
2. Run `bond_tracker.py` to generate the analysis and charts in the `/outputs` folder.
