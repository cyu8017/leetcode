# LeetCode 0299 - Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_counts: dict[str, int] = {}
        guess_counts: dict[str, int] = {}
        for secret_digit, guess_digit in zip(secret, guess):
            if secret_digit == guess_digit:
                bulls += 1
            else:
                secret_counts[secret_digit] = secret_counts.get(secret_digit, 0) + 1
                guess_counts[guess_digit] = guess_counts.get(guess_digit, 0) + 1
        cows = sum(min(guess_counts[digit], secret_counts.get(digit, 0)) for digit in guess_counts)
        return f"{bulls}A{cows}B"
