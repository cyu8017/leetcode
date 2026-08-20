// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution {
    func replaceElements(_ arr: [Int]) -> [Int] {
        var arr = arr
        var greatest = -1
        for i in stride(from: arr.count - 1, through: 0, by: -1) {
            let current = arr[i]
            arr[i] = greatest
            greatest = max(greatest, current)
        }
        return arr
    }
}
