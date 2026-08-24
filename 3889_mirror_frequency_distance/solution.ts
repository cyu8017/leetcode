// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

export function mirrorFrequency(s: any): any {
    const freq = new Map();
    for (const c of s) freq.set(c, (freq.get(c) || 0) + 1);
    let ans = 0;
    const vis = new Map();
    for (const [c, v] of freq.entries()) {
        let m;
        if (c >= 'a' && c <= 'z') m = String.fromCharCode(97 + 25 - (c.charCodeAt(0) - 97));
        else m = String.fromCharCode(48 + (9 - (c.charCodeAt(0) - 48)));
        if (vis.get(m) === true) continue;
        vis.set(c, true);
        const mv = freq.get(m) || 0;
        ans += Math.abs(v - mv);
    }
    return ans;
}
