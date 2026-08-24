// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

/**
 * @param {number[]} mapping
 * @param {number[]} nums
 * @return {number[]}
 */
var sortJumbled = function(mapping, nums) {
    const mapVal = (x) => {
        if (x === 0) return mapping[0];
        const digits = [];
        while (x > 0) { digits.push(x % 10); x = Math.floor(x / 10); }
        let res = 0;
        for (let i = digits.length - 1; i >= 0; i--)
            res = res * 10 + mapping[digits[i]];
        return res;
    };
    const n = nums.length;
    const arr = Array.from({length: n}, (_, i) => [mapVal(nums[i]), i, nums[i]]);
    arr.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    return arr.map(x => x[2]);
};
