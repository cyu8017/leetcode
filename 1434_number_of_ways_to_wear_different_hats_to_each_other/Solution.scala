import scala.collection.mutable
object Solution {
  def numberWays(hats: List[List[Int]]): Int = {
    val mod = 1000000007L; val people = hats.length
    val wearers = Array.fill(41)(mutable.ArrayBuffer.empty[Int])
    for ((choices, person) <- hats.zipWithIndex; hat <- choices) wearers(hat) += person
    var dp = Array.fill[Long](1 << people)(0); dp(0) = 1
    for (hat <- 1 to 40) {
      val next = dp.clone()
      for (mask <- dp.indices if dp(mask) != 0; person <- wearers(hat) if (mask & (1 << person)) == 0)
        next(mask | (1 << person)) = (next(mask | (1 << person)) + dp(mask)) % mod
      dp = next
    }
    dp.last.toInt
  }
}
