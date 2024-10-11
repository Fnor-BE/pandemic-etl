

def adjust_country_names(df):
    df['Country'] = df['Country'].apply(lambda x: x.strip())
    
    COUNTRY_ADJUSTMENTS = {
        'Bosnia and Herzegovina': ['Bosnia and Hezegovina'],
        'Burma': ['Myanmar'],
        'Cabo Verde': ['Cap Verde'],
        'Czechia': ['Czech Republic'],
        'Iran': ['Iran, Islamic Republic'],
        'Ireland': ['Republic of Ireland'],
        'Russia': ['Russian Federation'],
        'South Korea': ['Republic of Korea'],
        'Vietnam': ['Viet Nam'],
        'United States': ['US', 'United States of America']
    }
    
    # Verify 'Country' exists
    for country, variants in COUNTRY_ADJUSTMENTS.items():
        for variant in variants:
            # Update the Country column for each variant
            df.loc[df['Country'] == variant, 'Country'] = country
            
    SPLIT_COUNTRIES = {
        'Bermuda, UKOT':                                    ['United Kingdom', 'Bermuda'],
        'British Virgin Islands,  UKOT':                    ['United Kingdom', 'British Virgin Islands'],
        'British Virgin Islands, UKOT':                     ['United Kingdom', 'British Virgin Islands'],
        #'Brunei Darussalam'                                 ['United Kingdom', 'British Virgin Islands'],
        'Cayman Islands, UKOT':                             ['United Kingdom', 'Cayman Islands'],
        # 'Cook Island',
        # 'France, French Polynesia, FOC',
        # 'France, Martinique, FOC',
        # 'France, New Caledonia, FOC',
        # 'French Polynesia, FOC',
        # 'Guadaloupe, FOC',
        # 'Guernsey, Crown Dependency',
        # 'Hong Kong Special Administrative Region',
        # 'Isle of Man, Crown Dependency',
        # 'Jersey, Crown Dependency',
        # 'Martinique, FOC',
        # 'Netherlands Antilles, Curaçao',
        # 'Netherlands Antilles, Sint Maarten',
        # 'Netherlands, Aruba',
        # 'Netherlands, Curacao, OT',
        # 'New Caledonia, FOC',
        # 'Palau',
        # 'Puerto Rico',
        # 'Saint Martin, FOC',
        # 'Samoa',
        # 'The former Yugoslav Republic of Macedonia',
        # 'UK',
        # 'United Kingdom, Isle of Man, Crown Dependency',
        # 'United Kingdom, Jersey, Crown Dependency',
        # 'Vanuatu',
        # 'Virgin Islands',
        # 'West Bank and Gaza Strip'
        'Hong Kong SAR China':                              ['China', 'Hong Kong'],
        'Macao SAR China':                                  ['China', 'Macau'],
        'Taiwan China':                                     ['China', 'Taiwan'],
    }
    
    for match, repl in SPLIT_COUNTRIES.items():
        df.loc[df['Country'] == match, ['Country', 'ProvinceState']] = [repl[0], repl[1]]
    