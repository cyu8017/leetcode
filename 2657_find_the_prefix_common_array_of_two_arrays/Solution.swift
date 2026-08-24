// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution {
    func findThePrefixCommonArray(_ A: [Int], _ B: [Int]) -> [Int] {
        let n = A.count
        var seenA = Array(repeating: false, count: n + 1)
        var seenB = Array(repeating: false, count: n + 1)
        var ans = Array(repeating: 0, count: n)
        var common = 0
        for i in 0..<n {
            if seenB[A[i]] { common += 1 }
            seenA[A[i]] = true
            if seenA[B[i]] { common += 1 }
            seenB[B[i]] = true
            ans[i] = common
        }
        return ans
    }
}
