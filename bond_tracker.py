import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Daten laden
df = pd.read_csv('data/swiss_bonds.csv', parse_dates=['Date'])

# 2. Sektor-Durchschnitte berechnen (Zeitreihen-Analyse)
sector_analysis = df.groupby(['Date', 'Sector'])['Yield'].mean().unstack()

# 3. Spreads berechnen (Das Herzstück für Syndicate/DCM)
# Spread = Rendite eines Sektors MINUS Rendite der Eidgenossenschaft (Government)
# Wir multiplizieren mit 100, um Basispunkte (bps) zu erhalten
sector_analysis['Spread_Bank'] = (sector_analysis['Bank'] - sector_analysis['Government']) * 100
sector_analysis['Spread_Corporate'] = (sector_analysis['Corporate'] - sector_analysis['Government']) * 100

# 4. Grafiken erstellen
os.makedirs('outputs', exist_ok=True)

# Plot A: Rendite-Entwicklung (Yield Trends)
plt.figure(figsize=(10, 6))
for sector in ['Government', 'Bank', 'Corporate']:
    plt.plot(sector_analysis.index, sector_analysis[sector], label=sector, marker='o', markersize=4, linewidth=2)

plt.title('Swiss Bond Market: Yield Trends by Sector (CHF)', fontsize=14, fontweight='bold')
plt.ylabel('Yield in %')
plt.xlabel('Date')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('outputs/yield_trends.png')

# Plot B: Aktueller Spread-Vergleich (Credit Spreads)
plt.figure(figsize=(8, 5))
latest_spreads = sector_analysis[['Spread_Bank', 'Spread_Corporate']].iloc[-1]
latest_spreads.plot(kind='bar', color=['#2ecc71', '#e74c3c'], edgecolor='black')

plt.title('Current Credit Spreads over Swiss Government (bps)', fontsize=14, fontweight='bold')
plt.ylabel('Spread in Basis Points (bps)')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/spreads_over_gov.png')

print("\n--- ANALYSE ERFOLGREICH ---")
print(f"Letzter Stand Bank Spread: {latest_spreads['Spread_Bank']:.1f} bps")
print(f"Letzter Stand Corp Spread: {latest_spreads['Spread_Corporate']:.1f} bps")
print("Grafiken wurden im Ordner 'outputs/' gespeichert.")
