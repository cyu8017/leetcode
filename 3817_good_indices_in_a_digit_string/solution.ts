// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

export function goodIndices(s: any): any {
    const ans = [];
    for (let i = 0; i < s.length; i++) {
        const t = String(i);
        const k = t.length;
        if (i + 1 - k >= 0 && s.substring(i + 1 - k, i + 1) === t) ans.push(i);
    }
    return ans;
}
