// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

class Solution {
    func countGoodSubarrays(_ nums: [Int]) -> Int {
        let n = nums.count
        var l = [Int](repeating: -1, count: n)
        var stk = [Int]()
        for i in 0..<n {
            let x = nums[i]
            while !stk.isEmpty && nums[stk.last!] < x && (nums[stk.last!] | x) == x {
                stk.removeLast()
            }
            if !stk.isEmpty { l[i] = stk.last! }
            stk.append(i)
        }
        var r = [Int](repeating: n, count: n)
        stk = []
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !stk.isEmpty && (nums[stk.last!] | nums[i]) == nums[i] {
                stk.removeLast()
            }
            if !stk.isEmpty { r[i] = stk.last! }
            stk.append(i)
        }
        var ans = 0
        for i in 0..<n { ans += (i - l[i]) * (r[i] - i) }
        return ans
    }
}
