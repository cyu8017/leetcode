// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

export function possiblyEquals(s1: string, s2: string): boolean {
    const memo = new Map();
    const isDigit = (c) => c >= '0' && c <= '9';
    const dfs = (i, j, diff) => {
        const key = i + "," + j + "," + diff;
        if (memo.has(key)) return memo.get(key);
        const n = s1.length, m = s2.length;
        if (i === n && j === m) { memo.set(key, diff === 0); return diff === 0; }
        let res = false;
        if (diff === 0 && i < n && j < m && !isDigit(s1[i]) && !isDigit(s2[j])) {
            if (s1[i] === s2[j]) res = dfs(i + 1, j + 1, 0);
        } else if (diff > 0 && i < n && !isDigit(s1[i])) {
            res = dfs(i + 1, j, diff - 1);
        } else if (diff < 0 && j < m && !isDigit(s2[j])) {
            res = dfs(i, j + 1, diff + 1);
        }
        if (!res && i < n && isDigit(s1[i])) {
            let val = 0;
            for (let p = i; p < n && isDigit(s1[p]); p++) {
                val = val * 10 + (s1.charCodeAt(p) - 48);
                if (dfs(p + 1, j, diff + val)) { res = true; break; }
            }
        }
        if (!res && j < m && isDigit(s2[j])) {
            let val = 0;
            for (let p = j; p < m && isDigit(s2[p]); p++) {
                val = val * 10 + (s2.charCodeAt(p) - 48);
                if (dfs(i, p + 1, diff - val)) { res = true; break; }
            }
        }
        memo.set(key, res);
        return res;
    };
    return dfs(0, 0, 0);
}
