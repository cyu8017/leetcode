// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

export function matchReplacement(s: any, sub: any, mappings: any): any {
    const allow = new Set();
    for (const m of mappings) allow.add((m[0].charCodeAt(0) << 8) | m[1].charCodeAt(0));
    const n = s.length, mlen = sub.length;
    for (let i = 0; i + mlen <= n; i++) {
        let ok = true;
        for (let j = 0; j < mlen; j++) {
            const a = s[i + j], b = sub[j];
            if (a === b || allow.has((b.charCodeAt(0) << 8) | a.charCodeAt(0))) continue;
            ok = false;
            break;
        }
        if (ok) return true;
    }
    return false;
}
