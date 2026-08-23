// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

/**
 * @param {number[]} nums
 * @return {number}
 */
var deleteAndEarn = function(nums) {
    if (nums.length === 0) return 0;
    let maxNum = 0;
    for (const num of nums) maxNum = Math.max(maxNum, num);
    const points = new Array(maxNum + 1).fill(0);
    for (const num of nums) points[num] += num;
    let take = 0, skip = 0;
    for (const value of points) {
        const newTake = skip + value;
        const newSkip = Math.max(skip, take);
        take = newTake;
        skip = newSkip;
    }
    return Math.max(take, skip);
};
