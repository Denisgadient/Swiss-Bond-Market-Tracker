import pandas as pd
import numpy as np
import os

def create_market_data():
    os.makedirs('data', exist_ok=True)
    
    # Definition der Sektoren und Emittenten
    sectors = {
        'Government': ['Swiss Confederation'],
        'Bank': ['UBS', 'ZKB', 'Raiffeisen', 'Julius Baer'],
        'Corporate': ['Nestle', 'Roche', 'Novartis', 'Sika', 'Holcim']
    }
    
    # 20 Zeitpunkte (Wochen) simulieren
    dates = pd.date_range(end=pd.Timestamp.now(), periods=20, freq='W')
    data_list = []

    for date in dates:
        for sector, issuers in sectors.items():
            for issuer in issuers:
                # Wir simulieren für jeden Issuer 3 Bonds (Short, Medium, Long Term)
                for maturity in [3, 7, 10]:
                    # CHF Yield Logik: Gov ist am niedrigsten (~0.8%), Bank höher (~1.4%), Corp (~1.6%)
                    base = 0.8 if sector == 'Government' else (1.4 if sector == 'Bank' else 1.6)
                    yield_val = base + (maturity * 0.05) + np.random.normal(0, 0.03)
                    
                    data_list.append({
                        'Date': date,
                        'ISIN': f"CH{np.random.randint(100000000, 999999999)}",
                        'Issuer': issuer,
                        'Sector': sector,
                        'Maturity_Years': maturity,
                        'Yield': round(yield_val, 3)
                    })
    
    df = pd.DataFrame(data_list)
    df.to_csv('data/swiss_bonds.csv', index=False)
    print("Erfolg: 'data/swiss_bonds.csv' mit ~40 Bonds wurde erstellt.")

if __name__ == "__main__":
    create_market_data()
