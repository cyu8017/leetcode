// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

class Solution {
    func findLatestTime(_ s: String) -> String {
        let chars = Array(s)
        for h in stride(from: 11, through: 0, by: -1) {
            for m in stride(from: 59, through: 0, by: -1) {
                let t = String(format: "%02d:%02d", h, m)
                let tc = Array(t)
                var ok = true
                for i in 0..<5 {
                    if chars[i] != "?" && chars[i] != tc[i] {
                        ok = false
                        break
                    }
                }
                if ok { return t }
            }
        }
        return s
    }
}
