// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

class Solution {
    func findClosest(_ x: Int, _ y: Int, _ z: Int) -> Int {
        let a = abs(x - z), b = abs(y - z)
        if a == b { return 0 }
        return a < b ? 1 : 2
    }
}
