// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

class Solution {
    func carPooling(_ trips: [[Int]], _ capacity: Int) -> Bool {
        var diff = Array(repeating: 0, count: 1001)
        for trip in trips {
            diff[trip[1]] += trip[0]
            diff[trip[2]] -= trip[0]
        }
        var cur = 0
        for x in diff {
            cur += x
            if cur > capacity {
                return false
            }
        }
        return true
    }
}
