// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution {
    func findSpecialInteger(_ arr: [Int]) -> Int {
        let n = arr.count
        let span = n / 4
        for i in [0, span, 2 * span, 3 * span] where i < n {
            let target = arr[i]
            var lo = 0, hi = n
            while lo < hi {
                let mid = (lo + hi) / 2
                if arr[mid] < target { lo = mid + 1 } else { hi = mid }
            }
            let left = lo
            lo = 0; hi = n
            while lo < hi {
                let mid = (lo + hi) / 2
                if arr[mid] <= target { lo = mid + 1 } else { hi = mid }
            }
            if lo - left > span { return target }
        }
        return arr[0]
    }
}
