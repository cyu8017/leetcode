// LeetCode 3996 - Even Number of Knight Moves
// https://leetcode.com/problems/even-number-of-knight-moves/


class Solution {
    func canReach(_ start: [Int], _ target: [Int]) -> Bool {
        ((start[0] + start[1]) % 2) == ((target[0] + target[1]) % 2)
    }
}
