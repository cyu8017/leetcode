class Solution {
    fun read(file: String, queries: IntArray): IntArray {
        var index = 0
        return IntArray(queries.size) { i ->
            val count = minOf(queries[i], file.length - index)
            index += count
            count
        }
    }
}