def running_time(start_hour, start_minutes):
    # Define the pace for easy and tempo runs in minutes and seconds
    easy_pace = 8 * 60 + 15  # Easy pace is 8 minutes 15 seconds per mile (converted to seconds)
    tempo_pace = 7 * 60 + 12  # Tempo pace is 7 minutes 12 seconds per mile (converted to seconds)
    
    # Calculate the total time in seconds (2 easy pace miles + 3 tempo pace miles)
    total_time_seconds = easy_pace * 2 + (tempo_pace * 3)
    
    # Convert total time in seconds to minutes and remaining seconds
    total_minutes = total_time_seconds // 60  # Calculate total minutes
    total_seconds = total_time_seconds % 60  # Calculate the remaining seconds
    
    # Calculate the final minutes by adding the total time to the starting minutes
    end_minutes = total_minutes + start_minutes
    end_hour = start_hour  # Set the starting hour as the end hour
    
    # Check if the end minutes exceed 60 minutes and adjust the hour accordingly
    if end_minutes >= 60:
        end_hour += end_minutes // 60  # Increase the hour for each hour of excess minutes
        end_minutes = end_minutes % 60  # Adjust the remaining minutes after exceeding 60
    
    # Return the calculated end hour and end minutes
    return end_hour, end_minutes 

# Call the function with a start time of 6:52 AM
end_hour, end_minutes = running_time(6, 52)

# Print the arrival time
print(f"You will arrive home for breakfast at {end_hour}:{end_minutes} AM.")
