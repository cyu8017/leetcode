// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/


class Solution {
    fun findRestaurant(list1: Array<String>, list2: Array<String>): Array<String> {
        val index = HashMap<String, Int>()
        for (i in list1.indices) index[list1[i]] = i
        var best = Int.MAX_VALUE
        val result = ArrayList<String>()
        for (j in list2.indices) {
            val i = index[list2[j]] ?: continue
            val sum = i + j
            if (sum < best) {
                best = sum
                result.clear()
                result.add(list2[j])
            } else if (sum == best) {
                result.add(list2[j])
            }
        }
        return result.toTypedArray()
    }
}
