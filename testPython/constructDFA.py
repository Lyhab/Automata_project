class DFA:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def validate_input(self, input_string):
        current_state = self.initial_state

        for char in input_string:
            if char not in self.alphabet:
                return False

            current_state = self.transitions.get(current_state, {}).get(char)

            if current_state is None:
                return False

        return current_state in self.final_states


# Example usage:
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transitions = {
    'q0': {'0': 'q1', '1': 'q0'},
    'q1': {'0': 'q2', '1': 'q0'},
    'q2': {'0': 'q2', '1': 'q2'}
}
initial_state = 'q0'
final_states = {'q2'}

dfa = DFA(states, alphabet, transitions, initial_state, final_states)

# Validate input strings
print(dfa.validate_input("1001"))  # True
print(dfa.validate_input("10101"))  # False
print(dfa.validate_input("000"))  # True
