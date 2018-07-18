me = {"name": "Jasmin", 
    "age": 26, 
    "hobbies": ["playing video games", "reading", "playing board games", "learning"], 
    "wake up times": {"monday": 8, "friday": 8, "saturday": 11}
}

print(f'My name is {me["name"]}. I have {len(me["hobbies"])} hobbies. I get up at {me["wake up times"]["monday"]} on Monday.')
