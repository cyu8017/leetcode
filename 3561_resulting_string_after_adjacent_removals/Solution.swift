// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

class Solution {
    func isContiguous(_ a: Character, _ b: Character) -> Bool {
        let x = abs(Int(a.asciiValue!) - Int(b.asciiValue!))
        return x == 1 || x == 25
    }

    func resultingString(_ s: String) -> String {
        var stk = [Character]()
        for c in s {
            if let last = stk.last, isContiguous(last, c) { stk.removeLast() }
            else { stk.append(c) }
        }
        return String(stk)
    }
}
