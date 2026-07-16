// LeetCode 0548 - Split Array with Equal Sum
// https://leetcode.com/problems/split-array-with-equal-sum/

class Solution {
    func splitArray(_ nums: [Int]) -> Bool {
        let n = nums.count
        if n < 7 {
            return false
        }

        var prefix = [0]
        for value in nums {
            prefix.append(prefix.last! + value)
        }

        for j in 3..<(n - 3) {
            var seen = Set<Int>()
            for i in 1..<(j - 1) {
                let first = prefix[i] - prefix[0]
                let second = prefix[j] - prefix[i + 1]
                if first == second {
                    seen.insert(first)
                }
            }

            for k in (j + 2)..<(n - 1) {
                let third = prefix[k] - prefix[j + 1]
                let fourth = prefix[n] - prefix[k + 1]
                if third == fourth && seen.contains(third) {
                    return true
                }
            }
        }

        return false
    }
}
