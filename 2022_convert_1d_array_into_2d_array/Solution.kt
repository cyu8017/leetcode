// LeetCode 2022 - Convert 1D Array Into 2D Array
// https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution {
    fun construct2DArray(original: IntArray, m: Int, n: Int): Array<IntArray> {
if (original.size != m * n) {
return IntArray(0)[]
}
var ans: Array<IntArray> = Array(m) { IntArray(n) }
for (i in 0 until m) {
for (j in 0 until n) {
ans[i][j] = original[i * n + j]
}
}
return ans
}
}
