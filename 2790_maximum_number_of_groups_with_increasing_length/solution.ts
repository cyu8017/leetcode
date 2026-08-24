// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

export function maxIncreasingGroups(usageLimits: number[]): number {
    const arr = usageLimits.slice().sort((a, b) => a - b);
    let ans = 0, sum = 0;
    for (const v of arr) {
        sum += v;
        const need = (ans + 1) * (ans + 2) / 2;
        if (sum >= need) ans++;
    }
    return ans;
}
