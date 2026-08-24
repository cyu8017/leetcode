// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

export function numFriendRequests(ages: number[]): number {
    const count = new Array(121).fill(0);
    for (const age of ages) count[age]++;
    let ans = 0;
    for (let a = 1; a <= 120; a++) {
        if (!count[a]) continue;
        for (let b = 1; b <= 120; b++) {
            if (!count[b]) continue;
            if (b <= 0.5 * a + 7) continue;
            if (b > a) continue;
            if (b > 100 && a < 100) continue;
            ans += count[a] * count[b];
            if (a === b) ans -= count[a];
        }
    }
    return ans;
}
