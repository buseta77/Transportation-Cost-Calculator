Scripts execution orders:
1. Items
2. Formulas
3. Supplies
4. Rooms

We are using free version of Neon PostgreSQL provider.

All json files are initial values.
Labor hour is stored in supplies table.

Script to create executable file
```pyinstaller --onefile --windowed --icon=icons/app.ico app.py --add-data "icons/*;icons" --name="FH Calculator"```