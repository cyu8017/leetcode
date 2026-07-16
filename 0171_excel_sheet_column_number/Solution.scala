class Solution {
  def titleToNumber(columnTitle: String): Int = {
    columnTitle.foldLeft(0)((result, ch) => result * 26 + ch - 'A' + 1)
  }
}
