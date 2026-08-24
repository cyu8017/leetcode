// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

class Solution {
    func calculateScore(_ s: String) -> Int {
        var stacks = Array(repeating: [Int](), count: 26)
        var ans = 0
        for (i, ch) in s.enumerated() {
            let ci = Int(ch.asciiValue! - 97)
            let mir = 25 - ci
            if !stacks[mir].isEmpty {
                let j = stacks[mir].removeLast()
                ans += i - j
            } else {
                stacks[ci].append(i)
            }
        }
        return ans
    }
}
