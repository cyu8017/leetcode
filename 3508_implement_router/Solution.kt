// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

class Router {
    var lim = 0
    var vis = HashSet<Long>()
    var q = ArrayDeque<IntArray>()
    var idx = HashMap<Int, Int>()
    var d = HashMap<Int, MutableList<Int>>()

    fun f(a: Int, b: Int, c: Int): Long {
        return (a  shl  46) | (b  shl  29) | c
    }

    constructor(memoryLimit: Int) {
        lim = memoryLimit
    }

    fun addPacket(source: Int, destination: Int, timestamp: Int): Boolean {
        var x = f(source, destination, timestamp)
        if (vis.contains(x)) return false
        vis.add(x)
        if (q.size >= lim) forwardPacket()
        q.addLast(intArrayOf(source, destination, timestamp))
        d.getOrPut(destination) { ArrayList() }.add(timestamp)
        return true
    }

    fun forwardPacket(): IntArray {
        if (q.isEmpty()) return IntArray(0)
        var packet = q.pollFirst()
        var s = packet[0]
        var dest = packet[1]
        var t = packet[2]
        vis.remove(f(s, dest, t))
        idx[dest] = idx.getOrDefault(dest, 0 + 1)
        return intArrayOf(s, dest, t)
    }

    fun getCount(destination: Int, startTime: Int, endTime: Int): Int {
        var ls = d[destination]
        if (ls == null) return 0
        var k = idx.getOrDefault(destination, 0)
        return lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime)
    }

    fun lowerBound(a: MutableList<Int>, from: Int, target: Int): Int {
        var lo = from
        var hi = a.size
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (a[mid] < target) lo = mid + 1
            else hi = mid
        }
        return lo
    }
}
