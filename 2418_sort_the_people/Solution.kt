// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

class Solution {
    fun sortPeople(names: Array<String>, heights: IntArray): Array<String> {
        val n = names.size
        val idx = Array(n) { it }
        idx.sortWith(compareByDescending { heights[it] })
        return Array(n) { names[idx[it]] }
    }
}
