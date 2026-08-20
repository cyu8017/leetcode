// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

protocol CustomFunction {
    func f(_ x: Int, _ y: Int) -> Int
}

class Solution {
    func findSolution(_ customfunction: CustomFunction, _ z: Int) -> [[Int]] {
        var ans: [[Int]] = []
        var x = 1, y = 1000
        while x <= 1000 && y >= 1 {
            let v = customfunction.f(x, y)
            if v == z {
                ans.append([x, y])
                x += 1
                y -= 1
            } else if v < z {
                x += 1
            } else {
                y -= 1
            }
        }
        return ans
    }
}
