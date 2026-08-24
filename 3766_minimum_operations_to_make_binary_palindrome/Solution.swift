// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

class Solution {
    private static let PALS: [Int] = {
        let N = 1 << 14
        var pals = [Int]()
        for i in 0..<N {
            var sb = [Character]()
            var x = i
            if x == 0 {
                sb.append("0")
            } else {
                while x > 0 {
                    sb.append(Character(UnicodeScalar(48 + (x & 1))!))
                    x >>= 1
                }
                sb.reverse()
            }
            if isPalindrome(sb) { pals.append(i) }
        }
        return pals
    }()

    private static func isPalindrome(_ s: [Character]) -> Bool {
        let m = s.count
        for i in 0..<(m / 2) where s[i] != s[m - 1 - i] { return false }
        return true
    }

    func minOperations(_ nums: [Int]) -> [Int] {
        var ans = [Int](repeating: 0, count: nums.count)
        for k in 0..<nums.count {
            let x = nums[k]
            let it = lowerBound(x)
            var t = Int.max
            if it < Solution.PALS.count { t = Solution.PALS[it] - x }
            if it > 0 { t = min(t, x - Solution.PALS[it - 1]) }
            ans[k] = t
        }
        return ans
    }

    private func lowerBound(_ x: Int) -> Int {
        var lo = 0, hi = Solution.PALS.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if Solution.PALS[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
