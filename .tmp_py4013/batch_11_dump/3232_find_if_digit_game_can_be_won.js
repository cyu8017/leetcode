// LeetCode 3232 - Find if Digit Game Can Be Won
// https://leetcode.com/problems/find-if-digit-game-can-be-won/

var canAliceWin = function(nums) {
    let a = 0, b = 0;
    for (const x of nums) {
        if (x < 10) a += x;
        else b += x;
    }
    return a !== b;
};
