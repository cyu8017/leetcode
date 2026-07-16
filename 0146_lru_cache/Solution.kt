// LeetCode 0146 - LRU Cache
// https://leetcode.com/problems/lru-cache/

class LRUCache(private val capacity: Int) {
    private class Node(val key: Int, var value: Int) { var prev: Node? = null; var next: Node? = null }
    private val cache = HashMap<Int, Node>()
    private val head = Node(0, 0)
    private val tail = Node(0, 0)
    init { head.next = tail; tail.prev = head }
    fun get(key: Int): Int {
        val node = cache[key] ?: return -1
        moveToFront(node)
        return node.value
    }
    fun put(key: Int, value: Int) {
        val existing = cache[key]
        if (existing != null) { existing.value = value; moveToFront(existing); return }
        if (cache.size == capacity) { val lru = tail.prev!!; remove(lru); cache.remove(lru.key) }
        val node = Node(key, value); cache[key] = node; addFront(node)
    }
    private fun moveToFront(node: Node) { remove(node); addFront(node) }
    private fun remove(node: Node) { node.prev!!.next = node.next; node.next!!.prev = node.prev }
    private fun addFront(node: Node) { node.prev = head; node.next = head.next; head.next!!.prev = node; head.next = node }
}