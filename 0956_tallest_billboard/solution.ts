// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

export function tallestBillboard(rods: number[]): number {
    let dp = new Map([[0, 0]]);
    for (const rod of rods) {
        const cur = [...dp.entries()];
        for (const [diff, taller] of cur) {
            const key1 = diff + rod;
            dp.set(key1, Math.max(dp.get(key1) || 0, taller + rod));
            const nd = Math.abs(diff - rod);
            const nt = diff >= rod ? taller : taller - diff + rod;
            dp.set(nd, Math.max(dp.get(nd) || 0, nt));
        }
    }
    return dp.get(0) || 0;
}
