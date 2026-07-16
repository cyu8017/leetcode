object Solution {
  def hammingWeight(n: Int): Int = {
    var value = n
    var count = 0
    while (value != 0) {
      value &= value - 1
      count += 1
    }
    count
  }
}
