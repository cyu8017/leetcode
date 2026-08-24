// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/


class Solution {
    func countRatioSubarrays(_ nums: [Int], _ a: Int, _ b: Int) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var y = 0
            for j in i..<n {
                y += nums[j] % 2
                let x = j - i + 1 - y
                if y > 0 && x * b <= y * a { ans += 1 }
            }
        }
        return ans
    }
}
