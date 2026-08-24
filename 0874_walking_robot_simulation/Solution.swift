// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

class Solution {
    func robotSim(_ commands: [Int], _ obstacles: [[Int]]) -> Int {
        var blocked = Set<Int>()
        for o in obstacles { blocked.insert(encode(o[0], o[1])) }
        let dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        var x = 0, y = 0, d = 0, best = 0
        for cmd in commands {
            if cmd == -1 { d = (d + 1) % 4 }
            else if cmd == -2 { d = (d + 3) % 4 }
            else {
                let dx = dirs[d][0], dy = dirs[d][1]
                for _ in 0..<cmd {
                    let nx = x + dx, ny = y + dy
                    if blocked.contains(encode(nx, ny)) { break }
                    x = nx
                    y = ny
                }
                best = max(best, x * x + y * y)
            }
        }
        return best
    }

    private func encode(_ x: Int, _ y: Int) -> Int {
        return ((x + 30000) << 20) | (y + 30000)
    }
}
