// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

class Solution {
    func subarraysWithMoreZerosThanOnes(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        let n = nums.count
        let offset = n + 1
        var bit = [Int](repeating: 0, count: 2 * n + 8)
        func add(_ i: Int, _ v: Int) {
            var i = i
            while i < bit.count {
                bit[i] += v
                i += i & -i
            }
        }
        func sum(_ i: Int) -> Int {
            var i = i, s = 0
            while i > 0 {
                s += bit[i]
                i -= i & -i
            }
            return s
        }
        var pref = 0, ans = 0
        add(offset, 1)
        for x in nums {
            pref += x == 1 ? 1 : -1
            let idx = pref + offset
            ans = (ans + sum(idx - 1)) % MOD
            add(idx, 1)
        }
        return ans
    }
}
