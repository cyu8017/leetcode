object Solution {
  def closestDivisors(num: Int): Array[Int] = {
    Seq(num + 1, num + 2).map { x =>
      var a = math.sqrt(x).toInt
      while (x % a != 0) a -= 1
      Array(a, x / a)
    }.minBy(pair => pair(1) - pair(0))
  }
}
