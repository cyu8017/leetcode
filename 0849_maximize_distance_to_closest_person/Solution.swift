// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution {
    func maxDistToClosest(_ seats: [Int]) -> Int {
        let n = seats.count
        var prev = -1, ans = 0
        for i in 0..<n where seats[i] == 1 {
            if prev == -1 { ans = i }
            else { ans = max(ans, (i - prev) / 2) }
            prev = i
        }
        return max(ans, n - 1 - prev)
    }
}
