// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

/**
 * @param {string} n
 * @return {string}
 */
var nearestPalindromic = function(n) {
    const length = n.length;
    const number = BigInt(n);
    const candidates = [];
    const pow10 = (exp) => {
        let value = 1n;
        for (let i = 0; i < exp; ++i) value *= 10n;
        return value;
    };
    const makePalindrome = (half, len) => {
        const text = half.toString();
        let pal = text;
        if (len % 2 === 0) {
            for (let i = text.length - 1; i >= 0; --i) pal += text[i];
        } else {
            for (let i = text.length - 2; i >= 0; --i) pal += text[i];
        }
        return BigInt(pal);
    };
    candidates.push(pow10(length - 1) - 1n);
    candidates.push(pow10(length) + 1n);
    const prefix = BigInt(n.substring(0, Math.floor((length + 1) / 2)));
    for (let half = prefix - 1n; half <= prefix + 1n; ++half) {
        candidates.push(makePalindrome(half, length));
    }
    let best = -1n;
    let bestDiff = null;
    for (const candidate of candidates) {
        if (candidate === number) continue;
        const diff = candidate > number ? candidate - number : number - candidate;
        if (bestDiff === null || diff < bestDiff || (diff === bestDiff && candidate < best)) {
            best = candidate;
            bestDiff = diff;
        }
    }
    return best.toString();
};
