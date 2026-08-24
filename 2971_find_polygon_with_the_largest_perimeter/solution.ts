// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

export function largestPerimeter(nums: any): any {
    nums.sort((a, b) => a - b);
    let sum = 0;
    for (const v of nums) sum += v;
    for (let i = nums.length - 1; i >= 2; i--) {
        sum -= nums[i];
        if (sum > nums[i]) return sum + nums[i];
    }
    return -1;
}
