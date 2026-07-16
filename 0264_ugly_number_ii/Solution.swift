// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

class Solution {
    func nthUglyNumber(_ n: Int) -> Int {
        var ugly = [1]
        var index2 = 0
        var index3 = 0
        var index5 = 0
        while ugly.count < n {
            let nextUgly = min(
                ugly[index2] * 2,
                ugly[index3] * 3,
                ugly[index5] * 5
            )
            ugly.append(nextUgly)
            if nextUgly == ugly[index2] * 2 {
                index2 += 1
            }
            if nextUgly == ugly[index3] * 3 {
                index3 += 1
            }
            if nextUgly == ugly[index5] * 5 {
                index5 += 1
            }
        }
        return ugly[ugly.count - 1]
    }
}
