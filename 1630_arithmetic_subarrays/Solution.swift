// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

class Solution {
    func checkArithmeticSubarrays(_ nums: [Int], _ l: [Int], _ r: [Int]) -> [Bool] {
        zip(l, r).map { a, b in
            let x = nums[a...b].sorted()
            if x.count < 3 { return true }
            let diff = x[1] - x[0]
            for i in 2..<x.count {
                if x[i] - x[i - 1] != diff { return false }
            }
            return true
        }
    }
}
