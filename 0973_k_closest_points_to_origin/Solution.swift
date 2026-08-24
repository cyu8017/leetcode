// LeetCode 0973 - K Closest Points to Origin
// https://leetcode.com/problems/k-closest-points-to-origin/

class Solution {
    func kClosest(_ points: [[Int]], _ k: Int) -> [[Int]] {
        return Array(points.sorted { $0[0] * $0[0] + $0[1] * $0[1] < $1[0] * $1[0] + $1[1] * $1[1] }.prefix(k))
    }
}
