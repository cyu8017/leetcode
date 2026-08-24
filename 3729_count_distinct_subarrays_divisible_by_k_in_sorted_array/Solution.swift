// LeetCode 3729 - Count Distinct Subarrays Divisible By K In Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

class Solution {
    func numGoodSubarrays(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        var s = 0
        var cnt = [Int: Int]()
        cnt[0] = 1
        for x in nums {
            s = (s + x) % k
            ans += cnt[s, default: 0]
            cnt[s, default: 0] += 1
        }
        let n = nums.count
        var i = 0
        while i < n {
            var j = i + 1
            while j < n && nums[j] == nums[i] { j += 1 }
            let m = j - i
            for h in 1...m {
                if nums[i] * h % k == 0 { ans -= (m - h) }
            }
            i = j
        }
        return ans
    }
}
