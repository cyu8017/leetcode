trait BinaryMatrix {
  def get(row: Int, col: Int): Int
  def dimensions(): List[Int]
}
object Solution {
  def leftMostColumnWithOne(binaryMatrix: BinaryMatrix): Int = {
    val size = binaryMatrix.dimensions()
    var row = 0; var col = size(1) - 1; var answer = -1
    while (row < size(0) && col >= 0) {
      if (binaryMatrix.get(row, col) == 1) { answer = col; col -= 1 }
      else row += 1
    }
    answer
  }
}
