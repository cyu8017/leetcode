// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

class Solution {
    func uniqueLetterString(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var last = [Character: [Int]]()
        for ch in chars {
            if last[ch] == nil { last[ch] = [-1] }
        }
        for i in 0..<n { last[chars[i]]!.append(i) }
        for key in last.keys { last[key]!.append(n) }
        var ans = 0
        for indices in last.values {
            for k in 1..<(indices.count - 1) {
                ans += (indices[k] - indices[k - 1]) * (indices[k + 1] - indices[k])
            }
        }
        return ans
    }
}
