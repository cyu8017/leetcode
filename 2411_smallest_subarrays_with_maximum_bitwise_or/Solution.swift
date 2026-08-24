// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

class Solution {
    func smallestSubarrays(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = [Int](repeating: 0, count: n)
        var last = [Int](repeating: -1, count: 32)
        for i in stride(from: n - 1, through: 0, by: -1) {
            for b in 0..<32 where ((nums[i] >> b) & 1) != 0 { last[b] = i }
            var far = i
            for b in 0..<32 { far = max(far, last[b]) }
            ans[i] = far - i + 1
        }
        return ans
    }
}
