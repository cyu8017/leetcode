// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/
// JS QueryBatcher design stand-in.

class QueryBatcher(
    private val queryMultiple: (IntArray) -> IntArray,
    private val t: Int
) {
    private val pending = ArrayList<Int>()
    private val resolvers = ArrayList<(Int) -> Unit>()

    fun addQuery(query: Int, resolve: (Int) -> Unit) {
        pending.add(query)
        resolvers.add(resolve)
    }
}
