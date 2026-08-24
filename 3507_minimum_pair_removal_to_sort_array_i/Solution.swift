// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

class Solution {
    func isNonDecreasing(_ a: [Int]) -> Bool {
        for i in 1..<a.count where a[i] < a[i - 1] { return false }
        return true
    }

    func minimumPairRemoval(_ nums: [Int]) -> Int {
        var arr = nums
        var ans = 0
        while !isNonDecreasing(arr) {
            var k = 0
            var s = arr[0] + arr[1]
            if arr.count > 2 {
                for i in 1..<(arr.count - 1) {
                    let t = arr[i] + arr[i + 1]
                    if s > t { s = t; k = i }
                }
            }
            arr[k] = s
            arr.remove(at: k + 1)
            ans += 1
        }
        return ans
    }
}
