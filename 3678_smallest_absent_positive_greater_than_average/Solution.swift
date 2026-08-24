// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

class Solution {
    func smallestAbsent(_ nums: [Int]) -> Int {
        var s = Set<Int>()
        var sum = 0
        for x in nums { s.insert(x); sum += x }
        var ans = max(1, sum / nums.count + 1)
        while s.contains(ans) { ans += 1 }
        return ans
    }
}
