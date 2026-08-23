// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

class Solution {
    findPermutation(s) {
        const stack = [1];
        const result = [];
        for (const ch of s) {
            if (ch === "I") {
                while (stack.length) result.push(stack.pop());
            }
            stack.push(stack.length + result.length + 1);
        }
        while (stack.length) result.push(stack.pop());
        return result;
    }
}

module.exports = { Solution };
