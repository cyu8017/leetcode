// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

class Solution {
    func sleep(_ millis: Int) {
        Thread.sleep(forTimeInterval: Double(millis) / 1000.0)
    }
}
