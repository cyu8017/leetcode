// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution {
    func maximumGain(_ s: String, _ x: Int, _ y: Int) -> Int {
        func remove(_ text: [UInt8], _ open: UInt8, _ close: UInt8, _ score: Int) -> ([UInt8], Int) {
            var stack = [UInt8]()
            stack.reserveCapacity(text.count)
            var gained = 0
            for ch in text {
                if let last = stack.last, last == open, ch == close {
                    stack.removeLast()
                    gained += score
                } else {
                    stack.append(ch)
                }
            }
            return (stack, gained)
        }

        let a = UInt8(ascii: "a")
        let b = UInt8(ascii: "b")
        let bytes = Array(s.utf8)
        if x >= y {
            let (rest, first) = remove(bytes, a, b, x)
            let (_, second) = remove(rest, b, a, y)
            return first + second
        } else {
            let (rest, first) = remove(bytes, b, a, y)
            let (_, second) = remove(rest, a, b, x)
            return first + second
        }
    }
}
