// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

class Solution {
    private static class Fenwick {
        private lateinit var bit: IntArray
      fun Fenwick(n: Int):  {
bit = IntArray(n + 2)
}
        fun add(i: Int, v: Int) {
for (; i < bit.size; i += i & -i) {
bit[i] += v
}
}
        fun sum(i: Int): Int {
var s: Int = 0
for (; i > 0; i -= i & -i) {
s += bit[i]
}
return s
}
    }

    fun subarraysWithMoreZerosThanOnes(nums: IntArray): Int {
val MOD: Int = 1_000_000_007
var n: Int = nums.size
var offset: Int = n + 1
var fw: Fenwick = Fenwick(2 * n + 5)
var pref: Int = 0
var ans: Int = 0
fw.add(offset, 1)
for (x in nums) {
pref += if ((x == 1)) 1 else -1
var idx: Int = pref + offset
ans = (ans + fw.sum(idx - 1)) % MOD
fw.add(idx, 1)
}
return ans
}
}
