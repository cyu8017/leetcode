// LeetCode 3940 - Limit Occurrences In Sorted Array
// https://leetcode.com/problems/limit-occurrences-in-sorted-array/

export function limitOccurrences(nums: any, k: any): any {
    const n = nums.length;
    let cnt = 1, l = 1;
    for (let r = 1; r < n; r++) {
        if (nums[r] !== nums[r - 1]) cnt = 1;
        else cnt++;
        if (cnt <= k) {
            nums[l] = nums[r];
            l++;
        }
    }
    return nums.slice(0, l);
}
