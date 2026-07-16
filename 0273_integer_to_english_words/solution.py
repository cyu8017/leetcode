# LeetCode 0273 - Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/


class Solution:
    ONES = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    TENS = [
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def convert_chunk(value: int) -> str:
            if value == 0:
                return ""
            if value < 20:
                return self.ONES[value]
            if value < 100:
                tens = self.TENS[value // 10]
                ones = self.ONES[value % 10]
                return tens if not ones else f"{tens} {ones}"
            hundreds = self.ONES[value // 100]
            remainder = convert_chunk(value % 100)
            return hundreds + " Hundred" + (f" {remainder}" if remainder else "")

        parts: list[str] = []
        chunk_index = 0
        while num > 0:
            chunk = num % 1000
            if chunk:
                chunk_words = convert_chunk(chunk)
                if self.THOUSANDS[chunk_index]:
                    chunk_words += f" {self.THOUSANDS[chunk_index]}"
                parts.append(chunk_words)
            num //= 1000
            chunk_index += 1
        return " ".join(reversed(parts))
