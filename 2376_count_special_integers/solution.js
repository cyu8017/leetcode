// LeetCode 2376 - Count Special Integers
// https://leetcode.com/problems/count-special-integers/

/**
 * @param {number} n
 * @return {number}
 */
var countSpecialNumbers = function(n) {
    const s = String(n);
    const m = s.length;
    let ans = 0;
    let perm = 9;
    for (let i = 1; i < m; i++) {
        ans += perm;
        perm *= (10 - i);
    }
    const used = Array(10).fill(false);
    for (let i = 0; i < m; i++) {
        const start = i === 0 ? 1 : 0;
        const digit = s.charCodeAt(i) - 48;
        for (let d = start; d < digit; d++) {
            if (used[d]) continue;
            let rem = 10 - (i + 1);
            let ways = 1;
            for (let j = i + 1; j < m; j++) {
                ways *= rem;
                rem--;
            }
            ans += ways;
        }
        if (used[digit]) return ans;
        used[digit] = true;
    }
    return ans + 1;
};
