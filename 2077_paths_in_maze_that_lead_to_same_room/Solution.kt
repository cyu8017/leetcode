// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

class Solution {
    fun numberOfPaths(n: Int, corridors: Array<IntArray>): Int {
var g: Array<HashSet<Int>> = new HashSet[n + 1]
for (i in 0 ..n) {
g[i] = HashSet()
}
for (e in corridors) {
g[e[0]].add(e[1])
g[e[1]].add(e[0])
}
var ans: Int = 0
for (e in corridors) {
var a: Int = e[0]
var b: Int = e[1]
for (c in g[a]) {
if (g[b].contains(c)) {
ans++
}
}
}
return ans / 3
}
}
