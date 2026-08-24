// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

class Solution {
    fun countTriplets(nums: IntArray): Int {
var cnt: HashMap<Int, Int> = HashMap()
for (a in nums) {
for (b in nums) {
cnt.merge(a & b, 1, { a, b -> a + b })
}
}
var ans: Int = 0
for (c in nums) {
for (kv in cnt) {
if ((kv.key & c) == 0) {
ans += kv.value
}
}
}
return ans
}
}
