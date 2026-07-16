// LeetCode 0432 - All O`one Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

class AllOne {
    private class Bucket(val count: Int = 0) {
        val keys = HashSet<String>()
        var prev: Bucket? = null
        var next: Bucket? = null
    }

    private val head = Bucket()
    private val tail = Bucket()
    private val keyNodes = HashMap<String, Bucket>()

    init {
        head.next = tail
        tail.prev = head
    }

    private fun insertAfter(anchor: Bucket, node: Bucket) {
        node.prev = anchor
        node.next = anchor.next
        anchor.next!!.prev = node
        anchor.next = node
    }

    private fun remove(node: Bucket) {
        node.prev!!.next = node.next
        node.next!!.prev = node.prev
    }

    private fun ensureCountNode(count: Int, after: Bucket): Bucket {
        var current = after.next
        while (current !== tail && current!!.count < count) {
            current = current.next
        }
        if (current !== tail && current!!.count == count) {
            return current
        }
        val bucket = Bucket(count)
        insertAfter(current!!.prev!!, bucket)
        return bucket
    }

    fun inc(key: String) {
        if (key in keyNodes) {
            val bucket = keyNodes[key]!!
            bucket.keys.remove(key)
            val nextBucket = ensureCountNode(bucket.count + 1, bucket)
            nextBucket.keys.add(key)
            keyNodes[key] = nextBucket
            if (bucket.keys.isEmpty()) {
                remove(bucket)
            }
            return
        }

        val bucket = ensureCountNode(1, head)
        bucket.keys.add(key)
        keyNodes[key] = bucket
    }

    fun dec(key: String) {
        val bucket = keyNodes[key]!!
        bucket.keys.remove(key)
        if (bucket.count == 1) {
            keyNodes.remove(key)
        } else {
            val prevBucket = ensureCountNode(bucket.count - 1, head)
            prevBucket.keys.add(key)
            keyNodes[key] = prevBucket
        }
        if (bucket.keys.isEmpty()) {
            remove(bucket)
        }
    }

    fun getMaxKey(): String {
        val bucket = tail.prev!!
        if (bucket === head) {
            return ""
        }
        return bucket.keys.first()
    }

    fun getMinKey(): String {
        val bucket = head.next!!
        if (bucket === tail) {
            return ""
        }
        return bucket.keys.first()
    }
}
