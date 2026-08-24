// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

class Solution {
    func isReachableAtTime(_ sx: Int, _ sy: Int, _ fx: Int, _ fy: Int, _ t: Int) -> Bool {
        let need = max(abs(sx - fx), abs(sy - fy))
        if need == 0 { return t != 1 }
        return t >= need
    }
}
