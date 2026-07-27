// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream(n: Int) {
    private val a = arrayOfNulls<String>(n + 1)
    private var p = 1

    fun insert(idKey: Int, value: String): List<String> {
        a[idKey] = value
        val out = mutableListOf<String>()
        while (p < a.size && a[p] != null) {
            out.add(a[p]!!)
            p++
        }
        return out
    }
}
