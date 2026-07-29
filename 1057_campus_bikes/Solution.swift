// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

class Solution {
    func assignBikes(_ workers: [[Int]], _ bikes: [[Int]]) -> [Int] {
        var triples: [(Int, Int, Int)] = []
        for (w, worker) in workers.enumerated() {
            for (b, bike) in bikes.enumerated() {
                let dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                triples.append((dist, w, b))
            }
        }
        triples.sort {
            if $0.0 != $1.0 { return $0.0 < $1.0 }
            if $0.1 != $1.1 { return $0.1 < $1.1 }
            return $0.2 < $1.2
        }
        var ans = Array(repeating: -1, count: workers.count)
        var usedBikes = Set<Int>()
        var assigned = 0
        for (_, w, b) in triples {
            if ans[w] == -1 && !usedBikes.contains(b) {
                ans[w] = b
                usedBikes.insert(b)
                assigned += 1
                if assigned == workers.count {
                    break
                }
            }
        }
        return ans
    }
}
