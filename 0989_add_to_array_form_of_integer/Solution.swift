// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution {
    func addToArrayForm(_ num: [Int], _ k: Int) -> [Int] {
        var list = num
        var k = k
        var i = list.count - 1
        while k > 0 || i >= 0 {
            if i >= 0 {
                k += list[i]
                list[i] = k % 10
                i -= 1
            } else {
                list.insert(k % 10, at: 0)
            }
            k /= 10
        }
        return list
    }
}
