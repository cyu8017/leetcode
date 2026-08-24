// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

class Solution {
    func minUnlockedIndices(_ nums: [Int], _ locked: [Int]) -> Int {
        let n = nums.count
        var need = false
        for i in 1..<n where nums[i] < nums[i - 1] { need = true; break }
        if !need { return 0 }
        var left = n, right = -1
        for i in 0..<n {
            for j in (i + 1)..<n where nums[i] > nums[j] {
                if i < left { left = i }
                if j > right { right = j }
            }
        }
        if right < left { return 0 }
        var ans = 0
        for i in left...right where locked[i] == 1 { ans += 1 }
        var tmp = nums
        var lock = locked
        for i in left...right { lock[i] = 0 }
        var changed = true
        while changed {
            changed = false
            for i in 0..<(n - 1) {
                if lock[i] == 0 && lock[i + 1] == 0 && tmp[i] > tmp[i + 1] {
                    tmp.swapAt(i, i + 1)
                    changed = true
                }
            }
        }
        for i in 1..<n where tmp[i] < tmp[i - 1] { return -1 }
        return ans
    }
}
