// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

class Solution {
    func findShortestSubArray(_ nums: [Int]) -> Int {
        var first = [Int: Int](), last = [Int: Int](), count = [Int: Int]()
        var deg = 0
        for (i, num) in nums.enumerated() {
            if first[num] == nil { first[num] = i }
            last[num] = i
            count[num, default: 0] += 1
            deg = max(deg, count[num]!)
        }
        var best = nums.count
        for (num, c) in count where c == deg {
            best = min(best, last[num]! - first[num]! + 1)
        }
        return best
    }
}
