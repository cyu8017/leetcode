// LeetCode 0412 - Fizz Buzz
// https://leetcode.com/problems/fizz-buzz/

class Solution {
    func fizzBuzz(_ n: Int) -> [String] {
        var result: [String] = []
        for value in 1...n {
            if value % 15 == 0 {
                result.append("FizzBuzz")
            } else if value % 3 == 0 {
                result.append("Fizz")
            } else if value % 5 == 0 {
                result.append("Buzz")
            } else {
                result.append(String(value))
            }
        }
        return result
    }
}
