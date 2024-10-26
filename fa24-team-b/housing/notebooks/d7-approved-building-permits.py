# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv("/Users/ann/Downloads/approved_building_permits.csv", low_memory=False)

# %%
df

# %%
worktype_mapping = {
    'INTEXT': 'Renovation & Interior/Exterior Work',
    'INTREN': 'Renovation & Interior/Exterior Work',
    'EXTREN': 'Renovation & Interior/Exterior Work',
    'OTHER': 'Miscellaneous',
    'SPRINK': 'Fire Protection & Safety',
    'ADDITION': 'Renovation & Interior/Exterior Work',
    'COB': 'Miscellaneous',
    'FA': 'Fire Protection & Safety',
    'ERECT': 'Construction & New Installations',
    'SITE': 'Temporary Structures & Events',
    'VIOL': 'Miscellaneous',
    'PLUMBING': 'Electrical, Plumbing & Utility Systems',
    'SPCEVE': 'Temporary Structures & Events',
    'NEWCON': 'Construction & New Installations',
    'SIGNES': 'Signage & Canopy',
    'SPRNK9': 'Fire Protection & Safety',
    'EXTDEM': 'Demolition',
    'SD': 'Miscellaneous',
    'ROOF': 'Renovation & Interior/Exterior Work',
    'GARAGE': 'Construction & New Installations',
    'AWNING': 'Signage & Canopy',
    'FENCE2': 'Renovation & Interior/Exterior Work',
    'INSUL': 'Renovation & Interior/Exterior Work',
    'SIGNS': 'Signage & Canopy',
    'FSTTRK': 'Temporary Structures & Events',
    'CHGOCC': 'Occupancy & Use Change',
    'CELL': 'Temporary Structures & Events',
    'NROCC': 'Miscellaneous',
    'SOL': 'Construction & New Installations',
    'INTDEM': 'Demolition',
    'SPFT': 'Miscellaneous',
    'RAZE': 'Demolition',
    'TMPSER': 'Temporary Structures & Events',
    'ELECTRICAL': 'Electrical, Plumbing & Utility Systems',
    'GEN': 'Electrical, Plumbing & Utility Systems',
    'CANP': 'Signage & Canopy',
    'FENCE': 'Renovation & Interior/Exterior Work',
    'SIDE': 'Renovation & Interior/Exterior Work',
    'HOLVEN': 'Miscellaneous',
    'CONVRT': 'Miscellaneous',
    'SRVCHG': 'Electrical, Plumbing & Utility Systems',
    'LVOLT': 'Electrical, Plumbing & Utility Systems',
    'MAINT': 'Miscellaneous',
    'Service': 'Miscellaneous',
    'DRIVE': 'Construction & New Installations',
    'INDBLR': 'Electrical, Plumbing & Utility Systems',
    'TEMTRL': 'Temporary Structures & Events',
    'FLAM': 'Fire Protection & Safety',
    'COMPAR': 'Miscellaneous',
    'TVTRK': 'Temporary Structures & Events',
    'New': 'Construction & New Installations',
    'GAS': 'Electrical, Plumbing & Utility Systems',
    'INDFUR': 'Electrical, Plumbing & Utility Systems',
    'AWNRNW': 'Signage & Canopy',
    'RNWSIG': 'Signage & Canopy',
    'RESPAR': 'Miscellaneous',
    'AWNRET': 'Signage & Canopy',
    'BFCHMINFIN': 'Miscellaneous',
    'BFCHMTENT': 'Temporary Structures & Events',
    'General': 'Miscellaneous',
    'Dumpsters': 'Miscellaneous',
    'TMPUSOC': 'Occupancy & Use Change',
    'OSEAT': 'Temporary Structures & Events',
    'CANPRN': 'Signage & Canopy',
    'TCOO': 'Temporary Structures & Events'
}

df = df.dropna()

df.loc[:, 'issued_date'] = pd.to_datetime(df['issued_date'], errors='coerce', format='mixed').dt.date
df.loc[:, 'expiration_date'] = pd.to_datetime(df['expiration_date'], errors='coerce', format='mixed').dt.date

d7_zip = ["02119", "02120", "02121", "02122", "02124", "02125", "02115", "02215", "02118"]
df = df[df['zip'].isin(d7_zip)].copy()
df.loc[:, 'zip'] = df['zip'].apply(lambda x: str(x).zfill(5))

d7_city = ["Dorchester", "Fenway", "Roxbury", "South End"]
df = df[df['city'].isin(d7_city)].copy()

columns_to_drop = ['property_id', 'parcel_id', 'gpsy', 'gpsx']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

df['new_worktype'] = df['worktype'].map(worktype_mapping)

df = df.dropna(subset=['new_worktype'])

df

# %%
df['issued_date'] = pd.to_datetime(df['issued_date'], errors='coerce')
df = df.dropna(subset=['issued_date'])

df['issued_year'] = df['issued_date'].dt.year

worktype_counts_per_year = df.groupby(['issued_year', 'new_worktype']).size().unstack(fill_value=0)

plt.figure(figsize=(20, 10))
worktype_counts_per_year.plot(kind='line', marker='o', linestyle='-', figsize=(20, 10))

plt.title('Total Permit Applications by Work Type from 2010 to 2024', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Total Permit Applications', fontsize=16)
plt.xticks(rotation=0, ha='right')
plt.legend(title='Work Type', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# %%
df['issued_date'] = pd.to_datetime(df['issued_date'], errors='coerce')
df = df.dropna(subset=['issued_date'])

df['issued_year'] = df['issued_date'].dt.year

occupancytype_counts_per_year = df.groupby(['issued_year', 'occupancytype']).size().unstack(fill_value=0)

plt.figure(figsize=(20, 10))
occupancytype_counts_per_year.plot(kind='line', marker='o', linestyle='-', figsize=(20, 10))

plt.title('Total Permit Applications by Occupancy from 2010 to 2024', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Total Permit Applications', fontsize=16)
plt.xticks(rotation=0, ha='right')
plt.legend(title='Occupancy Type', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# %%
status_counts_per_year = df.groupby(['issued_year', 'status']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 6))
status_counts_per_year.plot(kind='line', marker='o', linestyle='-')

plt.title('Total Permit Applications Status from 2010 to 2024', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Total Permit Applications', fontsize=14)
plt.xticks(rotation=0)
plt.legend(title='Status', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# %%
df['total_fees'] = pd.to_numeric(df['total_fees'].replace(r'[\$,]', '', regex=True))
df['declared_valuation'] = pd.to_numeric(df['declared_valuation'].replace(r'[\$,]', '', regex=True))

summary_stats = df[['total_fees', 'declared_valuation']].describe()

pd.options.display.float_format = '{:,.2f}'.format

print(summary_stats)

# %%
df.to_csv("/Users/ann/Desktop/d7-approved-building-permits.csv", index=False)
