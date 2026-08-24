// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution {
    private var parent: HashMap<Int, Int> = HashMap<Int, Int>()

    fun removeStones(stones: Array<IntArray>): Int {
        for (s in stones) { unite(s[0], ~s[1]); }
        var roots = HashSet<Int>()
        for (s in stones) { roots.add(find(s[0])); }
        return stones.size - roots.size
    }

    private fun find(x: Int): Int {
        if (!parent.containsKey(x)) parent.put(x, x)
        if (parent[x] != x) parent.put(x, find(parent[x]))
        return parent[x]
    }

    private fun unite(a: Int, b: Int) {
        parent.put(find(a), find(b))
    }
}
