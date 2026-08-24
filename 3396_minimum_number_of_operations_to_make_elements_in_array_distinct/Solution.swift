// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var list = nums
        var ops = 0
        while true {
            var seen = Set<Int>()
            var dup = false
            for x in list {
                if !seen.insert(x).inserted { dup = true; break }
            }
            if !dup { return ops }
            if list.count <= 3 { return ops + 1 }
            list.removeFirst(3)
            ops += 1
        }
    }
}
