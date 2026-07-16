// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

class Solution {
    func findPermutation(_ s: String) -> [Int] {
        var stack = [1]
        var result: [Int] = []
        for ch in s {
            if ch == "I" {
                while !stack.isEmpty {
                    result.append(stack.removeLast())
                }
            }
            stack.append(stack.count + result.count + 1)
        }
        while !stack.isEmpty {
            result.append(stack.removeLast())
        }
        return result
    }
}
