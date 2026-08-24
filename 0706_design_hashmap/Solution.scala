// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

class MyHashMap() {
  private val data = scala.collection.mutable.HashMap.empty[Int, Int]

  def put(key: Int, value: Int): Unit = { data(key) = value }

  def get(key: Int): Int = data.getOrElse(key, -1)

  def remove(key: Int): Unit = { data.remove(key) }
}
