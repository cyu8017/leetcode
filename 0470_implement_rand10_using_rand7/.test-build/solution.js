"use strict";
// LeetCode 0470 - Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Solution = void 0;
exports.rand7 = rand7;
class Solution {
    rand10() {
        while (true) {
            const num = (rand7() - 1) * 7 + rand7();
            if (num <= 40)
                return ((num - 1) % 10) + 1;
        }
    }
}
exports.Solution = Solution;
function rand7() {
    throw new Error("rand7 must be provided by the test harness");
}
