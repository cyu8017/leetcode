// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

export function countMajoritySubarrays(nums: any, target: any): any {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let cnt = 0;
        for (let j = i; j < n; j++) {
            if (nums[j] === target) cnt++;
            if (cnt * 2 > j - i + 1) ans++;
        }
    }
    return ans;
}
