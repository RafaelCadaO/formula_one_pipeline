import pandas

def main():
    df = pandas.read_csv('/Users/macbookpro/dev/f1/pythonProject/data/contacts.csv',sep='\;')
    df_firm_id = df[df['Firm ID']==812010]

    df_firm_id_2 = df_firm_id.replace(['NULL',''],pandas.NA)

    filter_df = df_firm_id_2[df_firm_id_2['First Name'].notna()]

    filter_df['Company'] = filter_df['Company'].str.upper()
    filter_df['Job Title'] = filter_df['Job Title'].str.upper()
    #filter_df = filter_df['Job Title'].apply(filter_df['Job Title']).str().upper()

    filter_df['Phone Number'] = filter_df['Phone Number'].str.replace('-', '')
    filter_df['Phone Number'] = filter_df['Phone Number'].str.replace('+', '')

    filter_df.to_csv('/Users/macbookpro/dev/f1/pythonProject/data/contactsfinal.csv',sep='\t')





    #812010


if __name__ == '__main__':
    main()