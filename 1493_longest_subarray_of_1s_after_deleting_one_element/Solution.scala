object Solution {
  def longestSubarray(nums: Array[Int]): Int = {
    var left = 0
    var zeros = 0
    var answer = 0
    for (right <- nums.indices) {
      if (nums(right) == 0) zeros += 1
      while (zeros > 1) {
        if (nums(left) == 0) zeros -= 1
        left += 1
      }
      answer = math.max(answer, right - left)
    }
    answer
  }
}
