"""
Rule-Based Chatbot
A simple chatbot that uses if-else logic to respond to user inputs.
Handles greetings, exit commands, and basic conversation patterns.
"""

def sanitize_input(user_input):
    """
    Sanitize and normalize user input.
    Converts to lowercase and removes leading/trailing whitespace.
    
    Args:
        user_input (str): Raw user input
        
    Returns:
        str: Cleaned user input
    """
    return user_input.lower().strip()


def get_greeting_response(user_input):
    """
    Handle greeting commands.
    
    Args:
        user_input (str): Sanitized user input
        
    Returns:
        str: Greeting response or None if not a greeting
    """
    greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 
                 'good afternoon', 'good evening', 'howdy', 'sup']
    
    if user_input in greetings:
        return "Hello! Welcome to the chatbot. How can I help you today?"
    
    return None


def get_exit_response(user_input):
    """
    Handle exit commands.
    
    Args:
        user_input (str): Sanitized user input
        
    Returns:
        bool: True if user wants to exit, False otherwise
    """
    exit_commands = ['exit', 'quit', 'bye', 'goodbye', 'see you', 'farewell', 'leave']
    
    if user_input in exit_commands:
        return True
    
    return False


def get_how_are_you_response(user_input):
    """
    Handle 'how are you' type questions.
    
    Args:
        user_input (str): Sanitized user input
        
    Returns:
        str: Response or None if not applicable
    """
    how_are_you_phrases = ['how are you', 'how are you doing', 'how are you today',
                           'how do you feel', 'what\'s up']
    
    if user_input in how_are_you_phrases:
        return "I'm doing great, thank you for asking! I'm here to help you. What can I do for you?"
    
    return None


def get_name_response(user_input):
    """
    Handle 'what is your name' type questions.
    
    Args:
        user_input (str): Sanitized user input
        
    Returns:
        str: Response or None if not applicable
    """
    name_questions = ['what is your name', 'who are you', 'what\'s your name',
                      'tell me your name']
    
    if user_input in name_questions:
        return "I'm a Rule-Based Chatbot, created to assist you with basic conversation!"
    
    return None


def get_help_response(user_input):
    """
    Handle help requests.
    
    Args:
        user_input (str): Sanitized user input
        
    Returns:
        str: Response or None if not applicable
    """
    help_commands = ['help', 'help me', 'what can you do', 'what are your features']
    
    if user_input in help_commands:
        return """I can help you with:
        - Greetings (say 'hello', 'hi', etc.)
        - Tell you my name (ask 'who are you')
        - Chat about how you're doing
        - Answer questions about what I can do
        - Exit when you're done (say 'bye', 'exit', etc.)
        
Type any message and I'll try to respond!"""
    
    return None


def get_response(user_input):
    """
    Main logic to determine chatbot response based on user input.
    Uses if-else statements to route to appropriate response handlers.
    
    Args:
        user_input (str): Sanitized user input
        
    Returns:
        str: Chatbot response
    """
    # Check for greetings
    response = get_greeting_response(user_input)
    if response:
        return response
    
    # Check for "how are you" questions
    response = get_how_are_you_response(user_input)
    if response:
        return response
    
    # Check for name questions
    response = get_name_response(user_input)
    if response:
        return response
    
    # Check for help requests
    response = get_help_response(user_input)
    if response:
        return response
    
    # Default response for unknown inputs
    return "I'm not sure how to respond to that. Type 'help' to see what I can do!"


def run_chatbot():
    """
    Main function to run the chatbot in a continuous loop.
    Handles user input/output and exit conditions.
    """
    print("=" * 60)
    print("Welcome to the Rule-Based Chatbot!")
    print("Type 'help' for available commands or 'exit' to quit.")
    print("=" * 60)
    print()
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Skip empty inputs
            if not user_input:
                print("Chatbot: Please say something!\n")
                continue
            
            # Sanitize input
            sanitized_input = sanitize_input(user_input)
            
            # Check for exit command
            if get_exit_response(sanitized_input):
                print("Chatbot: Goodbye! Thanks for chatting with me!\n")
                break
            
            # Get and display response
            response = get_response(sanitized_input)
            print(f"Chatbot: {response}\n")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nChatbot: Goodbye! Thanks for chatting with me!")
            break
        except Exception as e:
            print(f"Chatbot: An error occurred: {str(e)}\n")


if __name__ == "__main__":
    run_chatbot()