"use strict";
// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/
function countMatches(items, ruleKey, ruleValue) {
    const idx = { type: 0, color: 1, name: 2 }[ruleKey];
    let count = 0;
    for (const item of items) {
        if (item[idx] === ruleValue) {
            count++;
        }
    }
    return count;
}
