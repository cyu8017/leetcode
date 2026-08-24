// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

class Solution {
    func maxContainers(_ n: Int, _ w: Int, _ maxWeight: Int) -> Int {
        let cap = n * n
        let byW = maxWeight / w
        return min(cap, byW)
    }
}
