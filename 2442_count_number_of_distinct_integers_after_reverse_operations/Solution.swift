// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution {
    func countDistinctIntegers(_ nums: [Int]) -> Int {
        func rev(_ x: Int) -> Int {
            var x = x, r = 0
            while x > 0 {
                r = r * 10 + x % 10
                x /= 10
            }
            return r
        }
        var seen = Set<Int>()
        for x in nums {
            seen.insert(x)
            seen.insert(rev(x))
        }
        return seen.count
    }
}
