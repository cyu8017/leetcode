// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

class Solution {
    fun findSmallestRegion(regions: List<List<String>>, region1: String, region2: String): String {
        val parent = mutableMapOf<String, String>()
        for (group in regions) {
            for (i in 1 until group.size) parent[group[i]] = group[0]
        }
        val ancestors = mutableSetOf<String>()
        var r1: String? = region1
        while (r1 != null) {
            ancestors.add(r1)
            r1 = parent[r1]
        }
        var r2 = region2
        while (r2 !in ancestors) r2 = parent[r2]!!
        return r2
    }
}
