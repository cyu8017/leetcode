// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

class Solution {
    fun minimumBuckets(hamsters: String): Int {
var b: CharArray = hamsters.toCharArray()
var ans: Int = 0
for (i in 0 until b.size) {
if (b[i] != 'H') {
continue
}
if (i > 0 && b[i - 1] == 'B') {
continue
}
if (i + 1 < b.size && b[i + 1] == '.') {
b[i + 1] = 'B'
ans++
}
else if (i > 0 && b[i - 1] == '.') {
b[i - 1] = 'B'
ans++
}
else {
return -1
}
}
return ans
}
}
