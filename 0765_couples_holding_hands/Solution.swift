// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

class Solution {
    func minSwapsCouples(_ row: [Int]) -> Int {
        var row = row
        var pos = [Int: Int]()
        for i in 0..<row.count { pos[row[i]] = i }
        var swaps = 0
        var i = 0
        while i < row.count {
            let partner = row[i] ^ 1
            if row[i + 1] != partner {
                let j = pos[partner]!
                pos[row[i + 1]] = j
                row[j] = row[i + 1]
                row[i + 1] = partner
                pos[partner] = i + 1
                swaps += 1
            }
            i += 2
        }
        return swaps
    }
}
