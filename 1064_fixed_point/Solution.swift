// LeetCode 1064 - Fixed Point
// https://leetcode.com/problems/fixed-point/

class Solution {
    func fixedPoint(_ arr: [Int]) -> Int {
        var lo = 0
        var hi = arr.count - 1
        var ans = -1
        while lo <= hi {
            let mid = (lo + hi) / 2
            if arr[mid] == mid {
                ans = mid
                hi = mid - 1
            } else if arr[mid] < mid {
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }
}
