# python dictionaries.py
# Dictionaries
# key-value pairs called items, associative arrays, hash tables, hashes
contacts = {
    "emergency": "911",
    "home": "555-555-555"
}
print("Dictionary property", contacts["emergency"])
print("Contacts", contacts)

contacts["school"] = "562"
print(contacts)
print(len(contacts))

del contacts["emergency"]
print("Deleted emergency contact", contacts)

if "home" in contacts.keys():
    print("Home contact set")

if "555-555-555" in contacts.values():
    print("Home number found")

for contact in contacts:
    print("Key", contact, "Value", contacts[contact])

for contact, phone_number in contacts.items():
    print(contact, phone_number)
