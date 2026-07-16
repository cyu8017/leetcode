// LeetCode 0229 - Majority Element II
// https://leetcode.com/problems/majority-element-ii/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    let candidate1 = null;
    let candidate2 = null;
    let count1 = 0;
    let count2 = 0;

    for (const num of nums) {
        if (num === candidate1) {
            count1 += 1;
        } else if (num === candidate2) {
            count2 += 1;
        } else if (count1 === 0) {
            candidate1 = num;
            count1 = 1;
        } else if (count2 === 0) {
            candidate2 = num;
            count2 = 1;
        } else {
            count1 -= 1;
            count2 -= 1;
        }
    }

    count1 = 0;
    count2 = 0;
    for (const num of nums) {
        if (num === candidate1) {
            count1 += 1;
        } else if (num === candidate2) {
            count2 += 1;
        }
    }

    const threshold = Math.floor(nums.length / 3);
    const result = [];
    if (count1 > threshold) {
        result.push(candidate1);
    }
    if (candidate2 !== candidate1 && count2 > threshold) {
        result.push(candidate2);
    }
    return result;
};
