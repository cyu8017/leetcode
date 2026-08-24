# LeetCode 2288 - Apply Discount to Prices
# https://leetcode.com/problems/apply-discount-to-prices/


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        parts = sentence.split(" ")
        for i, part in enumerate(parts):
            if len(part) >= 2 and part[0] == "$":
                ok = True
                for j in range(1, len(part)):
                    if part[j] < "0" or part[j] > "9":
                        ok = False
                        break
                if ok:
                    val = int(part[1:])
                    price = val * (100 - discount) / 100
                    parts[i] = f"${price:.2f}"
        return " ".join(parts)
