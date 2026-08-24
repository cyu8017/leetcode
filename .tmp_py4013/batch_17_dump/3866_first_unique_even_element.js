// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

var firstUniqueEven = function(nums) {
    const cnt = new Array(101).fill(0);
    for (const x of nums) cnt[x]++;
    for (const x of nums) {
        if (x % 2 === 0 && cnt[x] === 1) return x;
    }
    return -1;
};
