// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

class Solution {
    func minKBitFlips(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var flip = [Int](repeating: 0, count: n)
        var ans = 0, flipped = 0
        for i in 0..<n {
            if i >= k { flipped ^= flip[i - k] }
            if nums[i] == flipped {
                if i + k > n { return -1 }
                ans += 1
                flipped ^= 1
                flip[i] = 1
            }
        }
        return ans
    }
}
