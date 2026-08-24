// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution {
    func minimumTime(_ time: [Int], _ totalTrips: Int) -> Int {
        let mn = time.min()!
        var lo = 1, hi = mn * totalTrips
        while lo < hi {
            let mid = (lo + hi) / 2
            var trips = 0, ok = false
            for t in time {
                trips += mid / t
                if trips >= totalTrips { ok = true; break }
            }
            if ok { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }
}
