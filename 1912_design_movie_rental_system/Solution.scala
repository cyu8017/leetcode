// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer

class MovieRentingSystem(_n: Int, entries: Array[Array[Int]]) {
  private val price = mutable.Map.empty[(Int, Int), Int]
  private val available = mutable.Map.empty[Int, ArrayBuffer[(Int, Int)]]
  private val rented = ArrayBuffer.empty[(Int, Int, Int)]

  for (e <- entries) {
    val shop = e(0)
    val movie = e(1)
    val p = e(2)
    price((shop, movie)) = p
    val buf = available.getOrElseUpdate(movie, ArrayBuffer.empty[(Int, Int)])
    val idx = buf.indexWhere(t => t._1 > p || (t._1 == p && t._2 > shop))
    if (idx < 0) buf += ((p, shop)) else buf.insert(idx, (p, shop))
  }

  def search(movie: Int): List[Int] =
    available.getOrElse(movie, ArrayBuffer.empty[(Int, Int)]).take(5).map(_._2).toList

  def rent(shop: Int, movie: Int): Unit = {
    val p = price((shop, movie))
    val avail = available(movie)
    val ai = avail.indexOf((p, shop))
    avail.remove(ai)
    val ri = rented.indexWhere(t => t._1 > p || (t._1 == p && t._2 > shop) || (t._1 == p && t._2 == shop && t._3 > movie))
    if (ri < 0) rented += ((p, shop, movie)) else rented.insert(ri, (p, shop, movie))
  }

  def drop(shop: Int, movie: Int): Unit = {
    val p = price((shop, movie))
    val ri = rented.indexOf((p, shop, movie))
    rented.remove(ri)
    val avail = available.getOrElseUpdate(movie, ArrayBuffer.empty[(Int, Int)])
    val ai = avail.indexWhere(t => t._1 > p || (t._1 == p && t._2 > shop))
    if (ai < 0) avail += ((p, shop)) else avail.insert(ai, (p, shop))
  }

  def report(): List[List[Int]] =
    rented.take(5).map(t => List(t._2, t._3)).toList
}
