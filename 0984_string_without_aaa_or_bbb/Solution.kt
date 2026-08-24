// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

class Solution {
    fun strWithout3a3b(a: Int, b: Int): String {
var ans: StringBuilder = StringBuilder()
while (a > 0 || b > 0) {
var writeA: Boolean = false
var len: Int = ans.size
if (len >= 2 && ans[len - 1] == ans[len - 2]) {
writeA = ans[len - 1] == 'b'
}
else {
writeA = a >= b
}
if (writeA) {
ans.append('a')
a--
}
else {
ans.append('b')
b--
}
}
return ans.toString()
}
}
