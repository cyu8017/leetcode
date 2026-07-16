// LeetCode 0146 - LRU Cache
// https://leetcode.com/problems/lru-cache/

import scala.collection.mutable
class LRUCache(capacity: Int) {
  private class Node(val key: Int, var value: Int) { var prev: Node = null; var next: Node = null }
  private val cache = mutable.Map[Int, Node]()
  private val head = new Node(0, 0)
  private val tail = new Node(0, 0)
  head.next = tail
  tail.prev = head
  def get(key: Int): Int = cache.get(key) match {
    case Some(node) => moveToFront(node); node.value
    case None => -1
  }
  def put(key: Int, value: Int): Unit = cache.get(key) match {
    case Some(node) => node.value = value; moveToFront(node)
    case None =>
      if (cache.size == capacity) { val lru = tail.prev; remove(lru); cache -= lru.key }
      val node = new Node(key, value); cache += key -> node; addFront(node)
  }
  private def moveToFront(node: Node): Unit = { remove(node); addFront(node) }
  private def remove(node: Node): Unit = { node.prev.next = node.next; node.next.prev = node.prev }
  private def addFront(node: Node): Unit = { node.prev = head; node.next = head.next; head.next.prev = node; head.next = node }
}