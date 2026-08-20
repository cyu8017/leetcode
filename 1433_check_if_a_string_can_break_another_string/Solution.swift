// LeetCode 1433 - Check If a String Can Break Another String
// https://leetcode.com/problems/check-if-a-string-can-break-another-string/

class Solution {
    func checkIfCanBreak(_ s1: String, _ s2: String) -> Bool {
        let a = s1.sorted(), b = s2.sorted()
        return zip(a, b).allSatisfy { $0 >= $1 } || zip(a, b).allSatisfy { $0 <= $1 }
    }
}
