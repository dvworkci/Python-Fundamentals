# Dictionaries in python
# Examples : -
monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}

print(monthConversions)
print(monthConversions["Sep"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv","Not a valid key")) # Second param is default value