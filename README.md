# Automation for Indico

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
