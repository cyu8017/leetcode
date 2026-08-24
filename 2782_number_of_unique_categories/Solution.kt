// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

interface CategoryHandler {
    fun haveSameCategory(a: Int, b: Int): Boolean
}

class Solution {
    fun numberOfCategories(n: Int, categoryHandler: CategoryHandler): Int {
        val parent = IntArray(n) { it }
        fun find(x0: Int): Int {
            var x = x0
            while (parent[x] != x) {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (categoryHandler.haveSameCategory(i, j)) {
                    val a = find(i)
                    val b = find(j)
                    if (a != b) parent[a] = b
                }
            }
        }
        var ans = 0
        for (i in 0 until n) if (find(i) == i) ans++
        return ans
    }
}
