// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

/**
 * @param {number} n
 * @return {number}
 */
var primePalindrome = function(n) {
    if (n <= 2) return 2;
    if (n <= 3) return 3;
    if (n <= 5) return 5;
    if (n <= 7) return 7;
    if (n <= 11) return 11;
    const isPrime = (x) => {
        if (x < 2) return false;
        if (x % 2 === 0) return x === 2;
        for (let d = 3; d * d <= x; d += 2) if (x % d === 0) return false;
        return true;
    };
    for (let length = 1; length <= 5; length++) {
        const start = Math.pow(10, length - 1);
        const end = Math.pow(10, length);
        for (let root = start; root < end; root++) {
            const s = String(root);
            let pal = s;
            for (let i = s.length - 2; i >= 0; i--) pal += s[i];
            const val = parseInt(pal, 10);
            if (val >= n && isPrime(val)) return val;
        }
    }
    return 0;
};
