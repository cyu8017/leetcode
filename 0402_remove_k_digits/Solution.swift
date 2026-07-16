// LeetCode 0402 - Remove K Digits
// https://leetcode.com/problems/remove-k-digits/

class Solution {
    func removeKdigits(_ num: String, _ k: Int) -> String {
        var stack: [Character] = []
        var remaining = k

        for digit in num {
            while remaining > 0, let last = stack.last, last > digit {
                stack.removeLast()
                remaining -= 1
            }
            stack.append(digit)
        }

        if remaining > 0 {
            stack.removeLast(remaining)
        }

        let result = String(stack).trimmingCharacters(in: CharacterSet(charactersIn: "0"))
        return result.isEmpty ? "0" : result
    }
}
