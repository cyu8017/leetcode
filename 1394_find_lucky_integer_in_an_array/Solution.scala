object Solution {
  def findLucky(arr: Array[Int]): Int = { val c = arr.groupMapReduce(identity)(_ => 1)(_ + _); c.collect { case (x, n) if x == n => x }.foldLeft(-1)(math.max) }
}
