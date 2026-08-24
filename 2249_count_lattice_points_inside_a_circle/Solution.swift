// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

class Solution {
    func countLatticePoints(_ circles: [[Int]]) -> Int {
        var seen = Set<Int>()
        for c in circles {
            let x = c[0], y = c[1], r = c[2]
            for i in (x - r)...(x + r) {
                for j in (y - r)...(y + r) {
                    if (i - x) * (i - x) + (j - y) * (j - y) <= r * r {
                        seen.insert(i * 1000 + j)
                    }
                }
            }
        }
        return seen.count
    }
}
