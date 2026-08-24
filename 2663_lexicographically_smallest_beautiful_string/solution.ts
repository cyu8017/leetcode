// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

export function smallestBeautifulString(s: any, k: any): any {
    const n = s.length;
    const b = s.split("");
    for (let i = n - 1; i >= 0; i--) {
        for (let code = b[i].charCodeAt(0) + 1; code < 97 + k; code++) {
            const c = String.fromCharCode(code);
            if ((i > 0 && c === b[i - 1]) || (i > 1 && c === b[i - 2])) continue;
            b[i] = c;
            for (let j = i + 1; j < n; j++) {
                for (let nc = 97; nc < 97 + k; nc++) {
                    const ch = String.fromCharCode(nc);
                    if ((j > 0 && ch === b[j - 1]) || (j > 1 && ch === b[j - 2])) continue;
                    b[j] = ch;
                    break;
                }
            }
            return b.join("");
        }
    }
    return "";
}
