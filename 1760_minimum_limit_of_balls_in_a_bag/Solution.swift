// LeetCode 1760 - Minimum Limit of Balls in a Bag
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

class Solution {
    func minimumSize(_ nums: [Int], _ maxOperations: Int) -> Int {
        var lo = 1
        var hi = nums.max()!
        while lo < hi {
            let mid = (lo + hi) / 2
            var ops = 0
            for x in nums {
                ops += (x - 1) / mid
            }
            if ops <= maxOperations {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        return lo
    }
}
