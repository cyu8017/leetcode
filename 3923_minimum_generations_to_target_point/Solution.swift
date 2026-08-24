// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

class Solution {
    func minGenerations(_ points: [[Int]], _ target: [Int]) -> Int {
        struct P: Hashable {
            let a: Int, b: Int, c: Int
        }
        let targetPoint = P(a: target[0], b: target[1], c: target[2])
        var generation = [P: Int]()
        var all = [P]()
        for values in points {
            let p = P(a: values[0], b: values[1], c: values[2])
            generation[p] = 0
            all.append(p)
        }
        if let g = generation[targetPoint] { return g }
        var current = 1
        while true {
            let limit = all.count
            var added = [P]()
            for i in 0..<limit {
                for j in (i + 1)..<limit {
                    if all[i] == all[j] { continue }
                    let pi = all[i], pj = all[j]
                    let p = P(a: (pi.a + pj.a) / 2, b: (pi.b + pj.b) / 2, c: (pi.c + pj.c) / 2)
                    if generation[p] == nil {
                        generation[p] = current
                        added.append(p)
                    }
                }
            }
            if let g = generation[targetPoint] { return g }
            if added.isEmpty { return -1 }
            all.append(contentsOf: added)
            current += 1
        }
    }
}
