// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

class Solution {
    fun containVirus(isInfected: Array<IntArray>): Int {
        val m = isInfected.size
        val n = isInfected[0].size
        var walls = 0
        while (true) {
            val seen = HashSet<Long>()
            val regions = ArrayList<MutableSet<Long>>()
            val frontiers = ArrayList<MutableSet<Long>>()
            val perimeters = ArrayList<Int>()
            for (i in 0 until m) {
                for (j in 0 until n) {
                    val key = (i.toLong() shl 32) or (j.toLong() and 0xffffffffL)
                    if (isInfected[i][j] == 1 && !seen.contains(key)) {
                        val stack = ArrayList<LongArray>()
                        stack.add(longArrayOf(i.toLong(), j.toLong()))
                        seen.add(key)
                        val region = HashSet<Long>()
                        val frontier = HashSet<Long>()
                        var perimeter = 0
                        val dirs = arrayOf(
                            intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1)
                        )
                        while (stack.isNotEmpty()) {
                            val cur = stack.removeAt(stack.size - 1)
                            val r = cur[0].toInt()
                            val c = cur[1].toInt()
                            region.add((r.toLong() shl 32) or (c.toLong() and 0xffffffffL))
                            for (d in dirs) {
                                val nr = r + d[0]
                                val nc = c + d[1]
                                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue
                                val nk = (nr.toLong() shl 32) or (nc.toLong() and 0xffffffffL)
                                if (isInfected[nr][nc] == 1 && seen.add(nk)) {
                                    stack.add(longArrayOf(nr.toLong(), nc.toLong()))
                                } else if (isInfected[nr][nc] == 0) {
                                    frontier.add(nk)
                                    perimeter++
                                }
                            }
                        }
                        regions.add(region)
                        frontiers.add(frontier)
                        perimeters.add(perimeter)
                    }
                }
            }
            if (regions.isEmpty()) break
            var quarantine = 0
            for (i in 1 until regions.size) {
                if (frontiers[i].size > frontiers[quarantine].size) quarantine = i
            }
            if (frontiers[quarantine].isEmpty()) break
            walls += perimeters[quarantine]
            for (cell in regions[quarantine]) {
                val r = (cell shr 32).toInt()
                val c = cell.toInt()
                isInfected[r][c] = -1
            }
            for (index in frontiers.indices) {
                if (index == quarantine) continue
                for (cell in frontiers[index]) {
                    val r = (cell shr 32).toInt()
                    val c = cell.toInt()
                    isInfected[r][c] = 1
                }
            }
        }
        return walls
    }
}
