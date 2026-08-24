// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution {
    func maximumSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        var cnt = [Int: Int]()
        var sum = 0, ans = 0
        for i in 0..<nums.count {
            sum += nums[i]
            cnt[nums[i], default: 0] += 1
            if i >= k {
                let y = nums[i - k]
                sum -= y
                cnt[y]! -= 1
                if cnt[y] == 0 { cnt.removeValue(forKey: y) }
            }
            if i >= k - 1 && cnt.count == k && sum > ans { ans = sum }
        }
        return ans
    }
}
