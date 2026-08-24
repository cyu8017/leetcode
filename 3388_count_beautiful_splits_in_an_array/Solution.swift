// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

class Solution {
    func beautifulSplits(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        if n < 3 { return 0 }
        for i in 1..<(n - 1) {
            for j in (i + 1)..<n {
                var ok = false
                if i <= j - i && equal(nums, 0, i, i, i + i) { ok = true }
                if !ok && j - i <= n - j && equal(nums, i, j, j, j + (j - i)) { ok = true }
                if ok { ans += 1 }
            }
        }
        return ans
    }

    private func equal(_ a: [Int], _ as_: Int, _ ae: Int, _ bs: Int, _ be: Int) -> Bool {
        if ae - as_ != be - bs { return false }
        for i in 0..<(ae - as_) where a[as_ + i] != a[bs + i] { return false }
        return true
    }
}
