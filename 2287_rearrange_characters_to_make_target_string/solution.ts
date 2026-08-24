// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

export function rearrangeCharacters(s: any, target: any): any {
    const sc = new Array(26).fill(0), tc = new Array(26).fill(0);
    for (const c of s) sc[c.charCodeAt(0) - 97]++;
    for (const c of target) tc[c.charCodeAt(0) - 97]++;
    let ans = Infinity;
    for (let i = 0; i < 26; i++) {
        if (tc[i] === 0) continue;
        ans = Math.min(ans, Math.floor(sc[i] / tc[i]));
    }
    return ans;
}
