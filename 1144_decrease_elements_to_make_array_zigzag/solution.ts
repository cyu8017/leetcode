// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

function movesToMakeZigzag(nums: number[]): number {
    const cost = (start) => {
        let ans = 0;
        for (let i = start; i < nums.length; i += 2) {
            const left = i ? nums[i - 1] : Infinity;
            const right = i + 1 < nums.length ? nums[i + 1] : Infinity;
            ans += Math.max(0, nums[i] - Math.min(left, right) + 1);
        }
        return ans;
    };
    return Math.min(cost(0), cost(1));
}
