// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

export function hasSpecialSubstring(s: any, k: any): any {
    const n = s.length;
    for (let i = 0; i + k <= n; i++) {
        let ok = true;
        for (let j = i + 1; j < i + k; j++) {
            if (s[j] !== s[i]) { ok = false; break; }
        }
        if (!ok) continue;
        if (i > 0 && s[i - 1] === s[i]) continue;
        if (i + k < n && s[i + k] === s[i]) continue;
        return true;
    }
    return false;
}
