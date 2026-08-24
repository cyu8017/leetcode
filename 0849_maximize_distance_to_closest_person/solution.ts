// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

export function maxDistToClosest(seats: number[]): number {
    const n = seats.length;
    let prev = -1, ans = 0;
    for (let i = 0; i < n; i++) {
        if (seats[i] === 1) {
            if (prev === -1) ans = i;
            else ans = Math.max(ans, Math.floor((i - prev) / 2));
            prev = i;
        }
    }
    return Math.max(ans, n - 1 - prev);
}
