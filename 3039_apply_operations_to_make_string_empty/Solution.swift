// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

class Solution {
    func lastNonEmptyString(_ s: String) -> String {
        let chars = Array(s)
        var cnt = Array(repeating: 0, count: 26)
        var last = Array(repeating: 0, count: 26)
        var mx = 0
        let aVal = Int(Character("a").asciiValue!)
        for i in 0..<chars.count {
            let c = Int(chars[i].asciiValue!) - aVal
            cnt[c] += 1
            last[c] = i
            mx = max(mx, cnt[c])
        }
        var ans = ""
        for i in 0..<chars.count {
            let c = Int(chars[i].asciiValue!) - aVal
            if cnt[c] == mx && last[c] == i { ans.append(chars[i]) }
        }
        return ans
    }
}
