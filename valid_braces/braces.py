def valid_braces(string):
    # Stack to keep track of opening braces
    braces_stack = []
    
    # Dictionary to define matching pairs
    matching_brace = {')': '(', '}': '{', ']': '['}
    
    for char in string:
        # Push opening braces onto the stack
        if char in matching_brace.values():
            braces_stack.append(char)
        
        # Handle closing braces
        elif char in matching_brace.keys():
            # If stack is empty or top of stack does not match the current closing brace, it's invalid
            if not braces_stack or braces_stack.pop() != matching_brace[char]:
                return False

    # If the stack is empty, all braces were matched correctly
    return len(braces_stack) == 0

