// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

export function maximumCostSubstring(s: string, chars: string, vals: number[]): number {
    const val = new Array(26);
    for (let i = 0; i < 26; ++i) val[i] = i + 1;
    for (let i = 0; i < chars.length; ++i) val[chars.charCodeAt(i) - 97] = vals[i];
    let best = 0, cur = 0;
    for (const c of s) {
        cur += val[c.charCodeAt(0) - 97];
        if (cur < 0) cur = 0;
        if (cur > best) best = cur;
    }
    return best;
}
