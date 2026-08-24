// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

class Solution {
    var n = 0
    var order = [Int]()
    var total = 0

    func countValid(_ t: Int) -> Int {
        var star = Array(repeating: false, count: n)
        for i in 0...t { star[order[i]] = true }
        var invalid = 0
        var i = 0
        while i < n {
            if star[i] { i += 1; continue }
            var j = i
            while j < n && !star[j] { j += 1 }
            let L = j - i
            invalid += L * (L + 1) / 2
            i = j
        }
        return total - invalid
    }

    func minTime(_ s: String, _ order: [Int], _ k: Int) -> Int {
        self.order = order
        n = s.count
        total = n * (n + 1) / 2
        if k > total { return -1 }
        var lo = 0, hi = n - 1, ans = -1
        while lo <= hi {
            let mid = (lo + hi) / 2
            if countValid(mid) >= k {
                ans = mid
                hi = mid - 1
            } else { lo = mid + 1 }
        }
        return ans
    }
}
