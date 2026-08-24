// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

class Solution {
    fun minimumIndex(capacity: IntArray, itemSize: Int): Int {
        var ans = -1
        for (i in 0 until capacity.size) {
            if (capacity[i] >= itemSize && (ans == -1 || capacity[i] < capacity[ans])) ans = i
        }
        return ans
    }
}
