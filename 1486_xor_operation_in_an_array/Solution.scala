object Solution {
  def xorOperation(n: Int, start: Int): Int = (0 until n).foldLeft(0)((answer, i) => answer ^ (start + 2 * i))
}
