// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

class Solution {
    func canConvert(_ str1: String, _ str2: String) -> Bool {
        if str1 == str2 { return true }
        let a = Array(str1), b = Array(str2)
        var mapping: [Character: Character] = [:]
        for i in 0..<a.count {
            if let m = mapping[a[i]], m != b[i] { return false }
            mapping[a[i]] = b[i]
        }
        return Set(b).count < 26
    }
}
