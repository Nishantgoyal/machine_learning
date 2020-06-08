import copy


class Bayes:
    def __init__(self, probabilites):
        # Initial Probabilites
        self.probs = copy.deepcopy(probabilites)

    def get_posterior_prob(self, events, event_index):
        new_probs = copy.deepcopy(self.probs)
        joint_probs = [
            self.probs[index] * events[event_index][index]
            for index in range(len(self.probs))
        ]
        total_probs = sum(joint_probs)
        self.probs = [prob / total_probs for prob in joint_probs]


def color():
    # probabilities = [
    #     0.5,  # at R
    #     0.5  # at G
    # ]
    probabilities = [
        1 / 3,  # at A
        1 / 3,  # at B
        1 / 3  # at C
    ]
    events = [
        [
            0.9,  # at A
            0.1,  # at B
            0.1  # at C
        ],  # see R
        [
            0.1,  # at A
            0.9,  # at B
            0.1  # at C
        ]  # see G
    ]
    event_count = 1
    prob = Bayes(probabilities)
    # print(prob.probs)
    for _ in range(event_count):
        prob.get_posterior_prob(events, 0)
        print(prob.probs)


def at_home():
    probabilities = [
        0.4,  # home
        0.6  # gone
    ]
    events = [
        [
            0.01,  # home
            0.3  # gone
        ],  # rain
        [
            0.99,  # home
            0.7  # gone
        ]  # not rain
    ]
    event_count = 1
    prob = Bayes(probabilities)
    for _ in range(event_count):
        prob.get_posterior_prob(events, 0)
        print(prob.probs)


if __name__ == "__main__":
    # color()
    at_home()
