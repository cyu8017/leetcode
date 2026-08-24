// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution {
    fun maximumBeauty(items: Array<IntArray>, queries: IntArray): IntArray {
Arrays.sort(items, (a, b) -> Int.compare(a[0], b[0]))
var maxB: Int = 0
for (it in items) {
maxB = maxOf(maxB, it[1])
it[1] = maxB
}
var ans: IntArray = IntArray(queries.size)
for (i in 0 until queries.size) {
var lo: Int = 0
var hi: Int = items.size
while (lo < hi) {
var mid: Int = (lo + hi) / 2
if (items[mid][0] <= queries[i]) {
lo = mid + 1
}
else {
hi = mid
}
}
ans[i] = if (lo == 0) 0 else items[lo - 1][1]
}
return ans
}
}
