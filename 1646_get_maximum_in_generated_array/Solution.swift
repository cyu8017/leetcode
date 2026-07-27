// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution {
    func getMaximumGenerated(_ n: Int) -> Int {
        if n < 2 { return n }
        var a = [Int](repeating: 0, count: n + 1)
        a[1] = 1
        for i in 2...n {
            if i % 2 == 0 {
                a[i] = a[i / 2]
            } else {
                a[i] = a[i / 2] + a[i / 2 + 1]
            }
        }
        return a.max()!
    }
}
