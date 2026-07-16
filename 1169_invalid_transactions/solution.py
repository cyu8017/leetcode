# LeetCode 1169 - Invalid Transactions
# https://leetcode.com/problems/invalid-transactions/

class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(",")
            parsed.append((name, int(time), int(amount), city, t))
        invalid = set()
        for i, (name, time, amount, city, raw) in enumerate(parsed):
            if amount > 1000:
                invalid.add(raw)
            for j, (name2, time2, amount2, city2, raw2) in enumerate(parsed):
                if i != j and name == name2 and city != city2 and abs(time - time2) <= 60:
                    invalid.add(raw)
                    invalid.add(raw2)
        return list(invalid)
