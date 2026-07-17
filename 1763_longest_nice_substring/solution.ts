// LeetCode 1763 - Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/

function longestNiceSubstring(s: string): string {
    let bestStart = 0;
    let bestLen = 0;
    for (let i = 0; i < s.length; i++) {
        let lower = 0;
        let upper = 0;
        for (let j = i; j < s.length; j++) {
            const code = s.charCodeAt(j);
            if (code >= 97) {
                lower |= 1 << (code - 97);
            } else {
                upper |= 1 << (code - 65);
            }
            if (lower === upper && j - i + 1 > bestLen) {
                bestStart = i;
                bestLen = j - i + 1;
            }
        }
    }
    return s.slice(bestStart, bestStart + bestLen);
}
