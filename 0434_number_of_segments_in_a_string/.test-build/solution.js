"use strict";
// LeetCode 0434 - Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Solution = void 0;
class Solution {
    countSegments(s) {
        let count = 0;
        let inSegment = false;
        for (const char of s) {
            if (char !== " ") {
                if (!inSegment) {
                    count += 1;
                    inSegment = true;
                }
            }
            else {
                inSegment = false;
            }
        }
        return count;
    }
}
exports.Solution = Solution;
