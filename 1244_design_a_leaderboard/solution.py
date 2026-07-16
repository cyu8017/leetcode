from collections import defaultdict

class Leaderboard:
    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.scores.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        self.scores.pop(playerId, None)
