dayconversions = {
   "Sun": "Sunday",
   "Mon": "Monday",
   "Tue": "Tuesday",
   3: "Wednesday",
   "Thu":"Thursday",
   "Fri": "Friday"

}
print(dayconversions["Sun"]) ## using bracket notation
print(dayconversions.get("Thur","not a valid key")) ## using the keyword get