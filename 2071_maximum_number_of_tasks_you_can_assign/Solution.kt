// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

class Solution {
    fun maxTaskAssign(tasks: IntArray, workers: IntArray, pills: Int, strength: Int): Int {
tasks.sort()
workers.sort()
var lo: Int = 0, hi = minOf(tasks.size, workers.size)
while (lo < hi) {
var mid: Int = (lo + hi + 1) / 2
if (can(tasks, workers, pills, strength, mid)) {
lo = mid
}
else {
hi = mid - 1
}
}
return lo
}

    private fun can(tasks: IntArray, workers: IntArray, pills: Int, strength: Int, k: Int): Boolean {
if (k == 0) {
return true
}
var ws: java.util.TreeMap<Int, Int> = java.util.TreeMap()
for (i in workers.size - k until workers.size) {
ws.merge(workers[i], 1, { a, b -> a + b })
}
var p: Int = pills
for (i in k - 1 downTo 0) {
var task: Int = tasks[i]
var strongest: Int = ws.lastKey()
if (strongest >= task) {
remove(ws, strongest)
continue
}
if (p == 0) {
return false
}
var need: Int = task - strength
var found: Int = ws.ceilingKey(need)
if (found == null) {
return false
}
remove(ws, found)
p--
}
return true
}

    private fun remove(ws: java.util.TreeMap<Int, Int>, x: Int) {
var c: Int = ws[x]
if (c == 1) {
ws.remove(x)
}
else {
ws.put(x, c - 1)
}
}
}
