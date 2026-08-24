// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

class Solution {
    fun maxContainers(n: Int, w: Int, maxWeight: Int): Int {
        var cap = n * n
        var byW = maxWeight / w
        return if (cap < byW) cap else byW
    }
}
