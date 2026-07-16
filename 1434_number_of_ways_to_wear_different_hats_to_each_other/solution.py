class Solution:
    def numberWays(self, hats):
        mod, people = 1_000_000_007, len(hats)
        wearers = [[] for _ in range(41)]
        for person, choices in enumerate(hats):
            for hat in choices:
                wearers[hat].append(person)
        dp = [0] * (1 << people)
        dp[0] = 1
        for hat in range(1, 41):
            nxt = dp[:]
            for mask, ways in enumerate(dp):
                for person in wearers[hat]:
                    if not mask >> person & 1:
                        nxt[mask | (1 << person)] = (nxt[mask | (1 << person)] + ways) % mod
            dp = nxt
        return dp[-1]
