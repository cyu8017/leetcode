// LeetCode 1345 - Jump Game IV
// https://leetcode.com/problems/jump-game-iv/

class Solution {
    func minJumps(_ arr: [Int]) -> Int {
        var positions = [Int: [Int]]()
        for (i, value) in arr.enumerated() { positions[value, default: []].append(i) }
        var queue = [0], seen: Set<Int> = [0], steps = 0, qi = 0
        while qi < queue.count {
            let size = queue.count - qi
            for _ in 0..<size {
                let i = queue[qi]; qi += 1
                if i == arr.count - 1 { return steps }
                var next = positions.removeValue(forKey: arr[i]) ?? []
                next.append(i - 1)
                next.append(i + 1)
                for j in next where j >= 0 && j < arr.count && !seen.contains(j) {
                    seen.insert(j); queue.append(j)
                }
            }
            steps += 1
        }
        return -1
    }
}
