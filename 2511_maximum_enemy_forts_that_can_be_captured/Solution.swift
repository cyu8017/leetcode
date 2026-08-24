// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

class Solution {
    func captureForts(_ forts: [Int]) -> Int {
        var ans = 0, prev = -1
        for i in 0..<forts.count where forts[i] != 0 {
            if prev >= 0 && forts[prev] == -forts[i] {
                ans = max(ans, i - prev - 1)
            }
            prev = i
        }
        return ans
    }
}
