// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

class Solution {
    func splitLoopedString(_ strs: [String]) -> String {
        let bestForms = strs.map { s -> String in
            let rev = String(s.reversed())
            return s >= rev ? s : rev
        }
        var answer = ""
        for i in 0..<strs.count {
            var mid = ""
            if i + 1 < strs.count {
                mid += bestForms[(i + 1)...].joined()
            }
            if i > 0 {
                mid += bestForms[..<i].joined()
            }
            for candidate in [strs[i], String(strs[i].reversed())] {
                let chars = Array(candidate)
                for cut in 0..<chars.count {
                    let formed = String(chars[cut...]) + mid + String(chars[..<cut])
                    if formed > answer { answer = formed }
                }
            }
        }
        return answer
    }
}
