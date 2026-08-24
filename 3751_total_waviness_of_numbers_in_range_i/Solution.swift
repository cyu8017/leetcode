// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution {
    private func F(_ x: Int) -> Int {
        var x = x
        var nums = [Int]()
        while x > 0 {
            nums.append(x % 10)
            x /= 10
        }
        let m = nums.count
        if m < 3 { return 0 }
        var s = 0
        for i in 1..<(m - 1) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ||
               (nums[i] < nums[i - 1] && nums[i] < nums[i + 1]) {
                s += 1
            }
        }
        return s
    }

    func totalWaviness(_ num1: Int, _ num2: Int) -> Int {
        var ans = 0
        for x in num1...num2 { ans += F(x) }
        return ans
    }
}
