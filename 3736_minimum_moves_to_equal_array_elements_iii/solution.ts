// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

export function minMoves(nums: any): any {
    let mx = 0, s = 0;
    for (const x of nums) {
        mx = Math.max(mx, x);
        s += x;
    }
    return mx * nums.length - s;
}
