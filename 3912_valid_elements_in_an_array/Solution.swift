// LeetCode 3912 - Valid Elements In An Array
// https://leetcode.com/problems/valid-elements-in-an-array/

class Solution {
    func findValidElements(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var right = [Int](repeating: 0, count: n)
        right[n - 1] = nums[n - 1]
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                right[i] = max(right[i + 1], nums[i])
            }
        }
        var left = 0
        var ans = [Int]()
        for i in 0..<n {
            let x = nums[i]
            if x > left || i == n - 1 || x > right[i + 1] { ans.append(x) }
            left = max(left, x)
        }
        return ans
    }
}
