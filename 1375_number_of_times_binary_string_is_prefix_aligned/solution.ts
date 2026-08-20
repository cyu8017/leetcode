// LeetCode 1375 - Number Of Times Binary String Is Prefix Aligned
// https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

function numTimesAllBlue(flips: number[]): number {
    let ans = 0, mx = 0;
    for (let i = 0; i < flips.length; i++) {
        mx = Math.max(mx, flips[i]);
        if (mx === i + 1) ans++;
    }
    return ans;
}
