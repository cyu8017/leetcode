// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numberOfSubarrays = function(nums, k) {
    const frequency = new Map([[0, 1]]);
    let odd = 0, answer = 0;
    for (const x of nums) {
        odd += x & 1;
        answer += frequency.get(odd - k) || 0;
        frequency.set(odd, (frequency.get(odd) || 0) + 1);
    }
    return answer;
};
