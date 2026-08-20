// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

class Solution {
    func numKLenSubstrNoRepeats(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        if k > chars.count { return 0 }
        var window: [Character: Int] = [:]
        for i in 0..<k {
            window[chars[i], default: 0] += 1
        }
        var ans = window.count == k ? 1 : 0
        for i in k..<chars.count {
            window[chars[i], default: 0] += 1
            let left = chars[i - k]
            window[left, default: 0] -= 1
            if window[left] == 0 { window.removeValue(forKey: left) }
            if window.count == k { ans += 1 }
        }
        return ans
    }
}
