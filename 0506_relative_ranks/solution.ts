// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

export class Solution {
    findRelativeRanks(score: number[]): string[] {
        const medals: Record<number, string> = { 1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal" };
        const order = [...score.keys()].sort((a, b) => score[b] - score[a]);
        const result = Array<string>(score.length);
        order.forEach((index, rank) => {
            result[index] = medals[rank + 1] || String(rank + 1);
        });
        return result;
    }
}
