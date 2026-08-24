// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

class Solution {
    func f(_ x0: Int) -> Int {
        var x = x0, s = 0
        while x != 0 { s += x % 10; x /= 10 }
        return s
    }

    func minSwaps(_ nums: [Int]) -> Int {
        let n = nums.count
        var arr = (0..<n).map { [f(nums[$0]), nums[$0]] }
        arr.sort { $0[0] != $1[0] ? $0[0] < $1[0] : $0[1] < $1[1] }
        var d = [Int: Int]()
        for i in 0..<n { d[arr[i][1]] = i }
        var vis = Array(repeating: false, count: n)
        var ans = n
        for i in 0..<n {
            if !vis[i] {
                ans -= 1
                var j = i
                while !vis[j] {
                    vis[j] = true
                    j = d[nums[j]]!
                }
            }
        }
        return ans
    }
}
