// LeetCode 0278 - First Bad Version
// https://leetcode.com/problems/first-bad-version/

func isBadVersion(_ version: Int) -> Bool {
    false
}

class Solution {
    func firstBadVersion(_ n: Int) -> Int {
        var left = 1
        var right = n
        while left < right {
            let mid = left + (right - left) / 2
            if isBadVersion(mid) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
