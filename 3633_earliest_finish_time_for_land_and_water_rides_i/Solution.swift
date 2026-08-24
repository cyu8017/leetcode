// LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

class Solution {
    func calc(_ a1: [Int], _ t1: [Int], _ a2: [Int], _ t2: [Int]) -> Int {
        var minEnd = Int.max
        for i in 0..<a1.count { minEnd = min(minEnd, a1[i] + t1[i]) }
        var ans = Int.max
        for i in 0..<a2.count { ans = min(ans, max(minEnd, a2[i]) + t2[i]) }
        return ans
    }

    func earliestFinishTime(_ landStartTime: [Int], _ landDuration: [Int], _ waterStartTime: [Int], _ waterDuration: [Int]) -> Int {
        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration)
        )
    }
}
