// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

class Solution {
    func countCoveredBuildings(_ n: Int, _ buildings: [[Int]]) -> Int {
        var g1 = [Int: [Int]]()
        var g2 = [Int: [Int]]()
        for b in buildings {
            g1[b[0], default: []].append(b[1])
            g2[b[1], default: []].append(b[0])
        }
        for k in g1.keys { g1[k]!.sort() }
        for k in g2.keys { g2[k]!.sort() }
        var ans = 0
        for b in buildings {
            let x = b[0], y = b[1]
            let l1 = g1[x]!, l2 = g2[y]!
            if l2[0] < x && x < l2[l2.count - 1] && l1[0] < y && y < l1[l1.count - 1] { ans += 1 }
        }
        return ans
    }
}
