// LeetCode 0458 - Poor Pigs
// https://leetcode.com/problems/poor-pigs/

class Solution {
    func poorPigs(_ buckets: Int, _ minutesToDie: Int, _ minutesToTest: Int) -> Int {
        let states = minutesToTest / minutesToDie + 1
        var pigs = 0
        var capacity = 1
        while capacity < buckets {
            pigs += 1
            capacity *= states
        }
        return pigs
    }
}
