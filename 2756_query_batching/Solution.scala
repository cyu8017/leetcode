// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/

class QueryBatcher(queryMultiple: Array[Int] => Array[Int], t: Int) {
  private val pending = scala.collection.mutable.ArrayBuffer.empty[Int]
  private val resolvers = scala.collection.mutable.ArrayBuffer.empty[Int => Unit]

  def addQuery(query: Int, resolve: Int => Unit): Unit = {
    pending += query
    resolvers += resolve
  }
}
