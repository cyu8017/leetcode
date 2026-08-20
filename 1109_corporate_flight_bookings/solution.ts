// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

function corpFlightBookings(bookings: number[][], n: number): number[] {
    const diff = Array(n + 1).fill(0);
    for (const [first, last, seats] of bookings) {
        diff[first - 1] += seats;
        diff[last] -= seats;
    }
    const ans = [];
    let cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        ans.push(cur);
    }
    return ans;
}
