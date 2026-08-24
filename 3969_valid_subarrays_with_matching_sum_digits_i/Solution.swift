// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/


class Solution {
    func countValidSubarrays(_ nums: [Int], _ x: Int) -> Int {
        let n = nums.count
        var ans = 0
        for l in 0..<n {
            var s = 0
            for r in l..<n {
                s += nums[r]
                if s % 10 == x {
                    let t = String(s)
                    if Int(String(t.first!))! == x { ans += 1 }
                }
            }
        }
        return ans
    }
}
