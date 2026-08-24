// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution {
    func isPossible(_ nums: [Int]) -> Bool {
        var freq = [Int: Int]()
        var tails = [Int: Int]()
        for num in nums { freq[num, default: 0] += 1 }
        for num in nums {
            if freq[num, default: 0] == 0 { continue }
            freq[num]! -= 1
            if tails[num - 1, default: 0] > 0 {
                tails[num - 1]! -= 1
                tails[num, default: 0] += 1
            } else if freq[num + 1, default: 0] > 0 && freq[num + 2, default: 0] > 0 {
                freq[num + 1]! -= 1
                freq[num + 2]! -= 1
                tails[num + 2, default: 0] += 1
            } else {
                return false
            }
        }
        return true
    }
}
