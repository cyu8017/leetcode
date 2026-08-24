// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution {
    fun findOriginalArray(changed: IntArray): IntArray {
if (changed.size % 2 != 0) {
return IntArray(0)
}
changed.sort()
var freq: HashMap<Int, Int> = HashMap()
for (x in changed) {
freq.merge(x, 1, { a, b -> a + b })
}
var ans: MutableList<Int> = mutableListOf()
for (x in changed) {
if (freq.getOrDefault(x, 0) == 0) {
continue
}
freq.put(x, freq[x] - 1)
if (freq.getOrDefault(2 * x, 0) == 0) {
return IntArray(0)
}
freq.put(2 * x, freq[2 * x] - 1)
ans.add(x)
}
return ans.stream().mapToInt(i -> i).toArray()
}
}
