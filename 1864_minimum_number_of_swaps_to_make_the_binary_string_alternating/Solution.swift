// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

class Solution {
    func minSwaps(_ s: String) -> Int {
        let chars = Array(s)
        let zeros = chars.filter { $0 == "0" }.count
        let ones = chars.count - zeros
        if abs(zeros - ones) > 1 {
            return -1
        }

        func mismatches(_ pattern: [Character]) -> Int {
            var count = 0
            for i in 0..<chars.count {
                if chars[i] != pattern[i % 2] {
                    count += 1
                }
            }
            return count / 2
        }

        if zeros == ones {
            return min(mismatches(["0", "1"]), mismatches(["1", "0"]))
        }
        if zeros > ones {
            return mismatches(["0", "1"])
        }
        return mismatches(["1", "0"])
    }
}
