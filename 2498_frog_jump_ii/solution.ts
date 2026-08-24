// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

export function maxJump(stones: number[]): number {
    let ans = stones[1] - stones[0];
    for (let i = 2; i < stones.length; i++) {
        const diff = stones[i] - stones[i - 2];
        if (diff > ans) ans = diff;
    }
    return ans;
}
