// LeetCode 2172 - Maximum AND Sum of Array
// https://leetcode.com/problems/maximum-and-sum-of-array/

class Solution {
    func maximumANDSum(_ nums: [Int], _ numSlots: Int) -> Int {
        let n = nums.count, slots = numSlots
        var maxMask = 1
        for _ in 0..<slots { maxMask *= 3 }
        var dp = [Int](repeating: 0, count: maxMask)
        for mask in 0..<maxMask {
            var cnt = 0, x = mask
            while x > 0 { cnt += x % 3; x /= 3 }
            if cnt >= n { continue }
            let v = nums[cnt]
            var bas = 1
            for s in 1...slots {
                let occ = (mask / bas) % 3
                if occ < 2 {
                    let nm = mask + bas
                    dp[nm] = max(dp[nm], dp[mask] + (v & s))
                }
                bas *= 3
            }
        }
        return dp.max() ?? 0
    }
}
