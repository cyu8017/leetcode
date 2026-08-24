// LeetCode 3279 - Maximum Total Area Occupied by Pistons
// https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

class Solution {
    func maxArea(_ height: Int, _ positions: [Int], _ directions: String) -> Int {
        var pos = positions
        var dir = Array(directions)
        var best = 0
        for _ in 0...(2 * height) {
            best = max(best, pos.reduce(0, +))
            for i in 0..<pos.count {
                if dir[i] == "U" {
                    if pos[i] == height { dir[i] = "D"; pos[i] -= 1 }
                    else { pos[i] += 1 }
                } else {
                    if pos[i] == 0 { dir[i] = "U"; pos[i] += 1 }
                    else { pos[i] -= 1 }
                }
            }
        }
        return best
    }
}
