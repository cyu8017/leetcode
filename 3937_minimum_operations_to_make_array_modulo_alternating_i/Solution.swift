// LeetCode 3937 - Minimum Operations to Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/


class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        let a = nums.map { $0 % k }
        var ans = Int.max
        for x in 0..<k {
            for y in 0..<k {
                if x == y { continue }
                var cnt = 0
                for i in 0..<a.count {
                    let target = (i & 1) != 0 ? y : x
                    let diff = abs(target - a[i])
                    cnt += min(diff, k - diff)
                }
                ans = min(ans, cnt)
            }
        }
        return ans
    }
}
