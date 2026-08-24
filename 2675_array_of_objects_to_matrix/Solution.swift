// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

class Solution {
    func jsonToMatrix(_ arr: [[String: String]]) -> [[String]] {
        var keys = Set<String>()
        for obj in arr { keys.formUnion(obj.keys) }
        let sortedKeys = keys.sorted()
        var mat: [[String]] = [sortedKeys]
        for obj in arr {
            mat.append(sortedKeys.map { obj[$0] ?? "" })
        }
        return mat
    }
}
