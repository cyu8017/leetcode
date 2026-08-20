"use strict";
// LeetCode 1365 - How Many Numbers Are Smaller Than The Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
function smallerNumbersThanCurrent(nums) {
    const sorted = [...nums].sort((a, b) => a - b);
    return nums.map((x) => sorted.indexOf(x));
}
