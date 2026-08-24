// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

export function continuousSubarrays(nums: number[]): number {
    let ans = 0, left = 0;
    const minQ = [], maxQ = [];
    for (let right = 0; right < nums.length; right++) {
        while (minQ.length && nums[minQ[minQ.length - 1]] > nums[right]) minQ.pop();
        while (maxQ.length && nums[maxQ[maxQ.length - 1]] < nums[right]) maxQ.pop();
        minQ.push(right);
        maxQ.push(right);
        while (nums[maxQ[0]] - nums[minQ[0]] > 2) {
            left++;
            if (minQ[0] < left) minQ.shift();
            if (maxQ[0] < left) maxQ.shift();
        }
        ans += right - left + 1;
    }
    return ans;
}
