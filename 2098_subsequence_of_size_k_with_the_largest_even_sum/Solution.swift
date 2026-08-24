// LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
// https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

class Solution {
    func largestEvenSum(_ nums: [Int], _ k: Int) -> Int {
        let arr = nums.sorted(by: >)
        var sum = arr[0..<k].reduce(0, +)
        if sum % 2 == 0 { return sum }
        var ans = -1
        var oddIn = -1, evenIn = -1, oddOut = -1, evenOut = -1
        for i in stride(from: k - 1, through: 0, by: -1) {
            if arr[i] % 2 != 0 && oddIn == -1 { oddIn = i }
            if arr[i] % 2 == 0 && evenIn == -1 { evenIn = i }
        }
        for i in k..<arr.count {
            if arr[i] % 2 != 0 && oddOut == -1 { oddOut = i }
            if arr[i] % 2 == 0 && evenOut == -1 { evenOut = i }
        }
        if oddIn != -1 && evenOut != -1 { ans = max(ans, sum - arr[oddIn] + arr[evenOut]) }
        if evenIn != -1 && oddOut != -1 { ans = max(ans, sum - arr[evenIn] + arr[oddOut]) }
        return ans
    }
}
