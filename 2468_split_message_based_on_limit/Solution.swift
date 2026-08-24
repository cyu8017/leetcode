// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

class Solution {
    func splitMessage(_ message: String, _ limit: Int) -> [String] {
        let chars = Array(message)
        let n = chars.count
        if n == 0 { return [] }
        for parts in 1...n {
            let sbDigits = String(parts).count
            var ok = true
            var idx = 0
            var res = [String]()
            for i in 1...parts {
                let tail = 3 + String(i).count + sbDigits
                let cap = limit - tail
                if cap <= 0 || idx >= n {
                    ok = false
                    break
                }
                let take = min(cap, n - idx)
                res.append(String(chars[idx..<(idx + take)]) + "<\(i)/\(parts)>")
                idx += take
            }
            if ok && idx == n { return res }
        }
        return []
    }
}
