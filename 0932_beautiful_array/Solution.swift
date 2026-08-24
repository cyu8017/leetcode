// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

class Solution {
    func beautifulArray(_ n: Int) -> [Int] {
        if n == 1 { return [1] }
        let left = beautifulArray((n + 1) / 2)
        let right = beautifulArray(n / 2)
        return left.map { 2 * $0 - 1 } + right.map { 2 * $0 }
    }
}
