// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        let pos = nums.firstIndex(of: k)!
        var bal = [Int: Int]()
        bal[0] = 1
        var cur = 0
        for i in stride(from: pos - 1, through: 0, by: -1) {
            cur += nums[i] < k ? -1 : 1
            bal[cur, default: 0] += 1
        }
        var ans = (bal[0] ?? 0) + (bal[1] ?? 0)
        cur = 0
        for i in (pos + 1)..<nums.count {
            cur += nums[i] < k ? -1 : 1
            ans += (bal[-cur] ?? 0) + (bal[1 - cur] ?? 0)
        }
        return ans
    }
}
