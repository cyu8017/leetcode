// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

class Solution {
    func corpFlightBookings(_ bookings: [[Int]], _ n: Int) -> [Int] {
        var diff = [Int](repeating: 0, count: n + 1)
        for b in bookings {
            diff[b[0] - 1] += b[2]
            diff[b[1]] -= b[2]
        }
        var ans: [Int] = []
        var cur = 0
        for i in 0..<n {
            cur += diff[i]
            ans.append(cur)
        }
        return ans
    }
}
