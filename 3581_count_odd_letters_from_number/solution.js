// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

var countOddLetters = function(n) {
    const d = ['zero','one','two','three','four','five','six','seven','eight','nine'];
    let mask = 0;
    while (n > 0) {
        for (const c of d[n % 10]) mask ^= 1 << (c.charCodeAt(0) - 97);
        n = Math.floor(n / 10);
    }
    let cnt = 0;
    while (mask) { cnt += mask & 1; mask >>= 1; }
    return cnt;
};
