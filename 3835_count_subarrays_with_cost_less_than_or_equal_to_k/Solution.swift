// LeetCode 3835 - Count Subarrays With Cost Less Than Or Equal To K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        var q1 = [Int]()
        var q2 = [Int]()
        var l = 0
        for r in 0..<nums.count {
            let x = nums[r]
            while !q1.isEmpty && nums[q1.last!] <= x { q1.removeLast() }
            while !q2.isEmpty && nums[q2.last!] >= x { q2.removeLast() }
            q1.append(r)
            q2.append(r)
            while l < r && (nums[q1[0]] - nums[q2[0]]) * (r - l + 1) > k {
                l += 1
                if q1[0] < l { q1.removeFirst() }
                if q2[0] < l { q2.removeFirst() }
            }
            ans += r - l + 1
        }
        return ans
    }
}
