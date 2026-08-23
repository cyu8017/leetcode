// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var lastVisitedIntegers = function(nums) {
    const seen = [], ans = [];
    let k = 0;
    for (const v of nums) {
        if (v !== -1) {
            seen.push(v);
            k = 0;
        } else {
            k++;
            if (k > seen.length) ans.push(-1);
            else ans.push(seen[seen.length - k]);
        }
    }
    return ans;
};
