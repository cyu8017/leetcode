// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

export class Solution {
    makesquare(matchsticks: number[]): boolean {
        if (!matchsticks.length) return false;
        const total = matchsticks.reduce((sum, value) => sum + value, 0);
        if (total % 4) return false;
        const side = total / 4;
        const sticks = [...matchsticks].sort((a, b) => b - a);

        const dfs = (index: number, sides: number[]): boolean => {
            if (index === sticks.length) {
                return sides[0] === side && new Set(sides).size === 1;
            }
            const length = sticks[index];
            for (let sideIndex = 0; sideIndex < 4; sideIndex += 1) {
                if (sides[sideIndex] + length > side) continue;
                if (sideIndex > 0 && sides[sideIndex] === sides[sideIndex - 1]) continue;
                sides[sideIndex] += length;
                if (dfs(index + 1, sides)) return true;
                sides[sideIndex] -= length;
            }
            return false;
        };

        return dfs(0, [0, 0, 0, 0]);
    }
}
