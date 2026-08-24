// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

class Solution {
    private lateinit var parent: IntArray

    fun friendRequests(n: Int, restrictions: Array<IntArray>, requests: Array<IntArray>): BooleanArray {
parent = IntArray(n)
for (i in 0 until n) {
parent[i] = i
}
var ans: BooleanArray = BooleanArray(requests.size)
for (i in 0 until requests.size) {
var u: Int = find(requests[i][0]), v = find(requests[i][1])
var ok: Boolean = true
if (u != v) {
for (r in restrictions) {
var x: Int = find(r[0]), y = find(r[1])
if ((x == u && y == v) || (x == v && y == u)) {
ok = false
break
}
}
}
ans[i] = ok
if (ok) {
unite(u, v)
}
}
return ans
}

    private fun find(x: Int): Int {
return if (parent[x] == x) x else (parent[x] = find(parent[x]))
}

    private fun unite(a: Int, b: Int) {
a = find(a)
b = find(b)
if (a != b) {
parent[a] = b
}
}
}
