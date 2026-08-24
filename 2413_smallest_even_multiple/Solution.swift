// LeetCode 2413 - Smallest Even Multiple
// https://leetcode.com/problems/smallest-even-multiple/

class Solution {
    func smallestEvenMultiple(_ n: Int) -> Int {
        n % 2 == 0 ? n : n * 2
    }
}
