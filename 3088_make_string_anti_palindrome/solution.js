// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

/**
 * @param {string} s
 * @return {string}
 */
var makeAntiPalindrome = function(s) {
    const arr = s.split('').sort();
    const n = arr.length;
    const m = Math.floor(n / 2);
    if (arr[m] === arr[m - 1]) {
        let i = m;
        while (i < n && arr[i] === arr[i - 1]) i++;
        for (let j = m; j < n && arr[j] === arr[n - j - 1]; i++, j++) {
            if (i >= n) return "-1";
            const tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
        }
    }
    return arr.join('');
};
