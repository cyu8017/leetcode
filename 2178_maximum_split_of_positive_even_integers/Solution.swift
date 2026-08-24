// LeetCode 2178 - Maximum Split of Positive Even Integers
// https://leetcode.com/problems/maximum-split-of-positive-even-integers/

class Solution {
    func maximumEvenSplit(_ finalSum: Int) -> [Int] {
        if finalSum % 2 != 0 { return [] }
        var finalSum = finalSum
        var ans = [Int]()
        var x = 2
        while x <= finalSum {
            ans.append(x)
            finalSum -= x
            x += 2
        }
        ans[ans.count - 1] += finalSum
        return ans
    }
}
