// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

class Solution {
    func circularPermutation(_ n: Int, _ start: Int) -> [Int] {
        var ans: [Int] = []
        for i in 0..<(1 << n) {
            ans.append(start ^ i ^ (i >> 1))
        }
        return ans
    }
}
