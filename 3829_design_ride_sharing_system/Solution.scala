// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design_ride_sharing_system/

class RideSharingSystem() {
  private var t = 0
  private val riders = scala.collection.mutable.TreeMap.empty[Int, Int]
  private val drivers = scala.collection.mutable.TreeMap.empty[Int, Int]
  private val d = scala.collection.mutable.Map.empty[Int, Int]

  def addRider(riderId: Int): Unit = {
    d(riderId) = t
    riders(t) = riderId
    t += 1
  }

  def addDriver(driverId: Int): Unit = {
    drivers(t) = driverId
    t += 1
  }

  def matchDriverWithRider(): Array[Int] = {
    if (riders.isEmpty || drivers.isEmpty) return Array(-1, -1)
    val dKey = drivers.firstKey
    val rKey = riders.firstKey
    val driverId = drivers(dKey)
    val riderId = riders(rKey)
    drivers.remove(dKey)
    riders.remove(rKey)
    Array(driverId, riderId)
  }

  def cancelRider(riderId: Int): Unit = {
    if (!d.contains(riderId)) return
    riders.remove(d(riderId))
  }
}
