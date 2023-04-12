import main_scrap

Da_dict, Da_df = main_scrap.scrap('Data Analysis')
Ds_dict, Ds_df = main_scrap.scrap('Data science')
Ba_dict, Ba_df = main_scrap.scrap('Business Intelligence')

combined_dfs = main_scrap.df_concat([Da_df, Ds_df, Ba_df])

#Collect all in ( one CSV File )

combined_dfs.to_csv('data.csv', index=False)

if __name__ == "__main__":
    print("Done")