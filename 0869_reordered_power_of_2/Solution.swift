// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

class Solution {
    func reorderedPowerOf2(_ n: Int) -> Bool {
        let target = sig(n)
        for i in 0..<31 {
            if sig(1 << i) == target { return true }
        }
        return false
    }

    private func sig(_ x: Int) -> [Character] {
        return Array(String(x)).sorted()
    }
}
