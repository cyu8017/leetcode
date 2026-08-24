// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

class RideSharingSystem {
    private var t = 0
    private val riders = java.util.TreeMap<Int, Int>()
    private val drivers = java.util.TreeMap<Int, Int>()
    private val d = HashMap<Int, Int>()

    fun addRider(riderId: Int) {
        d[riderId] = t
        riders[t] = riderId
        t++
    }

    fun addDriver(driverId: Int) {
        drivers[t] = driverId
        t++
    }

    fun matchDriverWithRider(): IntArray {
        if (riders.isEmpty() || drivers.isEmpty()) return intArrayOf(-1, -1)
        val dKey = drivers.firstKey()
        val rKey = riders.firstKey()
        val driverId = drivers[dKey]!!
        val riderId = riders[rKey]!!
        drivers.remove(dKey)
        riders.remove(rKey)
        return intArrayOf(driverId, riderId)
    }

    fun cancelRider(riderId: Int) {
        if (!d.containsKey(riderId)) return
        riders.remove(d[riderId])
    }
}
