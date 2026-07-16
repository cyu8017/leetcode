// LeetCode 0362 - Design Hit Counter
// https://leetcode.com/problems/design-hit-counter/

class HitCounter {
    private var hits: [Int] = []

    init() {
    }

    func hit(_ timestamp: Int) {
        hits.append(timestamp)
    }

    func getHits(_ timestamp: Int) -> Int {
        while !hits.isEmpty && hits[0] <= timestamp - 300 {
            hits.removeFirst()
        }
        return hits.count
    }
}
