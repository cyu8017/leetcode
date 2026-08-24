// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

class SQL(_names: Array[String], _columns: Array[Int]) {
  private val tables = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ArrayBuffer[List[String]]]
  private val nextID = scala.collection.mutable.Map.empty[String, Int]

  _names.foreach { name =>
    tables(name) = scala.collection.mutable.ArrayBuffer.empty[List[String]]
    nextID(name) = 1
  }

  def ins(name: String, row: List[String]): Boolean = {
    if (!tables.contains(name)) return false
    val id = nextID(name)
    nextID(name) = id + 1
    tables(name) += (id.toString :: row)
    true
  }

  def rmv(name: String, rowId: Int): Unit = {
    val rows = tables(name)
    var i = 0
    while (i < rows.length) {
      if (rows(i).head.toInt == rowId) {
        rows.remove(i)
        return
      }
      i += 1
    }
  }

  def sel(name: String, rowId: Int, columnId: Int): String = {
    tables(name).foreach { r =>
      if (r.head.toInt == rowId) {
        if (columnId < 1 || columnId >= r.length) return "<null>"
        return r(columnId)
      }
    }
    "<null>"
  }

  def exp(name: String): List[String] = {
    tables(name).map(_.mkString(",")).toList
  }
}
