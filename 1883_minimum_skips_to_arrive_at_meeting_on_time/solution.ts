// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

function minSkips(dist: number[], speed: number, hoursBefore: number): number {
    const limit = hoursBefore * speed;
    let dp = new Array(dist.length + 1).fill(Infinity);
    dp[0] = 0;
    for (const road of dist) {
        const nxt = new Array(dist.length + 1).fill(Infinity);
        for (let skips = 0; skips < dist.length; skips++) {
            if (dp[skips] === Infinity) continue;
            nxt[skips] = Math.min(
                nxt[skips],
                Math.floor((dp[skips] + road + speed - 1) / speed) * speed
            );
            nxt[skips + 1] = Math.min(nxt[skips + 1], dp[skips] + road);
        }
        dp = nxt;
    }
    for (let skips = 0; skips < dp.length; skips++) {
        if (dp[skips] <= limit) return skips;
    }
    return -1;
}
