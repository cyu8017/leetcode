// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution {
    func minimumMountainRemovals(_ nums: [Int]) -> Int {
        func lis(_ a: [Int]) -> [Int] {
            var d = [Int]()
            var out = [Int]()
            for x in a {
                var lo = 0, hi = d.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if d[mid] < x { lo = mid + 1 } else { hi = mid }
                }
                if lo == d.count { d.append(x) } else { d[lo] = x }
                out.append(lo + 1)
            }
            return out
        }
        let l = lis(nums)
        let r = Array(lis(Array(nums.reversed())).reversed())
        let n = nums.count
        var best = 0
        for i in 0..<n {
            if l[i] > 1 && r[i] > 1 {
                best = max(best, l[i] + r[i] - 1)
            }
        }
        return n - best
    }
}
