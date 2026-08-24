// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

class Solution {
    func maxProduct(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        let total = 1 << n
        var best = 0
        for mask1 in 1..<total {
            let len1 = palLen(chars, mask1)
            if len1 == 0 { continue }
            let remain = (total - 1) ^ mask1
            var mask2 = remain
            while mask2 > 0 {
                let len2 = palLen(chars, mask2)
                if len2 > 0 { best = max(best, len1 * len2) }
                mask2 = (mask2 - 1) & remain
            }
        }
        return best
    }

    private func palLen(_ chars: [Character], _ mask: Int) -> Int {
        var picked = [Character]()
        for i in 0..<chars.count where (mask & (1 << i)) != 0 {
            picked.append(chars[i])
        }
        var l = 0, r = picked.count - 1
        while l < r {
            if picked[l] != picked[r] { return 0 }
            l += 1
            r -= 1
        }
        return picked.count
    }
}
