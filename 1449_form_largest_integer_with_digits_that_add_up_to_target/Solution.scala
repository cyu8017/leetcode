object Solution {
  def largestNumber(cost: Array[Int], target: Int): String = {
    val dp = Array.fill[Option[String]](target + 1)(None); dp(0) = Some("")
    for (total <- 1 to target; digit <- 1 to 9 if total >= cost(digit - 1) && dp(total - cost(digit - 1)).nonEmpty) {
      val candidate = digit.toString + dp(total - cost(digit - 1)).get
      if (dp(total).forall(x => candidate.length > x.length || (candidate.length == x.length && candidate > x))) dp(total) = Some(candidate)
    }
    dp(target).getOrElse("0")
  }
}
