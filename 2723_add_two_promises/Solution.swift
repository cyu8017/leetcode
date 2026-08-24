// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

class Solution {
    func addTwoPromises(_ promise1: () -> Int, _ promise2: () -> Int) -> Int {
        promise1() + promise2()
    }
}
