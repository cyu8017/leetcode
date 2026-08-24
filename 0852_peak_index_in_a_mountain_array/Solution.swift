// LeetCode 0852 - Peak Index in a Mountain Array
// https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution {
    func peakIndexInMountainArray(_ arr: [Int]) -> Int {
        var lo = 0, hi = arr.count - 1
        while lo < hi {
            let mid = (lo + hi) / 2
            if arr[mid] < arr[mid + 1] { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
