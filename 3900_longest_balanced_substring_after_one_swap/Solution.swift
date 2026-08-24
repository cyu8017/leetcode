// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

class Solution {
    func longestBalanced(_ s: String) -> Int {
        let chars = Array(s)
        var cnt0 = 0
        for c in chars where c == "0" { cnt0 += 1 }
        let cnt1 = chars.count - cnt0
        var pos = [Int: [Int]]()
        pos[0] = [-1]
        var ans = 0, pre = 0
        for i in 0..<chars.count {
            if chars[i] == "1" { pre += 1 } else { pre -= 1 }
            pos[pre, default: []].append(i)
            ans = max(ans, i - pos[pre]![0])
            if let p = pos[pre - 2] {
                if (i - p[0] - 2) / 2 < cnt0 { ans = max(ans, i - p[0]) }
                else if p.count > 1 { ans = max(ans, i - p[1]) }
            }
            if let p = pos[pre + 2] {
                if (i - p[0] - 2) / 2 < cnt1 { ans = max(ans, i - p[0]) }
                else if p.count > 1 { ans = max(ans, i - p[1]) }
            }
        }
        return ans
    }
}
