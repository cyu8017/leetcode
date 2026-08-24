// LeetCode 0989 - Add to Array-Form of Int
// https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution {
    fun addToArrayForm(num: IntArray, k: Int): MutableList<Int> {
var list: MutableList<Int> = mutableListOf()
for (x in num) {
list.add(x)
}
var i: Int = list.size - 1
while (k > 0 || i >= 0) {
if (i >= 0) {
k += list[i]
list.set(i, k % 10)
i--
}
else {
list.add(0, k % 10)
}
k /= 10
}
return list
}
}
