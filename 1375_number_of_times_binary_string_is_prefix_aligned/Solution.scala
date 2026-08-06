object Solution {
  def numTimesAllBlue(flips: Array[Int]): Int = {
    var maximum = 0; var answer = 0
    flips.indices.foreach(i => { maximum = math.max(maximum, flips(i)); if (maximum == i + 1) answer += 1 })
    answer
  }
}
