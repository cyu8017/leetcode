// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

import java.util.TreeMap

class Solution {
    fun mergeSimilarItems(items1: Array<IntArray>, items2: Array<IntArray>): List<List<Int>> {
        val mp = TreeMap<Int, Int>()
        for (it in items1) mp[it[0]] = mp.getOrDefault(it[0], 0) + it[1]
        for (it in items2) mp[it[0]] = mp.getOrDefault(it[0], 0) + it[1]
        val ans = ArrayList<List<Int>>()
        for ((k, v) in mp) ans.add(listOf(k, v))
        return ans
    }
}
