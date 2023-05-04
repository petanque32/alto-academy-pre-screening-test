def analyze_weekly_temperatures():
    # Initialize an empty list to store the temperatures
    temperatures = []

    # Use a loop to get the temperature for each day
    for day in [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]:
        temp = float(input(f"Enter the temperature for {day}: "))
        temperatures.append(temp)

    # Calculate the average temperature for the week
    avg_temp = sum(temperatures) / len(temperatures)
    print(f"The average temperature for the week is {avg_temp:.2f} degrees Celsius.")

    # Find the highest and lowest temperatures for the week
    highest_temp = max(temperatures)
    lowest_temp = min(temperatures)
    print(
        f"The highest temperature for the week is {highest_temp:.2f} degrees Celsius."
    )
    print(f"The lowest temperature for the week is {lowest_temp:.2f} degrees Celsius.")

    # Sort the temperatures in ascending order
    sorted_temperatures = sorted(temperatures)
    print("The temperatures for the week in ascending order are:")
    for temp in sorted_temperatures:
        print(f"{temp:.2f} degrees Celsius")

    # Calculate the variance of the temperatures for the week
    squared_deviations = [(temp - avg_temp) ** 2 for temp in temperatures]
    variance = sum(squared_deviations) / len(temperatures)
    print(
        f"The variance of the temperatures for the week is {variance:.2f} degrees Celsius squared."
    )


if __name__ == "__main__":
    analyze_weekly_temperatures()
