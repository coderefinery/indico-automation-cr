# Automation for Indico

## Notes

```
%load basic.py

confirm_users(data[data.Confirmed=='y'].ID)

for idx, row in data[~data.Room.isna()].iterrows():
     print(row)
     if update_person(row.ID, room=row.Room) == 'break': break

```
