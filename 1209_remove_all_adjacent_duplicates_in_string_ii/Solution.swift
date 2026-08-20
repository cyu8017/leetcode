// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution {
    func removeDuplicates(_ s: String, _ k: Int) -> String {
        var stack: [(Character, Int)] = []
        for ch in s {
            if let last = stack.last, last.0 == ch {
                stack[stack.count - 1].1 += 1
                if stack[stack.count - 1].1 == k { stack.removeLast() }
            } else {
                stack.append((ch, 1))
            }
        }
        return stack.map { String(repeating: $0.0, count: $0.1) }.joined()
    }
}
