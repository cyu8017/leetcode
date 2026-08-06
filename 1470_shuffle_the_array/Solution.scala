object Solution {
  def shuffle(nums: Array[Int], n: Int): Array[Int] = {
    val answer = new Array[Int](2 * n)
    for (i <- 0 until n) {
      answer(2 * i) = nums(i)
      answer(2 * i + 1) = nums(i + n)
    }
    answer
  }
}
