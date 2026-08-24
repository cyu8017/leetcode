// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution {
    func countSubarrays(_ nums: [Int], _ minK: Int, _ maxK: Int) -> Int {
        var ans = 0
        var imin = -1, imax = -1, ibad = -1
        for i in 0..<nums.count {
            let x = nums[i]
            if x < minK || x > maxK { ibad = i }
            if x == minK { imin = i }
            if x == maxK { imax = i }
            let bound = min(imin, imax)
            if bound > ibad { ans += bound - ibad }
        }
        return ans
    }
}
