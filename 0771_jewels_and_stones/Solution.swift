// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

class Solution {
    func numJewelsInStones(_ jewels: String, _ stones: String) -> Int {
        let set = Set(jewels)
        return stones.filter { set.contains($0) }.count
    }
}
