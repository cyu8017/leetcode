class SubrectangleQueries(rectangle: Array[Array[Int]]) {
  def updateSubrectangle(row1: Int, col1: Int, row2: Int, col2: Int, newValue: Int): Unit = {
    for (row <- row1 to row2; col <- col1 to col2) rectangle(row)(col) = newValue
  }

  def getValue(row: Int, col: Int): Int = rectangle(row)(col)
}
