// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

import scala.collection.mutable

class Excel(height: Int, width: Char) {
  private val values = Array.ofDim[Int](height + 1, width - 'A' + 1)
  private val formulas = mutable.Map.empty[Long, mutable.ArrayBuffer[Array[Int]]]

  def set(row: Int, column: Char, `val`: Int): Unit = {
    val col = column - 'A'
    formulas.remove(key(row, col))
    values(row)(col) = `val`
  }

  def get(row: Int, column: Char): Int = eval(row, column - 'A')

  def sum(row: Int, column: Char, numbers: Array[String]): Int = {
    val col = column - 'A'
    val cells = mutable.ArrayBuffer.empty[Array[Int]]
    numbers.foreach { token =>
      val colon = token.indexOf(':')
      if (colon >= 0) {
        val p1 = parse(token.substring(0, colon))
        val p2 = parse(token.substring(colon + 1))
        var r = p1(0)
        while (r <= p2(0)) {
          var c = p1(1)
          while (c <= p2(1)) {
            cells += Array(r, c)
            c += 1
          }
          r += 1
        }
      } else {
        cells += parse(token)
      }
    }
    formulas(key(row, col)) = cells
    eval(row, col)
  }

  private def parse(cell: String): Array[Int] =
    Array(cell.substring(1).toInt, cell.charAt(0) - 'A')

  private def eval(row: Int, col: Int): Int = {
    formulas.get(key(row, col)) match {
      case Some(formula) =>
        var total = 0
        formula.foreach(cell => total += eval(cell(0), cell(1)))
        total
      case None => values(row)(col)
    }
  }

  private def key(row: Int, col: Int): Long =
    (row.toLong << 32) | (col.toLong & 0xffffffffL)
}
