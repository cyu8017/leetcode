// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

export function maximumBags(capacity: any, rocks: any, additionalRocks: any): any {
    const need = capacity.map((c, i) => c - rocks[i]);
    need.sort((a, b) => a - b);
    let ans = 0;
    for (const n of need) {
        if (additionalRocks < n) break;
        additionalRocks -= n;
        ans++;
    }
    return ans;
}
