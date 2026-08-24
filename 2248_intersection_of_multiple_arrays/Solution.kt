// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution {

    fun intersection(nums: Array<IntArray>): MutableList<Int> {

            var freq = HashMap<Int, Int>()
            for (arr in nums) {
                var seen = HashSet<Int>()
                for (x in arr) {
                    if (seen.add(x)) freq.put(x, freq.getOrDefault(x, 0) + 1)
                }
            }
            var ans = ArrayList<Int>()
            for (kv in freq.entries)
                if (kv.getValue() == nums.size) ans.add(kv.getKey())
            ans.sort()
            return ans

    }

}
