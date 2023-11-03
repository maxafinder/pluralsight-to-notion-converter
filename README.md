<img src="https://github.com/maxafinder/pluralsight-to-notion-converter/assets/76804820/a864c92d-3204-4409-a4fe-19cc4121e9bb" width="15%" />

# pluralsight-to-notion-converter
Allows notes downloaded from Pluralsight to be automatically converted from a `.csv` file into a completely formatted Notion page.
## Example

<table>
<tr>
<td>
	<img src="https://github.com/maxafinder/pluralsight-to-notion-converter/assets/76804820/28a2d3b8-08fe-4d43-961b-eee4de7db6a1" width="100%" align="top" />
	<br>
	Downloaded notes (before)
</td>
<td>
	<img src="https://github.com/maxafinder/pluralsight-to-notion-converter/assets/76804820/02fed8ad-ee00-4ff6-8933-342c452ff3ad" width="100%" />
    <br>
    Converted to Notion (After)
</td>
</tr>
</table>

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
