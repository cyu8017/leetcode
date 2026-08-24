// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

class MyHashSet() {
  private val data = scala.collection.mutable.HashSet.empty[Int]

  def add(key: Int): Unit = { data += key }

  def remove(key: Int): Unit = { data -= key }

  def contains(key: Int): Boolean = data.contains(key)
}
