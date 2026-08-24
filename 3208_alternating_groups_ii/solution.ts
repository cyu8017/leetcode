// LeetCode 3208 - Alternating Groups II
// https://leetcode.com/problems/alternating-groups-ii/

export function numberOfAlternatingGroups(colors: any, k: any): any {
    const n = colors.length;
    let cnt = 0, ans = 0;
    for (let i = 0; i < n * 2; i++) {
        if (i > 0 && colors[i % n] === colors[(i - 1) % n]) cnt = 1;
        else cnt++;
        if (i >= n && cnt >= k) ans++;
    }
    return ans;
}
