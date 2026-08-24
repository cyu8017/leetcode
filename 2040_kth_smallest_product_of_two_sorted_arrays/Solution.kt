// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

class Solution {
    fun kthSmallestProduct(nums1: IntArray, nums2: IntArray, k: Long): Long {
var lo: Long = -10_000_000_000L
var hi: Long = 10_000_000_000L
while (lo < hi) {
var mid: Long = lo + (hi - lo) / 2
if (countLE(nums1, nums2, mid) >= k) {
hi = mid
}
else {
lo = mid + 1
}
}
return lo
}

    private fun countLE(nums1: IntArray, nums2: IntArray, x: Long): Long {
var cnt: Long = 0
for (a in nums1) {
if (a > 0) {
var lo: Int = 0
var hi: Int = nums2.size
while (lo < hi) {
var mid: Int = (lo + hi) / 2
if (a.toLong() * nums2[mid] <= x) {
lo = mid + 1
}
else {
hi = mid
}
}
cnt += lo
}
else if (a < 0) {
var lo: Int = 0
var hi: Int = nums2.size
while (lo < hi) {
var mid: Int = (lo + hi) / 2
if (a.toLong() * nums2[mid] <= x) {
hi = mid
}
else {
lo = mid + 1
}
}
cnt += nums2.size - lo
}
else if (x >= 0) {
cnt += nums2.size
}
}
return cnt
}
}
