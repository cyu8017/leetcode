// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution {
    func maxCount(_ banned: [Int], _ n: Int, _ maxSum: Int) -> Int {
        let ban = Set(banned)
        var ans = 0, sum = 0
        for i in 1...n {
            if ban.contains(i) { continue }
            if sum + i > maxSum { break }
            sum += i
            ans += 1
        }
        return ans
    }
}
