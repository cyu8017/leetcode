// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

class Solution {
    fun interchangeableRectangles(rectangles: Array<IntArray>): Long {
var freq: HashMap<String, Int> = HashMap()
var ans: Long = 0
for (rect in rectangles) {
var g: Int = gcd(rect[0], rect[1])
var key: String = (rect[0] / g) + "/" + (rect[1] / g)
var f: Int = freq.getOrDefault(key, 0)
ans += f
freq.put(key, f + 1)
}
return ans
}

    private fun gcd(a: Int, b: Int): Int {
while (b != 0) {
var t: Int = a % b
a = b
b = t
}
return a
}
}
