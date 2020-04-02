def cleanup(merged):
    # Standerdize Country Names
    merged['Country'].replace('United Kingdom', 'UK', inplace=True)
    merged['Country'].replace('Mainland China', 'China', inplace=True)
    merged['Country'].replace(['Korea, South', 'Republic of Korea'], 'South Korea', inplace=True)
    merged['Country'].replace('Iran (Islamic Republic of)', 'Iran',inplace=True)

    # Standerdize US State Names
    merged['State'] = merged['State'].str.strip()
    merged['State'].replace(regex={'^.*Virgin Islands.*$': 'Virgin Islands'}, inplace=True)
    merged['State'].replace(regex={'^(.+) \(From Diamond Princess\)$': r'\1'}, inplace=True)
    merged['State'].replace(regex={'^.*Princess.*$': 'Cruise Ship'}, inplace=True)
    merged['State'].replace(regex={'^.+, (.+)$': r'\1'}, inplace=True)
    merged['State'].replace(['District of Columbia', 'D.C.'], 'DC', inplace=True)
    merged['State'].replace('Chicago', 'IL', inplace=True)
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }
    merged['State'].replace(us_state_abbrev, inplace=True)
    # Fill NaNs otherwise some operations such as gorupby will not work
    merged['Confirmed'].fillna(0, inplace=True)
    merged['Deaths'].fillna(0, inplace=True)
    merged['Recovered'].fillna(0, inplace=True)
    merged['State'].fillna('n/a', inplace=True)
    merged['County'].fillna('n/a', inplace=True)

def verify(merged):
    # Run verifications - ignore small deviations
    df_neg = merged[(merged['County'] != 'Unassigned') & (merged['Confirmed_New'] < -100) | (merged['Deaths_New'] < -50) | (merged['Recovered_New'] < -50)]
    if df_neg.shape[0] > 0:
        print('Some deltas are hugely negative!')
        print(df_neg.sort_values('Confirmed_New'))

    mismatch = merged[(merged['State'] != 'US') & (merged['State'] != 'Recovered') & (merged['County'] != 'Unassigned') & (merged['Confirmed'] - (merged['Deaths'] + merged['Recovered']) < -10)]
    if mismatch.shape[0] > 0:
        print('Confirmed is much smaller than Deaths + Recovered!')
        print(mismatch)
