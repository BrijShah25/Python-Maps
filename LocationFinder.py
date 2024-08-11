import openai


# openai.api_key = 'ADD OPENAI API KEY'
# They are restricting me to add my OPENAI API to GITHUB, so please contact me from my Resume to get the API key. Thanks. :)

def get_directions(start_location, end_location):
    prompt = f"Provide driving directions and the distance from {start_location} to {end_location}."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use gpt-3.5-turbo or gpt-4
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )

    return response.choices[0].message['content'].strip()

# Get user input for locations
start_location = input("Enter the starting location: ")
end_location = input("Enter the destination location: ")

# Get directions
directions = get_directions(start_location, end_location)
print("\nDirections and Distance:")
print(directions)
