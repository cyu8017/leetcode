// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

class Solution {
    func longestRepeatingSubstring(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count

        func hasDup(_ length: Int) -> Bool {
            var seen = Set<String>()
            for i in 0...(n - length) {
                let sub = String(chars[i..<(i + length)])
                if seen.contains(sub) {
                    return true
                }
                seen.insert(sub)
            }
            return false
        }

        var lo = 1
        var hi = n - 1
        var ans = 0
        while lo <= hi {
            let mid = (lo + hi) / 2
            if hasDup(mid) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }
}
