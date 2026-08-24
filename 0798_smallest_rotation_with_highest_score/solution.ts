// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

export function bestRotation(nums: number[]): number {
    const n = nums.length;
    const change = new Array(n).fill(1);
    for (let i = 0; i < n; i++) change[(i - nums[i] + 1 + n) % n] -= 1;
    for (let i = 1; i < n; i++) change[i] += change[i - 1];
    let best = 0;
    for (let i = 1; i < n; i++) if (change[i] > change[best]) best = i;
    return best;
}
