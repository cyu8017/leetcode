// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

export function appealSum(s: string): number {
    const last = new Array(26).fill(-1);
    let ans = 0, cur = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s.charCodeAt(i) - 97;
        cur += i - last[c];
        last[c] = i;
        ans += cur;
    }
    return ans;
}
