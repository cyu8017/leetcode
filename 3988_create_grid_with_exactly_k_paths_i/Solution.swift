// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/


class Solution {
    func createGrid(_ m: Int, _ n: Int, _ k: Int) -> [String] {
        var cands = [[String]]()
        if k == 1 { cands.append(["."]) }
        else if k == 2 { cands.append(["..", ".."]) }
        else if k == 3 {
            cands.append(["..", "..", ".."])
            cands.append(["...", "..."])
        } else if k == 4 {
            cands.append(["..", "..", "..", ".."])
            cands.append(["....", "...."])
            cands.append(["..#", "...", "#.."])
        }
        for pat in cands {
            let pr = pat.count, pc = pat[0].count
            if pr > m || pc > n { continue }
            var result = [String]()
            for _ in 0..<m {
                result.append(String(repeating: "#", count: n))
            }
            for i in 0..<pr {
                var row = Array(result[i])
                let p = Array(pat[i])
                for j in 0..<pc { row[j] = p[j] }
                result[i] = String(row)
            }
            if pr < m {
                for i in pr..<m {
                    var row = Array(result[i])
                    row[pc - 1] = "."
                    result[i] = String(row)
                }
            }
            if pc < n {
                var row = Array(result[m - 1])
                for j in pc..<n { row[j] = "." }
                result[m - 1] = String(row)
            }
            return result
        }
        return []
    }
}
