// LeetCode 1337 - The K Weakest Rows in a Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution {
    func kWeakestRows(_ mat: [[Int]], _ k: Int) -> [Int] {
        Array(mat.indices.sorted { (mat[$0].reduce(0, +), $0) < (mat[$1].reduce(0, +), $1) }.prefix(k))
    }
}
