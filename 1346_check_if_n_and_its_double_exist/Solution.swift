// LeetCode 1346 - Check If N and Its Double Exist
// https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution {
    func checkIfExist(_ arr: [Int]) -> Bool {
        var seen = Set<Int>()
        for value in arr {
            if seen.contains(2 * value) || (value % 2 == 0 && seen.contains(value / 2)) { return true }
            seen.insert(value)
        }
        return false
    }
}
