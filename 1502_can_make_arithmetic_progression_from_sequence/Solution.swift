// LeetCode 1502 - Can Make Arithmetic Progression From Sequence
// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution {
    func canMakeArithmeticProgression(_ arr: [Int]) -> Bool {
        var a = arr.sorted()
        let d = a[1] - a[0]
        for i in 2..<a.count {
            if a[i] - a[i - 1] != d { return false }
        }
        return true
    }
}
