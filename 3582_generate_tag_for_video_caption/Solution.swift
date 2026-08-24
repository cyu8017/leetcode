// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

class Solution {
    func generateTag(_ caption: String) -> String {
        var ans = "#"
        let words = caption.split { $0.isWhitespace }.map(String.init)
        var i = 0
        for word in words {
            if word.isEmpty { continue }
            var w = word.lowercased()
            if i == 0 { ans += w }
            else {
                if !w.isEmpty {
                    let first = String(w.prefix(1)).uppercased()
                    w = first + w.dropFirst()
                }
                ans += w
            }
            if ans.count >= 100 { break }
            i += 1
        }
        if ans.count > 100 { ans = String(ans.prefix(100)) }
        return ans
    }
}
