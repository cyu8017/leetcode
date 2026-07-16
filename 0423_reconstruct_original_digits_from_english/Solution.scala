// LeetCode 0423 - Reconstruct Original Digits from English
// https://leetcode.com/problems/reconstruct-original-digits-from-english/

object Solution {
  def originalDigits(s: String): String = {
    val counts = Array.fill(26)(0)
    for (ch <- s) {
      counts(ch - 'a') += 1
    }

    val digitCounts = Array.fill(10)(0)
    digitCounts(0) = counts('z' - 'a')
    digitCounts(2) = counts('w' - 'a')
    digitCounts(4) = counts('u' - 'a')
    digitCounts(6) = counts('x' - 'a')
    digitCounts(8) = counts('g' - 'a')
    digitCounts(1) = counts('o' - 'a') - digitCounts(0) - digitCounts(2) - digitCounts(4)
    digitCounts(3) = counts('h' - 'a') - digitCounts(8)
    digitCounts(5) = counts('f' - 'a') - digitCounts(4)
    digitCounts(7) = counts('s' - 'a') - digitCounts(6)
    digitCounts(9) = counts('i' - 'a') - digitCounts(5) - digitCounts(6) - digitCounts(8)

    val result = new StringBuilder
    for (digit <- 0 until 10) {
      result.append(digit.toString * digitCounts(digit))
    }
    result.toString()
  }
}
