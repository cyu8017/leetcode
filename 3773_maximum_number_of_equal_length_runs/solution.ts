// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

export function maxSameLengthRuns(s: any): any {
    const cnt = new Map();
    const n = s.length;
    let ans = 0;
    for (let i = 0; i < n; ) {
        let j = i + 1;
        while (j < n && s[j] === s[i]) j++;
        const m = j - i;
        cnt.set(m, (cnt.get(m) || 0) + 1);
        ans = Math.max(ans, cnt.get(m));
        i = j;
    }
    return ans;
}
