// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

export function meetRequirement(n: number, lights: number[][], requirement: number[]): number {
    const diff = new Array(n + 1).fill(0);
    for (const light of lights) {
        const pos = light[0], r = light[1];
        const l = Math.max(0, pos - r);
        const rr = Math.min(n - 1, pos + r);
        diff[l]++;
        diff[rr + 1]--;
    }
    let ans = 0, cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        if (cur >= requirement[i]) ans++;
    }
    return ans;
}
