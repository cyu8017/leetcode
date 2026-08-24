// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

class Solution {
    fun numberOfCleanRooms(room: Array<IntArray>): Int {
var m: Int = room.size
var n: Int = room[0].size
var dirs: Array<IntArray> = arrayOf(intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(-1, 0))
var vis: HashSet<Int> = HashSet()
var cleaned: HashSet<Long> = HashSet()
cleaned.add(0L)
var r: Int = 0
var c: Int = 0
var d: Int = 0
while (vis.add(r * 10000 + c * 10 + d)) {
var nr: Int = r + dirs[d][0]
var nc: Int = c + dirs[d][1]
if (nr >= 0 && nr < m && nc >= 0 && nc < n && room[nr][nc] == 0) {
r = nr
c = nc
cleaned.add(((r.toLong()) << 32) ^ (c & 0xffffffffL))
}
else {
d = (d + 1) % 4
}
}
return cleaned.size
}
}
