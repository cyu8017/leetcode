// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot {
    private val w: Int
    private val h: Int
    private val peri: Int
    private var pos = 0
    private var moved = false

    constructor(width: Int, height: Int) {
        w = width
        h = height
        peri = 2 * (width + height) - 4
    }

    private fun getPosDir(): IntArray {
        var p = pos
        if (p == 0) {
            if (!moved) return intArrayOf(0, 0, 0)
            return intArrayOf(0, 0, 3)
        }
        if (p <= w - 1) return intArrayOf(p, 0, 0)
        p -= w - 1
        if (p <= h - 1) return intArrayOf(w - 1, p, 1)
        p -= h - 1
        if (p <= w - 1) return intArrayOf(w - 1 - p, h - 1, 2)
        p -= w - 1
        return intArrayOf(0, h - 1 - p, 3)
    }

    fun step(num: Int) {
        moved = true
        pos = (pos + num) % peri
    }

    fun getPos(): IntArray {
        val pd = getPosDir()
        return intArrayOf(pd[0], pd[1])
    }

    fun getDir(): String {
        val names = arrayOf("East", "North", "West", "South")
        return names[getPosDir()[2]]
    }
}
