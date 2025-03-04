from datetime import datetime
import os

def get_current_datetime():
    # Use actual current date and time
    return datetime.now().strftime("%d %B %Y, %I:%M %p")

def list_operations(numbers):
    numbers = list(map(int, numbers))
    sum_numbers = sum(numbers)
    max_number = max(numbers)
    reversed_list = numbers[::-1]
    return sum_numbers, max_number, reversed_list

def remove_duplicates(numbers):
    return list(set(numbers))

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

def save_summary_to_file(summary, filename):
    # Save the file in the current working directory (project folder)
    file_path = os.path.join(os.getcwd(), filename)
    with open(file_path, 'w') as file:
        file.write(summary)
    print(f"Chatbot: Summary saved to {file_path}")

def search_chat_history(keyword, chat_history):
    found_lines = [line for line in chat_history if keyword.lower() in line.lower()]
    return found_lines

def main():
    print("Chatbot: Hello! I'm your assistant! How can I help you today?")
    chat_history = []
    commands_used = {}

    while True:
        user_input = input("User: ").strip().lower()
        chat_history.append(f"User: {user_input}")

        if user_input in ["hello", "hi"]:
            response = "Hi there! How can I help you today?"
            print(f"Chatbot: {response}")
            chat_history.append(f"Chatbot: {response}")
            commands_used["hello/hi"] = commands_used.get("hello/hi", 0) + 1
        elif user_input == "date time todays":
            current_datetime = get_current_datetime()
            response = f"{current_datetime}\nHow else can I assist you?"
            print(f"Chatbot: {response}")
            chat_history.append(f"Chatbot: {response}")
            commands_used["date time todays"] = commands_used.get("date time todays", 0) + 1
        elif user_input == "list operations":
            numbers_input = input("Chatbot: Please enter a list of integers (comma-separated): ")
            chat_history.append(f"Chatbot: Please enter a list of integers (comma-separated): {numbers_input}")
            try:
                numbers = list(map(int, numbers_input.split(',')))
                sum_numbers, max_number, reversed_list = list_operations(numbers)
                response = f"Sum: {sum_numbers}\nMaximum: {max_number}\nReversed List: {reversed_list}"
                print(f"Chatbot: {response}")
                chat_history.append(f"Chatbot: {response}")

                remove_dup = input("Chatbot: Would you like to remove duplicates? (yes/no): ").strip().lower()
                chat_history.append(f"Chatbot: Would you like to remove duplicates? (yes/no): {remove_dup}")
                if remove_dup == "yes":
                    unique_numbers = remove_duplicates(numbers)
                    response = f"Updated List: {unique_numbers}"
                    print(f"Chatbot: {response}")
                    chat_history.append(f"Chatbot: {response}")

                    # Recalculate sum, max, and reversed list after removing duplicates
                    sum_numbers, max_number, reversed_list = list_operations(unique_numbers)
                    response = f"Sum: {sum_numbers}\nMaximum: {max_number}\nReversed List: {reversed_list}"
                    print(f"Chatbot: {response}")
                    chat_history.append(f"Chatbot: {response}")

                print("Chatbot: How else can I assist you?")
            except ValueError:
                response = "Error: Please enter a valid list of integers separated by commas."
                print(f"Chatbot: {response}")
                chat_history.append(f"Chatbot: {response}")
            commands_used["list operations"] = commands_used.get("list operations", 0) + 1
        elif user_input == "generate prime":
            while True:
                range_input = input("Chatbot: Enter the range (start and end, comma-separated): ").strip()
                chat_history.append(f"Chatbot: Enter the range (start and end, comma-separated): {range_input}")
                try:
                    start, end = map(int, range_input.split(','))
                    if start >= end:
                        response = "Error: Start must be less than end."
                        print(f"Chatbot: {response}")
                        chat_history.append(f"Chatbot: {response}")
                    else:
                        primes = generate_primes(start, end)
                        response = f"Prime Numbers: {primes}"
                        print(f"Chatbot: {response}")
                        chat_history.append(f"Chatbot: {response}")
                        break
                except ValueError:
                    response = "Error: Please enter valid integers for start and end."
                    print(f"Chatbot: {response}")
                    chat_history.append(f"Chatbot: {response}")
            commands_used["generate prime"] = commands_used.get("generate prime", 0) + 1
        elif user_input == "search history":
            keyword = input("Chatbot: Enter the keyword to search in chat history: ").strip().lower()
            found_lines = search_chat_history(keyword, chat_history)
            if found_lines:
                print("Chatbot: Found the following lines:")
                for line in found_lines:
                    print(f"    - {line}")
            else:
                print("Chatbot: No matching lines found.")
            commands_used["search history"] = commands_used.get("search history", 0) + 1
        elif user_input == "bye":
            # Generate session summary
            summary = "Here’s a summary of your session:\n"
            summary += f"   - Commands Used: {len(commands_used)}\n"
            most_frequent_command = max(commands_used, key=commands_used.get)
            summary += f"   - Most Frequent Command: {most_frequent_command}\n"
            print(summary)

            # Ask if the user wants to save the summary
            save = input("Chatbot: Do you want to save this summary? (yes/no): ").strip().lower()
            if save == "yes":
                filename = f"summary_{datetime.now().strftime('%d%m%Y')}.txt"
                save_summary_to_file(summary, filename)
                print("Chatbot: Summary saved. Goodbye! Have a great day!")
            else:
                print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = "Enter correct keyword"
            print(f"Chatbot: {response}")
            chat_history.append(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
