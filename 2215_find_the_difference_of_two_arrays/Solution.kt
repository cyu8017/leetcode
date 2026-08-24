// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution {

    fun findDifference(nums1: IntArray, nums2: IntArray): MutableList<MutableList<Int>> {

            var s1 = HashSet<Int>()
            var s2 = HashSet<Int>()
            for (x in nums1) s1.add(x)
            for (x in nums2) s2.add(x)
            var a = ArrayList<Int>()
            var b = ArrayList<Int>()
            for (x in s1) if (!s2.contains(x)) a.add(x)
            for (x in s2) if (!s1.contains(x)) b.add(x)
            var ans = ArrayList<Int>()
            ans.add(a)
            ans.add(b)
            return ans

    }

}
