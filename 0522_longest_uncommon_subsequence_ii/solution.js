// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution {
    findLUSlength(strs) {
        const isSubsequence = (target, source) => {
            let index = 0;
            for (const char of source) {
                if (index < target.length && target[index] === char) index += 1;
            }
            return index === target.length;
        };
        let result = -1;
        for (let i = 0; i < strs.length; i += 1) {
            if (strs.some((other, j) => i !== j && isSubsequence(strs[i], other))) continue;
            result = Math.max(result, strs[i].length);
        }
        return result;
    }
}

module.exports = { Solution };
