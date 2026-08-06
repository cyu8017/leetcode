object Solution {
  def canBeEqual(target: Array[Int], arr: Array[Int]): Boolean = target.sorted.sameElements(arr.sorted)
}
