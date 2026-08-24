// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

export function maxDistance(s: any, k: any): any {
    let ans = 0;
    let lat = 0, lon = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c === "N") lat++;
        else if (c === "S") lat--;
        else if (c === "E") lon++;
        else lon--;
        const md = Math.abs(lat) + Math.abs(lon);
        const steps = i + 1;
        let cur = md + 2 * k;
        if (cur > steps) cur = steps;
        if (cur > ans) ans = cur;
    }
    return ans;
}
