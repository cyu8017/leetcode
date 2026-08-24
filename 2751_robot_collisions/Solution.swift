// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

class Solution {
    func survivedRobotsHealths(_ positions: [Int], _ healths: [Int], _ directions: String) -> [Int] {
        let n = positions.count
        let dirs = Array(directions)
        var idx = Array(0..<n)
        idx.sort { positions[$0] < positions[$1] }
        var stack: [[Int]] = []
        for i in idx {
            var cur = [i, healths[i], Int(dirs[i].asciiValue!)]
            while !stack.isEmpty && stack.last![2] == Int(Character("R").asciiValue!) && cur[2] == Int(Character("L").asciiValue!) {
                var top = stack.removeLast()
                if top[1] == cur[1] {
                    cur[1] = 0
                    break
                } else if top[1] > cur[1] {
                    top[1] -= 1
                    stack.append(top)
                    cur[1] = 0
                    break
                } else {
                    cur[1] -= 1
                }
            }
            if cur[1] > 0 { stack.append(cur) }
        }
        var alive: [Int: Int] = [:]
        for r in stack { alive[r[0]] = r[1] }
        return (0..<n).compactMap { alive[$0] }
    }
}
