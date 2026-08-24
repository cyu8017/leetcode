// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

export function convertTime(current: string, correct: string): number {
    const toMin = (t) => (t.charCodeAt(0) - 48) * 600 + (t.charCodeAt(1) - 48) * 60
        + (t.charCodeAt(3) - 48) * 10 + (t.charCodeAt(4) - 48);
    let diff = toMin(correct) - toMin(current);
    let ans = 0;
    for (const step of [60, 15, 5, 1]) {
        ans += Math.floor(diff / step);
        diff %= step;
    }
    return ans;
}
