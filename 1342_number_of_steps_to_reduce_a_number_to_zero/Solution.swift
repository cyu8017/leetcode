// LeetCode 1342 - Number of Steps to Reduce a Number to Zero
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution {
    func numberOfSteps(_ num: Int) -> Int {
        var num = num, steps = 0
        while num > 0 {
            num = num % 2 == 0 ? num / 2 : num - 1
            steps += 1
        }
        return steps
    }
}
