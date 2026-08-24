// LeetCode 2164 - Sort Even and Odd Indices Independently
// https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution {
    func sortEvenOdd(_ nums: [Int]) -> [Int] {
        var even = [Int](), odd = [Int]()
        for i in 0..<nums.count {
            if i % 2 == 0 { even.append(nums[i]) }
            else { odd.append(nums[i]) }
        }
        even.sort()
        odd.sort(by: >)
        var ans = nums
        var ei = 0, oi = 0
        for i in 0..<ans.count {
            if i % 2 == 0 { ans[i] = even[ei]; ei += 1 }
            else { ans[i] = odd[oi]; oi += 1 }
        }
        return ans
    }
}
