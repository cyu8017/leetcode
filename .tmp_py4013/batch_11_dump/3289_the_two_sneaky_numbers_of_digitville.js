// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

var getSneakyNumbers = function(nums) {
    const seen = new Set();
    const ans = [];
    for (const x of nums) {
        if (seen.has(x)) ans.push(x);
        else seen.add(x);
    }
    return ans;
};
