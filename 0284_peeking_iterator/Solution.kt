// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

interface Iterator {
    fun next(): Int
    fun hasNext(): Boolean
}

class PeekingIterator(private val iterator: Iterator) {
    private var peeked: Int? = null
    private var hasPeeked = false

    fun peek(): Int {
        if (!hasPeeked) {
            peeked = iterator.next()
            hasPeeked = true
        }
        return peeked!!
    }

    fun next(): Int {
        if (hasPeeked) {
            val result = peeked!!
            peeked = null
            hasPeeked = false
            return result
        }
        return iterator.next()
    }

    fun hasNext(): Boolean {
        return hasPeeked || iterator.hasNext()
    }
}
