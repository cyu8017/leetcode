// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

class Solution {
    func longestDupSubstring(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count
        let nums = chars.map { Int($0.asciiValue!) }
        let MOD = 1_000_000_007
        let BASE = 911382323

        func search(_ length: Int) -> Int {
            if length == 0 { return 0 }
            var h = 0
            for i in 0..<length {
                h = (h * BASE + nums[i]) % MOD
            }
            var seen = [Int: [Int]]()
            seen[h] = [0]
            var power = 1
            for _ in 0..<length {
                power = (power * BASE) % MOD
            }
            if n - length < 1 { return -1 }
            for i in 1...(n - length) {
                h = (h * BASE - nums[i - 1] * power % MOD + nums[i + length - 1]) % MOD
                if h < 0 { h += MOD }
                if let idxs = seen[h] {
                    let cur = String(chars[i..<(i + length)])
                    for j in idxs {
                        if String(chars[j..<(j + length)]) == cur { return i }
                    }
                    seen[h, default: []].append(i)
                } else {
                    seen[h] = [i]
                }
            }
            return -1
        }

        var lo = 0, hi = n - 1
        var start = -1, bestLen = 0
        while lo <= hi {
            let mid = (lo + hi) / 2
            let pos = search(mid)
            if pos >= 0 {
                start = pos
                bestLen = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        if start < 0 { return "" }
        return String(chars[start..<(start + bestLen)])
    }
}
