// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

function maxResult(nums: number[], k: number): number {
    const q: [number, number][] = [[0, nums[0]]];
    for (let i = 1; i < nums.length; i++) {
        while (q[0][0] < i - k) q.shift();
        const score = nums[i] + q[0][1];
        while (q.length && q[q.length - 1][1] <= score) q.pop();
        q.push([i, score]);
    }
    return q[q.length - 1][1];
}
