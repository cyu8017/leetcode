// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

class Solution {
    func numOfUnplacedFruits(_ fruits: [Int], _ baskets: [Int]) -> Int {
        var used = Array(repeating: false, count: baskets.count)
        var unplaced = 0
        for f in fruits {
            var placed = false
            for j in 0..<baskets.count where !used[j] && baskets[j] >= f {
                used[j] = true
                placed = true
                break
            }
            if !placed { unplaced += 1 }
        }
        return unplaced
    }
}
