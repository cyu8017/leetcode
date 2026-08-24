// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

class Solution {
    func totalStrength(_ strength: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = strength.count
        var left = [Int](repeating: 0, count: n)
        var right = [Int](repeating: 0, count: n)
        var stack: [Int] = []
        for i in 0..<n {
            while let last = stack.last, strength[last] >= strength[i] { stack.removeLast() }
            left[i] = stack.last ?? -1
            stack.append(i)
        }
        stack.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, strength[last] > strength[i] { stack.removeLast() }
            right[i] = stack.last ?? n
            stack.append(i)
        }
        var pref = [Int](repeating: 0, count: n + 1)
        var prefPref = [Int](repeating: 0, count: n + 2)
        for i in 0..<n { pref[i + 1] = (pref[i] + strength[i]) % mod }
        for i in 0...n { prefPref[i + 1] = (prefPref[i] + pref[i]) % mod }
        var ans = 0
        for i in 0..<n {
            let l = left[i] + 1, r = right[i] - 1
            let leftSum = (prefPref[i + 1] - prefPref[l] + mod) % mod
            let rightSum = (prefPref[r + 2] - prefPref[i + 1] + mod) % mod
            let leftCnt = i - l + 1, rightCnt = r - i + 1
            let contrib = (rightCnt * leftSum % mod - leftCnt * rightSum % mod + mod) % mod
            ans = (ans + contrib * strength[i] % mod) % mod
        }
        return ans
    }
}
