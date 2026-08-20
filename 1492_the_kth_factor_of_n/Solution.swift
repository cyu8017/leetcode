// LeetCode 1492 - The kth Factor of n
// https://leetcode.com/problems/the-kth-factor-of-n/

class Solution {
    func kthFactor(_ n: Int, _ k: Int) -> Int {
        var k = k
        for x in 1...n where n % x == 0 {
            k -= 1
            if k == 0 { return x }
        }
        return -1
    }
}
