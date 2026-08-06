object Solution {
  def countLargestGroup(n: Int): Int = { val c = (1 to n).groupMapReduce(x => x.toString.map(_ - '0').sum)(_ => 1)(_ + _).values; val mx = c.max; c.count(_ == mx) }
}
