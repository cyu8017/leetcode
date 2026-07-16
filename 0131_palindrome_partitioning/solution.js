// LeetCode 0131 - Palindrome Partitioning
// https://leetcode.com/problems/palindrome-partitioning/

/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    const result = [];

    const isPalindrome = (left, right) => {
        while (left < right) {
            if (s[left] !== s[right]) return false;
            left += 1;
            right -= 1;
        }
        return true;
    };

    const dfs = (start, path) => {
        if (start === s.length) {
            result.push([...path]);
            return;
        }
        for (let end = start; end < s.length; end += 1) {
            if (isPalindrome(start, end)) {
                path.push(s.slice(start, end + 1));
                dfs(end + 1, path);
                path.pop();
            }
        }
    };

    dfs(0, []);
    return result;
};