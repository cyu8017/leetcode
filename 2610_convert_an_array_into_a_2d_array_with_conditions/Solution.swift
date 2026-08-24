// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution {
    func findMatrix(_ nums: [Int]) -> [[Int]] {
        var freq = [Int: Int]()
        var ans = [[Int]]()
        for x in nums {
            let f = freq[x, default: 0]
            if f == ans.count { ans.append([]) }
            ans[f].append(x)
            freq[x] = f + 1
        }
        return ans
    }
}
