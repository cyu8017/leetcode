// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

class Solution {
    func powerfulIntegers(_ x: Int, _ y: Int, _ bound: Int) -> [Int] {
        var ans = Set<Int>()
        var a = 1
        while a < bound {
            var b = 1
            while a + b <= bound {
                ans.insert(a + b)
                if y == 1 { break }
                b *= y
            }
            if x == 1 { break }
            a *= x
        }
        return Array(ans)
    }
}
