// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

class Solution {
    func minimumDifference(_ nums: [Int], _ k: Int) -> Int {
        let mx = nums.max()!
        let m = mx == 0 ? 1 : mx.bitWidth - mx.leadingZeroBitCount
        var cnt = Array(repeating: 0, count: m)
        var ans = Int.max, s = 0, i = 0
        for j in 0..<nums.count {
            let x = nums[j]
            s |= x
            ans = min(ans, abs(s - k))
            for h in 0..<m where ((x >> h) & 1) != 0 { cnt[h] += 1 }
            while i < j && s > k {
                let y = nums[i]
                for h in 0..<m where ((y >> h) & 1) != 0 {
                    cnt[h] -= 1
                    if cnt[h] == 0 { s ^= 1 << h }
                }
                ans = min(ans, abs(s - k))
                i += 1
            }
        }
        return ans
    }
}
