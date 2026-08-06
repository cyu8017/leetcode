object Solution {
  def smallerNumbersThanCurrent(nums: Array[Int]): Array[Int] = {
    val sorted = nums.sorted
    nums.map(sorted.indexOf)
  }
}
