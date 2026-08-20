// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

class TrafficLight() {
  private var greenRoad = 1
  private val lock = new Object

  def carArrived(carId: Int, roadId: Int, direction: Int, turnGreen: Runnable, crossCar: Runnable): Unit = {
    lock.synchronized {
      if (roadId != greenRoad) {
        turnGreen.run()
        greenRoad = roadId
      }
      crossCar.run()
    }
  }
}
