// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

class Solution {
    fun twoOutOfThree(nums1: IntArray, nums2: IntArray, nums3: IntArray): IntArray {
var s0: HashSet<Int> = HashSet(), s1 = HashSet(), s2 = HashSet()
for (v in nums1) {
s0.add(v)
}
for (v in nums2) {
s1.add(v)
}
for (v in nums3) {
s2.add(v)
}
var ans: MutableList<Int> = mutableListOf()
for (v in 1 ..100) {
var c: Int = (if (s0.contains(v)) 1 else 0) + (if (s1.contains(v)) 1 else 0) + (if (s2.contains(v)) 1 else 0)
if (c >= 2) {
ans.add(v)
}
}
return ans.stream().mapToInt(i -> i).toArray()
}
}
