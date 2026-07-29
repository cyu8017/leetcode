// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

class Solution {
    func gridIllumination(_ n: Int, _ lamps: [[Int]], _ queries: [[Int]]) -> [Int] {
        var rows = [Int: Int]()
        var cols = [Int: Int]()
        var diag1 = [Int: Int]()
        var diag2 = [Int: Int]()
        var lit = Set<[Int]>()
        for lamp in lamps {
            let r = lamp[0], c = lamp[1]
            if lit.contains([r, c]) { continue }
            lit.insert([r, c])
            rows[r, default: 0] += 1
            cols[c, default: 0] += 1
            diag1[r - c, default: 0] += 1
            diag2[r + c, default: 0] += 1
        }
        var ans = [Int]()
        for q in queries {
            let r = q[0], c = q[1]
            let on = (rows[r] ?? 0) > 0 || (cols[c] ?? 0) > 0 || (diag1[r - c] ?? 0) > 0 || (diag2[r + c] ?? 0) > 0
            ans.append(on ? 1 : 0)
            for i in (r - 1)...(r + 1) {
                for j in (c - 1)...(c + 1) {
                    if lit.contains([i, j]) {
                        lit.remove([i, j])
                        rows[i, default: 0] -= 1
                        cols[j, default: 0] -= 1
                        diag1[i - j, default: 0] -= 1
                        diag2[i + j, default: 0] -= 1
                    }
                }
            }
        }
        return ans
    }
}
