// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

class Solution {
    func shortestBeautifulSubstring(_ s: String, _ k: Int) -> String {
        let chars = Array(s)
        let n = chars.count
        var ans = ""
        for i in 0..<n {
            var ones = 0
            for j in i..<n {
                if chars[j] == "1" { ones += 1 }
                if ones == k {
                    let cand = String(chars[i...j])
                    if ans.isEmpty || cand.count < ans.count || (cand.count == ans.count && cand < ans) {
                        ans = cand
                    }
                    break
                }
                if ones > k { break }
            }
        }
        return ans
    }
}
