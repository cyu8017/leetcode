// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

class Solution {
    func onceTwice(_ nums: [Int]) -> [Int] {
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        var a = 0, b = 0
        for (k, v) in freq {
            if v == 1 { a = k }
            else if v == 2 { b = k }
        }
        return [a, b]
    }
}
