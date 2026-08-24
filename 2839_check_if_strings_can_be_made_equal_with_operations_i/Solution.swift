// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

class Solution {
    func canBeEqual(_ s1: String, _ s2: String) -> Bool {
        let a = Array(s1), b = Array(s2)
        var even1 = [a[0], a[2]].sorted()
        var even2 = [b[0], b[2]].sorted()
        var odd1 = [a[1], a[3]].sorted()
        var odd2 = [b[1], b[3]].sorted()
        return even1 == even2 && odd1 == odd2
    }
}
