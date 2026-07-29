// LeetCode 1095 - Find in Mountain Array
// https://leetcode.com/problems/find-in-mountain-array/

interface MountainArray {
    fun get(index: Int): Int
    fun length(): Int
}

class Solution {
    fun findInMountainArray(target: Int, mountainArr: MountainArray): Int {
        val n = mountainArr.length()
        var lo = 0
        var hi = n - 1
        while (lo < hi) {
            val mid = lo + (hi - lo) / 2
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) lo = mid + 1 else hi = mid
        }
        val peak = lo
        lo = 0
        hi = peak
        while (lo <= hi) {
            val mid = lo + (hi - lo) / 2
            val `val` = mountainArr.get(mid)
            if (`val` == target) return mid
            if (`val` < target) lo = mid + 1 else hi = mid - 1
        }
        lo = peak + 1
        hi = n - 1
        while (lo <= hi) {
            val mid = lo + (hi - lo) / 2
            val `val` = mountainArr.get(mid)
            if (`val` == target) return mid
            if (`val` > target) lo = mid + 1 else hi = mid - 1
        }
        return -1
    }
}
