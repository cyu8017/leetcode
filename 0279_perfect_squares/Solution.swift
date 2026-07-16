// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

class Solution {
    func numSquares(_ n: Int) -> Int {
        var squares: [Int] = []
        var value = 1
        while value * value <= n {
            squares.append(value * value)
            value += 1
        }

        var queue: [(Int, Int)] = [(n, 0)]
        var visited: Set<Int> = [n]

        while !queue.isEmpty {
            let (remain, steps) = queue.removeFirst()
            if remain == 0 {
                return steps
            }
            for square in squares {
                let next = remain - square
                if next < 0 {
                    break
                }
                if !visited.contains(next) {
                    visited.insert(next)
                    queue.append((next, steps + 1))
                }
            }
        }
        return 0
    }
}
