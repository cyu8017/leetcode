// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

var isPossibleToSplit = function(nums) {
    const cnt = new Array(101).fill(0);
    for (const x of nums) {
        cnt[x]++;
        if (cnt[x] >= 3) return false;
    }
    return true;
};
