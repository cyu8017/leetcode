// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

class EventEmitter {
    private val handlers = HashMap<String, MutableList<(IntArray) -> Unit>>()

    fun subscribe(eventName: String, callback: (IntArray) -> Unit): () -> Unit {
        handlers.getOrPut(eventName) { ArrayList() }.add(callback)
        var idx = handlers[eventName]!!.size - 1
        return {
            val v = handlers[eventName]
            if (v != null && idx >= 0 && idx < v.size) {
                v.removeAt(idx)
                idx = -1
            }
        }
    }

    fun emit(eventName: String, args: IntArray): IntArray {
        val res = ArrayList<Int>()
        val list = handlers[eventName]
        if (list != null) {
            for (cb in ArrayList(list)) {
                cb(args)
                res.add(0)
            }
        }
        return res.toIntArray()
    }
}

class Solution {
    fun createEmitter(): EventEmitter = EventEmitter()
}
