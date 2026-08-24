// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

export function minCostSetTime(startAt: number, moveCost: number, pushCost: number, targetSeconds: number): number {
    const cost = (mins, secs) => {
        if (mins < 0 || mins > 99 || secs < 0 || secs > 99) return Math.floor(Number.MAX_SAFE_INTEGER / 2);
        let s;
        if (mins > 0) s = String(mins) + String(Math.floor(secs / 10)) + String(secs % 10);
        else s = String(secs);
        let cur = String(startAt);
        let ans = 0;
        for (let i = 0; i < s.length; i++) {
            const c = s[i];
            if (c !== cur) { ans += moveCost; cur = c; }
            ans += pushCost;
        }
        return ans;
    };
    const mins = Math.floor(targetSeconds / 60), secs = targetSeconds % 60;
    let ans = cost(mins, secs);
    if (mins > 0) ans = Math.min(ans, cost(mins - 1, secs + 60));
    return ans;
}
