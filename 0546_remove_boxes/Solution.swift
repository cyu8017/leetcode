// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

class Solution {
    func removeBoxes(_ boxes: [Int]) -> Int {
        var memo: [String: Int] = [:]

        func dp(_ left: Int, _ right: Int, _ streak: Int) -> Int {
            if left > right {
                return 0
            }
            let state = "\(left),\(right),\(streak)"
            if let cached = memo[state] {
                return cached
            }

            var r = right
            var s = streak
            while r > left && boxes[r] == boxes[r - 1] {
                r -= 1
                s += 1
            }

            var best = (s + 1) * (s + 1) + dp(left, r - 1, 0)
            if left < r {
                for i in left..<r {
                    if boxes[i] == boxes[r] {
                        best = max(best, dp(left, i, s + 1) + dp(i + 1, r - 1, 0))
                    }
                }
            }

            memo[state] = best
            return best
        }

        return dp(0, boxes.count - 1, 0)
    }
}
