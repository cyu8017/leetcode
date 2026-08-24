// LeetCode 2150 - Find All Lonely Numbers in the Array
// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

class Solution {
    fun findLonely(nums: IntArray): MutableList<Int> {
        var freq = HashMap()
        for (x in nums) freq.merge(x, 1, Int::sum)
        var ans = mutableListOf()
        for (kv in freq.entrySet())
            if (kv.getValue() == 1 && !freq.containsKey(kv.getKey() - 1) && !freq.containsKey(kv.getKey() + 1))
                ans.add(kv.getKey())
        return ans
    }
}
