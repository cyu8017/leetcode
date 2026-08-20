// LeetCode 1542 - Find Longest Awesome Substring
// https://leetcode.com/problems/find-longest-awesome-substring/

class Solution {
    func longestAwesome(_ s: String) -> Int {
        var first = [0: -1]
        var mask = 0, answer = 0
        for (i, ch) in s.enumerated() {
            mask ^= 1 << Int(String(ch))!
            if let prev = first[mask] {
                answer = max(answer, i - prev)
            } else {
                first[mask] = i
            }
            for bit in 0..<10 {
                let candidate = mask ^ (1 << bit)
                if let prev = first[candidate] {
                    answer = max(answer, i - prev)
                }
            }
        }
        return answer
    }
}
