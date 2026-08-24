// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

class Solution {
    func numOfUnplacedFruits(_ fruits: [Int], _ baskets: [Int]) -> Int {
        let n = baskets.count
        var size = 1
        while size < n { size <<= 1 }
        var tree = Array(repeating: 0, count: size * 2)
        for i in 0..<n { tree[size + i] = baskets[i] }
        for i in stride(from: size - 1, through: 1, by: -1) {
            tree[i] = max(tree[i * 2], tree[i * 2 + 1])
        }
        func find(_ node: Int, _ nl: Int, _ nr: Int, _ need: Int) -> Int {
            if tree[node] < need { return -1 }
            if nl == nr { return nl }
            let mid = (nl + nr) / 2
            let left = find(node * 2, nl, mid, need)
            if left != -1 { return left }
            return find(node * 2 + 1, mid + 1, nr, need)
        }
        func update(_ idx: Int) {
            var p = size + idx
            tree[p] = -1
            p >>= 1
            while p > 0 {
                tree[p] = max(tree[p * 2], tree[p * 2 + 1])
                p >>= 1
            }
        }
        var unplaced = 0
        for f in fruits {
            let idx = find(1, 0, size - 1, f)
            if idx == -1 || idx >= n { unplaced += 1 }
            else { update(idx) }
        }
        return unplaced
    }
}
