// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

/**
 * @param {string} left
 * @param {string} right
 * @return {number}
 */
var superpalindromesInRange = function(left, right) {
    const L = BigInt(left), R = BigInt(right);
    const isPal = (x) => {
        const s = x.toString();
        const n = s.length;
        for (let i = 0; i < n / 2; i++) if (s[i] !== s[n - 1 - i]) return false;
        return true;
    };
    let ans = 0;
    for (let k = 1n; k <= 100000n; k++) {
        const s = k.toString();
        const rev = s.split("").reverse().join("");
        const pal = BigInt(s + rev);
        const sq = pal * pal;
        if (sq > R) break;
        if (sq >= L && isPal(sq)) ans++;
    }
    for (let k = 1n; k <= 100000n; k++) {
        const s = k.toString();
        const rev = s.slice(0, -1).split("").reverse().join("");
        const pal = BigInt(s + rev);
        const sq = pal * pal;
        if (sq > R) break;
        if (sq >= L && isPal(sq)) ans++;
    }
    return ans;
};
