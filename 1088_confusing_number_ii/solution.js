// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

/**
 * @param {number} n
 * @return {number}
 */
var confusingNumberII = function(n) {
    const rotate = { 0: 0, 1: 1, 6: 9, 8: 8, 9: 6 };
    const digits = [0, 1, 6, 8, 9];
    let ans = 0;

    function isConfusing(num) {
        const original = num;
        let rotated = 0;
        while (num) {
            const d = num % 10;
            rotated = rotated * 10 + rotate[d];
            num = Math.floor(num / 10);
        }
        return rotated !== original;
    }

    function dfs(cur) {
        if (cur > n) return;
        if (cur && isConfusing(cur)) ans++;
        if (cur === 0) {
            for (const d of [1, 6, 8, 9]) dfs(d);
        } else {
            for (const d of digits) dfs(cur * 10 + d);
        }
    }

    dfs(0);
    return ans;
};
