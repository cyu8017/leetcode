// LeetCode 0374 - Guess Number Higher or Lower
// https://leetcode.com/problems/guess-number-higher-or-lower/

func guess(_ num: Int) -> Int {
    0
}

class Solution {
    func guessNumber(_ n: Int) -> Int {
        var left = 1
        var right = n

        while left <= right {
            let mid = (left + right) / 2
            let result = guess(mid)
            if result == 0 {
                return mid
            }
            if result < 0 {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }

        return left
    }
}
