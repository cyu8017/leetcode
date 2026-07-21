// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

class SeatManager(_n: Int) {
  private val available = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
  for (i <- 1 to _n) available.enqueue(i)

  def reserve(): Int = available.dequeue()

  def unreserve(seatNumber: Int): Unit = available.enqueue(seatNumber)
}
