def load_and_process(startup_funding_csv):

    # Method Chain 1 (Load data and drop data)

    df1 = (
          pd.read_csv("startup_funding_csv.csv")
          .rename(columns={"InvestmentnType": "Investment Type"})
          .copy().drop(['Remarks','Investors Name','City  Location', 'Date dd/mm/yyyy', 'Sr No'], axis=1)
          .dropna(axis=0)
      )

    # Method Chain 2 (Cleaning and wrangling)

    df2 = (
          df1
          .loc[lambda x: x['Industry Vertical'] == "Finance"]
          .replace(',','', regex=True)
          .astype({"Amount in USD": int})
          .sort_values("Amount in USD")
          .replace("Seed/ Angel Funding", "Seed / Angel Funding")
          .replace("Private", "Private Equity")
          .sort_values("Investment Type")
        
      )
     
    

    return df2 