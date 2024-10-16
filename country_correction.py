

def adjust_country_names(df):
    df['Country'] = df['Country'].apply(lambda x: x.strip())
    
    COUNTRY_ADJUSTMENTS = {
        'Bosnia and Herzegovina': ['Bosnia and Hezegovina'],
        'Brunei': ['Brunei Darussalam'],
        'Burma': ['Myanmar'],
        'Cabo Verde': ['Cap Verde'],
        'Czechia': ['Czech Republic'],
        'Iran': ['Iran, Islamic Republic'],
        'Ireland': ['Republic of Ireland'],
        'North Macedonia': ['The former Yugoslav Republic of Macedonia'],
        'Russia': ['Russian Federation'],
        'South Korea': ['Republic of Korea'],
        'Taiwan': ['Taiwan*', 'Taiwan China'],
        'United Kingdom': ['UK'],
        'United States': ['US', 'United States of America'],
        'Vietnam': ['Viet Nam'],
        'West Bank and Gaza': ['West Bank and Gaza Strip']
    }
    
    # Verify 'Country' exists
    for country, variants in COUNTRY_ADJUSTMENTS.items():
        for variant in variants:
            # Update the Country column for each variant
            df.loc[df['Country'] == variant, 'Country'] = country
            
    SPLIT_COUNTRIES = {
        'Bermuda, UKOT':                                ['United Kingdom', 'Bermuda'],
        'British Virgin Islands,  UKOT':                ['United Kingdom', 'British Virgin Islands'],
        'British Virgin Islands, UKOT':                 ['United Kingdom', 'British Virgin Islands'],
        'Cayman Islands, UKOT':                         ['United Kingdom', 'Cayman Islands'],
        'Guernsey, Crown Dependency':                   ['United Kingdom', 'Channel Islands'],
        'Isle of Man, Crown Dependency':                ['United Kingdom', 'Isle of Man'],
        'Jersey, Crown Dependency':                     ['United Kingdom', 'Channel Islands'],
        'United Kingdom, Jersey, Crown Dependency':     ['United Kingdom', 'Channel Islands'],
        'United Kingdom, Isle of Man, Crown Dependency':['United Kingdom', 'Isle of Man'],
        'Virgin Islands':                               ['United Kingdom', 'British Virgin Islands'],
        'France, French Polynesia, FOC':                ['France', 'French Polynesia'],
        'France, Martinique, FOC':                      ['France', 'Martinique'],
        'France, New Caledonia, FOC':                   ['France', 'New Caledonia'],
        'French Polynesia, FOC':                        ['France', 'French Polynesia'],
        'Guadaloupe, FOC':                              ['France', 'Guadeloupe'],
        'New Caledonia, FOC':                           ['France', 'New Caledonia'],
        'Martinique, FOC':                              ['France', 'Martinique'],
        'Netherlands Antilles, Curaçao':                ['Netherlands', 'Curacao'],
        'Netherlands Antilles, Sint Maarten':           ['Netherlands', 'Sint Maarten'],
        'Netherlands, Aruba':                           ['Netherlands', 'Aruba'],
        'Netherlands, Curacao, OT':                     ['Netherlands', 'Curacao'],
        'Saint Martin, FOC':                            ['Netherlands', 'Sint Maarten'],
        'Hong Kong Special Administrative Region':      ['China', 'Hong Kong'],
        'Hong Kong SAR China':                          ['China', 'Hong Kong'],
        'Macao SAR China':                              ['China', 'Macau'],
        'Puerto Rico':                                  ['United States', 'Puerto Rico'],
        # 'Cook Island',
        # 'Palau',
        # 'Samoa',
        # 'Vanuatu',
    }
    
    for match, repl in SPLIT_COUNTRIES.items():
        df.loc[df['Country'] == match, ['Country', 'ProvinceState']] = [repl[0], repl[1]]
    