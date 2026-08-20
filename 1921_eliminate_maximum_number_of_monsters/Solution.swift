// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

class Solution {
    func eliminateMaximum(_ dist: [Int], _ speed: [Int]) -> Int {
        let arrival = zip(dist, speed).map { ($0.0 + $0.1 - 1) / $0.1 }.sorted()
        for (i, t) in arrival.enumerated() {
            if t <= i { return i }
        }
        return arrival.count
    }
}
