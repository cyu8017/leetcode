// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution {
    func findPairs(_ nums: [Int], _ k: Int) -> Int {
        if k < 0 {
            return 0
        }

        var freq: [Int: Int] = [:]
        for num in nums {
            freq[num, default: 0] += 1
        }

        var pairs = 0
        for num in freq.keys {
            if k == 0 {
                if freq[num]! > 1 {
                    pairs += 1
                }
            } else if freq[num + k] != nil {
                pairs += 1
            }
        }
        return pairs
    }
}
