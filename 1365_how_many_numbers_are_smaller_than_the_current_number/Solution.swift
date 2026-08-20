// LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution {
    func smallerNumbersThanCurrent(_ nums: [Int]) -> [Int] {
        let sorted = nums.sorted()
        return nums.map { x in
            var lo = 0, hi = sorted.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if sorted[mid] < x { lo = mid + 1 } else { hi = mid }
            }
            return lo
        }
    }
}
