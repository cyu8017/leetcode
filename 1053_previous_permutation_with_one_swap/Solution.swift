// LeetCode 1053 - Previous Permutation With One Swap
// https://leetcode.com/problems/previous-permutation-with-one-swap/

class Solution {
    func prevPermOpt1(_ arr: [Int]) -> [Int] {
        var arr = arr
        let n = arr.count
        var i = n - 2
        while i >= 0 && arr[i] <= arr[i + 1] {
            i -= 1
        }
        if i < 0 {
            return arr
        }
        var j = n - 1
        while arr[j] >= arr[i] || arr[j] == arr[j - 1] {
            j -= 1
        }
        arr.swapAt(i, j)
        return arr
    }
}
