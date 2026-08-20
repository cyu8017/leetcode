// LeetCode 1306 - Jump Game III
// https://leetcode.com/problems/jump-game-iii/

class Solution {
    func canReach(_ arr: [Int], _ start: Int) -> Bool {
        var stack = [start]
        var seen = Set<Int>()
        while !stack.isEmpty {
            let i = stack.removeLast()
            if seen.contains(i) || i < 0 || i >= arr.count { continue }
            if arr[i] == 0 { return true }
            seen.insert(i)
            stack.append(i - arr[i])
            stack.append(i + arr[i])
        }
        return false
    }
}
