// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution {
    func minSizeSubarray(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        let total = nums.reduce(0, +)
        var ans = 1 << 30
        if total > 0 {
            let loops = target / total
            let remain = target % total
            if remain == 0 { return loops * n }
            let arr = nums + nums
            var left = 0, sum = 0, best = 1 << 30
            for right in 0..<arr.count {
                sum += arr[right]
                while sum > remain && left <= right {
                    sum -= arr[left]
                    left += 1
                }
                if sum == remain {
                    best = min(best, right - left + 1)
                }
            }
            if best < (1 << 30) { ans = loops * n + best }
        }
        return ans == (1 << 30) ? -1 : ans
    }
}
