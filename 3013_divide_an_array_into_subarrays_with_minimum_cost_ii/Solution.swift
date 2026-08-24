// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

class Solution {
    func minimumCost(_ nums: [Int], _ k0: Int, _ dist: Int) -> Int {
        var k = k0 - 1
        let n = nums.count
        var uniq = nums.sorted()
        var write = 0
        for v in uniq {
            if write == 0 || uniq[write - 1] != v {
                uniq[write] = v
                write += 1
            }
        }
        uniq = Array(uniq[0..<write])
        let m = uniq.count
        var cnt = Array(repeating: 0, count: m + 3)
        var sum = Array(repeating: 0, count: m + 3)

        func cntUpd(_ x0: Int, _ d: Int) {
            var x = x0
            while x <= m + 2 {
                cnt[x] += d
                x += x & -x
            }
        }
        func cntQry(_ x0: Int) -> Int {
            var x = x0, s = 0
            while x > 0 {
                s += cnt[x]
                x -= x & -x
            }
            return s
        }
        func sumUpd(_ x0: Int, _ d: Int) {
            var x = x0
            while x <= m + 2 {
                sum[x] += d
                x += x & -x
            }
        }
        func sumQry(_ x0: Int) -> Int {
            var x = x0, s = 0
            while x > 0 {
                s += sum[x]
                x -= x & -x
            }
            return s
        }
        func rankOf(_ v: Int) -> Int {
            var lo = 0, hi = uniq.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if uniq[mid] < v { lo = mid + 1 }
                else { hi = mid }
            }
            return lo + 1
        }
        func kth(_ kk: Int) -> Int {
            var k = kk, idx = 0
            var bit = 1 << 20
            while bit != 0 {
                let nidx = idx + bit
                if nidx <= m && cnt[nidx] < k {
                    k -= cnt[nidx]
                    idx = nidx
                }
                bit >>= 1
            }
            return idx + 1
        }
        func sumSmallest(_ kk: Int) -> Int {
            if kk <= 0 { return 0 }
            let r = kth(kk)
            let before = cntQry(r - 1)
            var s = sumQry(r - 1)
            s += (kk - before) * uniq[r - 1]
            return s
        }

        let end0 = min(dist + 1, n - 1)
        if end0 >= 1 {
            for i in 1...end0 {
                let r = rankOf(nums[i])
                cntUpd(r, 1)
                sumUpd(r, nums[i])
            }
        }
        var kk = min(k, end0)
        var ans = nums[0] + sumSmallest(kk)
        if dist + 2 < n {
            for i in (dist + 2)..<n {
                let rem = nums[i - dist - 1]
                let r1 = rankOf(rem)
                cntUpd(r1, -1)
                sumUpd(r1, -rem)
                let add = nums[i]
                let r2 = rankOf(add)
                cntUpd(r2, 1)
                sumUpd(r2, add)
                kk = min(k, dist + 1)
                ans = min(ans, nums[0] + sumSmallest(kk))
            }
        }
        return ans
    }
}
