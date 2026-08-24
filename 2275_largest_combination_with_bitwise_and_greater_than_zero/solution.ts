// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

export function largestCombination(candidates: number[]): number {
    let ans = 0;
    for (let bit = 0; bit < 24; bit++) {
        let cnt = 0;
        for (const x of candidates) if (((x >> bit) & 1) !== 0) cnt++;
        ans = Math.max(ans, cnt);
    }
    return ans;
}
