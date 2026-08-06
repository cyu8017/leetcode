object Solution {
  def countElements(arr: Array[Int]): Int = {
    val values = arr.toSet
    arr.count(x => values.contains(x + 1))
  }
}
