// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

class Solution {
    private var bit: [Int] = []
    private let negInf = -(1 << 60)

    func maxBalancedSubsequenceSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var keys = Array(repeating: 0, count: n)
        var uniq: [Int] = []
        for i in 0..<n {
            keys[i] = nums[i] - i
            uniq.append(keys[i])
        }
        uniq.sort()
        var compact: [Int] = []
        for v in uniq {
            if compact.isEmpty || compact.last! != v { compact.append(v) }
        }
        uniq = compact
        bit = Array(repeating: negInf, count: uniq.count + 2)
        var ans = negInf
        for i in 0..<n {
            let id = idxOf(uniq, keys[i])
            let best = query(id)
            var cur = nums[i]
            if best > negInf / 2 {
                cur = max(cur, best + nums[i])
            }
            update(id, cur)
            ans = max(ans, cur)
        }
        return ans
    }

    private func idxOf(_ uniq: [Int], _ v: Int) -> Int {
        var lo = 0, hi = uniq.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if uniq[mid] < v { lo = mid + 1 }
            else { hi = mid }
        }
        return lo + 1
    }

    private func update(_ i0: Int, _ val: Int) {
        var i = i0
        while i < bit.count {
            bit[i] = max(bit[i], val)
            i += i & -i
        }
    }

    private func query(_ i0: Int) -> Int {
        var i = i0, best = negInf
        while i > 0 {
            best = max(best, bit[i])
            i -= i & -i
        }
        return best
    }
}
