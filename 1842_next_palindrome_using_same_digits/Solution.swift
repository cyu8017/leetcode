// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

class Solution {
    func nextPalindrome(_ num: String) -> String {
        var nums = Array(num)
        if !nextPermutation(&nums) { return "" }
        let n = nums.count
        for i in 0..<(n / 2) {
            nums[n - i - 1] = nums[i]
        }
        return String(nums)
    }

    private func nextPermutation(_ nums: inout [Character]) -> Bool {
        let n = nums.count / 2
        var i = n - 2
        while i >= 0 && nums[i] >= nums[i + 1] { i -= 1 }
        if i < 0 { return false }
        var j = n - 1
        while nums[j] <= nums[i] { j -= 1 }
        nums.swapAt(i, j)
        nums[(i + 1)..<n].reverse()
        return true
    }
}
