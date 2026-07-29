// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

class Solution {
    func addNegabinary(_ arr1: [Int], _ arr2: [Int]) -> [Int] {
        var i = arr1.count - 1
        var j = arr2.count - 1
        var carry = 0
        var ans: [Int] = []
        while i >= 0 || j >= 0 || carry != 0 {
            var total = carry
            if i >= 0 {
                total += arr1[i]
                i -= 1
            }
            if j >= 0 {
                total += arr2[j]
                j -= 1
            }
            ans.append(total & 1)
            carry = -(total >> 1)
        }
        while ans.count > 1 && ans.last == 0 {
            ans.removeLast()
        }
        return ans.reversed()
    }
}
