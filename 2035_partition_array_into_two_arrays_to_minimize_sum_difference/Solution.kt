// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

class Solution {
    fun minimumDifference(nums: IntArray): Int {
var n: Int = nums.size / 2
var total: Int = 0
for (v in nums) {
total += v
}
var left: IntArray = Arrays.copyOfRange(nums, 0, n)
var right: IntArray = Arrays.copyOfRange(nums, n, nums.size)
var L: Array<MutableList<Int>> = sumsByCount(left)
var R: Array<MutableList<Int>> = sumsByCount(right)
var ans: Int = Int.MAX_VALUE
for (k in 0 ..n) {
for (s1 in L[k]) {
var need: Int = total / 2 - s1
var arr: MutableList<Int> = R[n - k]
var idx: Int = Collections.binarySearch(arr, need)
if (idx < 0) {
idx = -idx - 1
}
for (j in intArrayOf( idx - 1, idx )) {
if (j >= 0 && j < arr.size) {
var s2: Int = arr[j]
ans = minOf(ans, kotlin.math.abs(total - 2 * (s1 + s2)))
}
}
}
}
return ans
}

    private fun sumsByCount(arr: IntArray): Array<MutableList<Int>> {
var m: Int = arr.size
@SuppressWarnings("unchecked")
        var res: Array<MutableList<Int>> = new ArrayList[m + 1]
for (i in 0 ..m) {
res[i] = mutableListOf()
}
for (mask in 0 until (1 << m)) {
var sum: Int = 0
var c: Int = 0
for (i in 0 until m) {
if ((mask & (1 << i)) != 0) {
sum += arr[i]
c++
}
}
res[c].add(sum)
}
for (v in res) {
v.sort()
}
return res
}
}
