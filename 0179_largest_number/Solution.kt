class Solution {
    fun largestNumber(nums: IntArray): String {
        val parts = nums.map { it.toString() }
            .sortedWith(Comparator { a, b -> (b + a).compareTo(a + b) })
        return if (parts[0] == "0") "0" else parts.joinToString("")
    }
}
