// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

export function destroyTargets(nums: number[], space: number): number {
    const cnt = new Map();
    for (const x of nums) {
        const m = x % space;
        cnt.set(m, (cnt.get(m) || 0) + 1);
    }
    let bestCnt = 0;
    for (const c of cnt.values()) if (c > bestCnt) bestCnt = c;
    let ans = 1000000000;
    for (const [key, value] of cnt) {
        if (value === bestCnt) {
            for (const x of nums) {
                if (x % space === key && x < ans) ans = x;
            }
        }
    }
    return ans;
}
