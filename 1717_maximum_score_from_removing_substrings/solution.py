class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(text: str, pair: str, score: int) -> tuple[str, int]:
            stack = []
            gained = 0
            for ch in text:
                if stack and stack[-1] == pair[0] and ch == pair[1]:
                    stack.pop()
                    gained += score
                else:
                    stack.append(ch)
            return "".join(stack), gained

        if x >= y:
            rest, first = remove(s, "ab", x)
            _, second = remove(rest, "ba", y)
        else:
            rest, first = remove(s, "ba", y)
            _, second = remove(rest, "ab", x)
        return first + second
