# Automation for Indico

Indico doesn't have an API to update registrants to events, and when
you need to do mass updates this is annoying.  This uses Selenium to
do these updates by scripting a web browser.

Currently little documentation, but the idea is:
- export participants to a spreadsheet
- update the spreadsheet, add a column for changes you want to make
- Open in IPython shell and copy-paste the relevant lines into it to
  set up the environment. (`%load basic.py`)
- Load your modified spreadsheet in a pandas dataframe (variable name
  `data` below)
- Run some of the lines you see below to update the registrations.



## Notes

```
%load basic.py

select_users(data[data.confirm=='y'].ID)
# Then you have to manually confirm yourself

# Set rooms
for idx, row in data[~data.new_room.isna()].iterrows():
     print(row)
     if update_person(row.ID, room=row.new_room) == 'break': break

for idx, row in data[~data.new_type.isna()].iterrows():
     print(row)
     if update_person(row.ID, type=row.new_type) == 'break': break
```
