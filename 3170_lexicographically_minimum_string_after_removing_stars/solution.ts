// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

export function clearStars(s: string): string {
    const g = Array.from({ length: 26 }, () => []);
    const n = s.length;
    const rem = new Array(n).fill(false);
    for (let i = 0; i < n; i++) {
        if (s[i] === '*') {
            rem[i] = true;
            for (let j = 0; j < 26; j++) {
                if (g[j].length) {
                    rem[g[j].pop()] = true;
                    break;
                }
            }
        } else {
            g[s.charCodeAt(i) - 97].push(i);
        }
    }
    let ans = '';
    for (let i = 0; i < n; i++) if (!rem[i]) ans += s[i];
    return ans;
}
