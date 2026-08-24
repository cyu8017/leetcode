// LeetCode 2177 - Find Three Consecutive Integers That Sum to a Given Number
// https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution {
    func sumOfThree(_ num: Int) -> [Int] {
        if num % 3 != 0 { return [] }
        let x = num / 3
        return [x - 1, x, x + 1]
    }
}
