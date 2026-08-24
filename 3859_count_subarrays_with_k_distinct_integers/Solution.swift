// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

class Solution {
    private var nums = [Int]()
    private var k = 0, m = 0

    func countSubarrays(_ nums: [Int], _ k: Int, _ m: Int) -> Int {
        self.nums = nums
        self.k = k
        self.m = m
        return f(k) - f(k + 1)
    }

    private func f(_ lim: Int) -> Int {
        var cnt = [Int: Int]()
        var ans = 0
        var l = 0, t = 0
        for x in nums {
            let c = (cnt[x] ?? 0) + 1
            cnt[x] = c
            if c == m { t += 1 }
            while cnt.count >= lim && t >= k {
                let y = nums[l]
                l += 1
                let cy = cnt[y]! - 1
                if cy == m - 1 { t -= 1 }
                if cy == 0 { cnt.removeValue(forKey: y) }
                else { cnt[y] = cy }
            }
            ans += l
        }
        return ans
    }
}
