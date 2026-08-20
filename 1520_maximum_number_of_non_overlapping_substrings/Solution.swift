// LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

class Solution {
    func maxNumOfSubstrings(_ s: String) -> [String] {
        let chars = Array(s)
        var first = [Character: Int]()
        var last = [Character: Int]()
        for (i, ch) in chars.enumerated() {
            if first[ch] == nil { first[ch] = i }
            last[ch] = i
        }
        var intervals = [(end: Int, start: Int)]()
        for (i, ch) in chars.enumerated() {
            guard first[ch] == i else { continue }
            var end = last[ch]!
            var j = i
            var valid = true
            while j <= end {
                if first[chars[j]]! < i {
                    valid = false
                    break
                }
                end = max(end, last[chars[j]]!)
                j += 1
            }
            if valid { intervals.append((end, i)) }
        }
        intervals.sort { $0.end < $1.end }
        var answer = [String]()
        var previousEnd = -1
        for iv in intervals {
            if iv.start > previousEnd {
                answer.append(String(chars[iv.start...iv.end]))
                previousEnd = iv.end
            }
        }
        return answer.sorted { $0.count < $1.count }
    }
}
