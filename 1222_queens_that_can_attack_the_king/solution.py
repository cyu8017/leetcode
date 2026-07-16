class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        occupied, answer = {tuple(q) for q in queens}, []
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == dc == 0: continue
                r, c = king[0] + dr, king[1] + dc
                while 0 <= r < 8 and 0 <= c < 8:
                    if (r, c) in occupied:
                        answer.append([r, c])
                        break
                    r, c = r + dr, c + dc
        return answer
