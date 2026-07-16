// LeetCode 0017 - Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits.length === 0) {
        return [];
    }

    const mapping = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    };
    const result = [];

    function backtrack(index, path) {
        if (index === digits.length) {
            result.push(path.join(""));
            return;
        }
        for (const ch of mapping[digits[index]]) {
            path.push(ch);
            backtrack(index + 1, path);
            path.pop();
        }
    }

    backtrack(0, []);
    return result;
};
