// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

class Solution {
    func rotateElements(_ nums: [Int], _ k: Int) -> [Int] {
        var nums = nums
        var t = [Int]()
        for x in nums where x >= 0 { t.append(x) }
        let m = t.count
        if m == 0 { return nums }
        var d = [Int](repeating: 0, count: m)
        for i in 0..<m { d[((i - k) % m + m) % m] = t[i] }
        var j = 0
        for i in 0..<nums.count {
            if nums[i] >= 0 {
                nums[i] = d[j]
                j += 1
            }
        }
        return nums
    }
}
