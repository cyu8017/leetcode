// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/


class Solution {
    func createGrid(_ m: Int, _ n: Int) -> [String] {
        var g = [String]()
        for i in 0..<m {
            var row = Array(repeating: Character("#"), count: n)
            if i == 0 {
                for j in 0..<n { row[j] = "." }
            }
            row[n - 1] = "."
            g.append(String(row))
        }
        return g
    }
}
