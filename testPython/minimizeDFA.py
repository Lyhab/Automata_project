from collections import deque


class DFA:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def minimize(self):
        # Step 1: Partition the states into two sets - final and non-final
        final_states = set(self.final_states)
        non_final_states = set(self.states) - final_states

        # Initialize the partitions
        partitions = [final_states, non_final_states]
        new_partitions = []

        # Step 2: Partition refinement
        while True:
            for partition in partitions:
                split = self.split_partition(partition, partitions, new_partitions)
                if split:
                    new_partitions.append(split)

            if new_partitions == partitions:
                break

            partitions = new_partitions
            new_partitions = []

        # Step 3: Create the minimized DFA
        minimized_states = []
        minimized_transitions = {}
        minimized_initial_state = None
        minimized_final_states = set()

        for partition in partitions:
            state_name = ','.join(sorted(partition))
            minimized_states.append(state_name)

            for char in self.alphabet:
                next_partition = self.get_next_partition(partition, char, partitions)
                next_state_name = ','.join(sorted(next_partition))
                minimized_transitions[state_name, char] = next_state_name

            if self.initial_state in partition:
                minimized_initial_state = state_name

            if partition & final_states:
                minimized_final_states.add(state_name)

        return DFA(minimized_states, self.alphabet, minimized_transitions,
                   minimized_initial_state, minimized_final_states)

    def split_partition(self, partition, partitions, new_partitions):
        if len(partition) <= 1:
            return None

        transitions = {}
        split = set()

        for state in partition:
            for char in self.alphabet:
                next_state = self.transitions.get(state, {}).get(char)
                next_partition = self.get_next_partition(partition, char, partitions)

                if next_state not in transitions:
                    transitions[next_state] = {}

                transitions[next_state][next_partition] = True

            if len(transitions) > 1:
                split.add(state)

        if len(split) > 0:
            for state in split:
                partition.remove(state)

            return split

        return None

    def get_next_partition(self, partition, char, partitions):
        for subset in partition:
            for state in subset.split(','):
                next_state = self.transitions.get(state, {}).get(char)
                if next_state is not None:
                    for p in partitions:
                        if next_state in p:
                            return p

        return None


# Example usage:
states = {'q0', 'q1', 'q2', 'q3'}
alphabet = {'0', '1'}
transitions = {
    'q0': {'0': 'q1', '1': 'q2'},
    'q1': {'0': 'q3', '1': 'q2'},
    'q2': {'0': 'q1', '1': 'q2'},
    'q3': {'0': 'q3', '1': 'q2'}
}
initial_state = 'q0'
final_states = {'q3'}

dfa = DFA(states, alphabet, transitions, initial_state, final_states)

# Minimize the DFA
minimized_dfa = dfa.minimize()

# Print the minimized DFA properties
print("Minimized states:", minimized_dfa.states)
print("Minimized transitions:", minimized_dfa.transitions)
print("Minimized initial state:", minimized_dfa.initial_state)
print("Minimized final states:", minimized_dfa.final_states)
