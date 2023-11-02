# pluralsight-to-notion-converter
Allows notes downloaded from Pluralsight to be automatically converted into a completely formatted Notion page.



## Pluralsight notes format
When you download your notes from Pluralsight, the file format that they are in is `.csv`.

## Notion integration
View the [documentation](https://developers.notion.com/docs/create-a-notion-integration) to create an internal Notion Integration. After creating a Notion Integration do the following:
1. Create a page in Notion where you want to store your Pluralsight notes.
2. Go to the Notion page you created and click on the `...` icon. Then scroll to the bottom, click on `Add Connections`, and then select the Notion Integration you created.
3. Create a `.env` file in the root directory of this project, and add the environment variables `NOTION_KEY` and `NOTION_PAGE_ID`.
	* The Notion Key can be found on the [integrations page](https://www.notion.so/my-integrations)
	* The Notion Page ID can be found at the end of the Notion page's URL (32-character code).

## Run converter in virtual environment
Make sure you have `pipenv` installed. You can install it with:
```
pip install --user pipenv
```

Run the converter with the command:

```
pipenv run python3 convert.py
```