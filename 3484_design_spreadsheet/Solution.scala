// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet(_rows: Int) {
  private val cells = scala.collection.mutable.Map.empty[String, Int]

  def setCell(cell: String, value: Int): Unit = { cells(cell) = value }

  def resetCell(cell: String): Unit = { cells.remove(cell) }

  def getValue(formula0: String): Int = {
    var formula = formula0
    if (formula.nonEmpty && formula.charAt(0) == '=') formula = formula.substring(1)
    var sum = 0
    var start = 0
    while (start < formula.length) {
      val plus = formula.indexOf('+', start)
      val p = if (plus < 0) formula.substring(start) else formula.substring(start, plus)
      var isNum = p.nonEmpty && (Character.isDigit(p.charAt(0)) || (p.charAt(0) == '-' && p.length > 1))
      if (isNum) {
        var i = 1
        while (i < p.length) {
          if (!Character.isDigit(p.charAt(i))) { isNum = false; i = p.length }
          else i += 1
        }
      }
      if (isNum) sum += p.toInt
      else sum += cells.getOrElse(p, 0)
      if (plus < 0) return sum
      start = plus + 1
    }
    sum
  }
}
