// LeetCode 0432 - All O`one` Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

import scala.collection.mutable

class AllOne {
  private class CountNode(val count: Int) {
    val keys: mutable.Set[String] = mutable.Set.empty
    var prev: CountNode = null
    var next: CountNode = null
  }

  private val head = new CountNode(0)
  private val tail = new CountNode(0)
  private val keyNodes = mutable.Map.empty[String, CountNode]

  head.next = tail
  tail.prev = head

  def inc(key: String): Unit = {
    if (keyNodes.contains(key)) {
      val bucket = keyNodes(key)
      bucket.keys.remove(key)
      val nextBucket = ensureCountNode(bucket.count + 1, bucket)
      nextBucket.keys.add(key)
      keyNodes(key) = nextBucket
      if (bucket.keys.isEmpty) {
        remove(bucket)
      }
      return
    }

    val bucket = ensureCountNode(1, head)
    bucket.keys.add(key)
    keyNodes(key) = bucket
  }

  def dec(key: String): Unit = {
    val bucket = keyNodes(key)
    bucket.keys.remove(key)
    if (bucket.count == 1) {
      keyNodes.remove(key)
    } else {
      val prevBucket = ensureCountNode(bucket.count - 1, head)
      prevBucket.keys.add(key)
      keyNodes(key) = prevBucket
    }
    if (bucket.keys.isEmpty) {
      remove(bucket)
    }
  }

  def getMaxKey(): String = {
    val bucket = tail.prev
    if (bucket eq head) {
      return ""
    }
    bucket.keys.head
  }

  def getMinKey(): String = {
    val bucket = head.next
    if (bucket eq tail) {
      return ""
    }
    bucket.keys.head
  }

  private def insertAfter(anchor: CountNode, node: CountNode): Unit = {
    node.prev = anchor
    node.next = anchor.next
    anchor.next.prev = node
    anchor.next = node
  }

  private def remove(node: CountNode): Unit = {
    node.prev.next = node.next
    node.next.prev = node.prev
  }

  private def ensureCountNode(count: Int, after: CountNode): CountNode = {
    var current = after.next
    while (current ne tail) {
      if (current.count >= count) {
        if (current.count == count) {
          return current
        }
        val bucket = new CountNode(count)
        insertAfter(current.prev, bucket)
        return bucket
      }
      current = current.next
    }
    val bucket = new CountNode(count)
    insertAfter(tail.prev, bucket)
    bucket
  }
}
