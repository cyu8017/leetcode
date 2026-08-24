// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

class Solution {
    func maxCount(_ banned: [Int], _ n: Int, _ maxSum: Int) -> Int {
        var uniq = [Int]()
        for x in banned.sorted() {
            if x >= 1 && x <= n && (uniq.isEmpty || uniq.last != x) { uniq.append(x) }
        }
        var ans = 0
        var remain = maxSum
        func check(_ l: Int, _ r: Int) {
            if l > r || remain <= 0 { return }
            var lo = l, hi = r, best = l - 1
            while lo <= hi {
                let mid = (lo + hi) / 2
                let cnt = mid - l + 1
                let sum = (l + mid) * cnt / 2
                if sum <= remain {
                    best = mid
                    lo = mid + 1
                } else {
                    hi = mid - 1
                }
            }
            if best >= l {
                let cnt = best - l + 1
                ans += cnt
                remain -= (l + best) * cnt / 2
            }
        }
        var prev = 0
        for b in uniq {
            check(prev + 1, b - 1)
            prev = b
        }
        check(prev + 1, n)
        return ans
    }
}
