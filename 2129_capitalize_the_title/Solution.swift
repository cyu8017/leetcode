// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

class Solution {
    func capitalizeTitle(_ title: String) -> String {
        title.split(separator: " ").map { w in
            var s = w.lowercased()
            if s.count > 2 {
                s = s.prefix(1).uppercased() + s.dropFirst()
            }
            return s
        }.joined(separator: " ")
    }
}
