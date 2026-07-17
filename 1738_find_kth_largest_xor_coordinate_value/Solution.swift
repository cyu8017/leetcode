// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

class Solution {
    func kthLargestValue(_ matrix: [[Int]], _ k: Int) -> Int {
        let rows = matrix.count
        let cols = matrix[0].count
        var pref = [[Int]](repeating: [Int](repeating: 0, count: cols + 1), count: rows + 1)
        var values: [Int] = []
        values.reserveCapacity(rows * cols)
        for r in 1...rows {
            for c in 1...cols {
                pref[r][c] = pref[r - 1][c] ^ pref[r][c - 1] ^ pref[r - 1][c - 1] ^ matrix[r - 1][c - 1]
                values.append(pref[r][c])
            }
        }
        values.sort(by: >)
        return values[k - 1]
    }
}
