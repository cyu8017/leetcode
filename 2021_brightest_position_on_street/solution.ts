// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

export function brightestPosition(lights: number[][]): number {
    const events = [];
    for (const light of lights) {
        const pos = light[0], r = light[1];
        events.push([pos - r, 1]);
        events.push([pos + r + 1, -1]);
    }
    events.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : b[1] - a[1]);
    let best = 0, cur = 0, ans = 0;
    for (const e of events) {
        cur += e[1];
        if (cur > best) { best = cur; ans = e[0]; }
    }
    return ans;
}
