// LeetCode 0986 - Interval List Intersections
// https://leetcode.com/problems/interval-list-intersections/

class Solution {
    fun intervalIntersection(firstList: Array<IntArray>, secondList: Array<IntArray>): Array<IntArray> {
var i: Int = 0
var j: Int = 0
var ans: MutableList<IntArray> = mutableListOf()
while (i < firstList.size && j < secondList.size) {
var lo: Int = maxOf(firstList[i][0], secondList[j][0])
var hi: Int = minOf(firstList[i][1], secondList[j][1])
if (lo <= hi) {
ans.add(intArrayOf( lo, hi ))
}
if (firstList[i][1] < secondList[j][1]) {
i++
}
else {
j++
}
}
return ans.toArray(IntArray(0)[])
}
}
