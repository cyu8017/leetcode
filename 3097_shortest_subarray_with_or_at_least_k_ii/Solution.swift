// LeetCode 3097 - Shortest Subarray With OR at Least K II
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

class Solution {
    func minimumSubarrayLength(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var cnt = Array(repeating: 0, count: 32)
        var ans = n + 1, s = 0, i = 0
        for j in 0..<n {
            let x = nums[j]
            s |= x
            for h in 0..<32 where ((x >> h) & 1) != 0 { cnt[h] += 1 }
            while s >= k && i <= j {
                ans = min(ans, j - i + 1)
                for h in 0..<32 where ((nums[i] >> h) & 1) != 0 {
                    cnt[h] -= 1
                    if cnt[h] == 0 { s ^= 1 << h }
                }
                i += 1
            }
        }
        return ans == n + 1 ? -1 : ans
    }
}
