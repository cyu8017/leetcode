// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

class Solution {
    func filterCharacters(_ s: String, _ k: Int) -> String {
        var cnt = Array(repeating: 0, count: 26)
        for c in s.utf8 { cnt[Int(c - 97)] += 1 }
        var ans = ""
        for c in s {
            if cnt[Int(c.asciiValue! - 97)] < k { ans.append(c) }
        }
        return ans
    }
}
