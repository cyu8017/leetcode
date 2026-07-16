// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

class ZigzagIterator {
    private var vectors: [[Int]]
    private var indices: [Int]
    private var turn: Int

    init(_ v1: [Int], _ v2: [Int]) {
        self.vectors = [v1, v2]
        self.indices = [0, 0]
        self.turn = 0
    }

    func next() -> Int {
        while indices[turn] >= vectors[turn].count {
            turn = 1 - turn
        }
        let value = vectors[turn][indices[turn]]
        indices[turn] += 1
        turn = 1 - turn
        return value
    }

    func hasNext() -> Bool {
        indices.enumerated().contains { index, vectorIndex in
            index < vectors[vectorIndex].count
        }
    }
}
