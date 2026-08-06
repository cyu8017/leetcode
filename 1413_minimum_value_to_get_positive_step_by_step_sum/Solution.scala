object Solution {
  def minStartValue(nums: Array[Int]): Int = { var sum=0; var low=0; nums.foreach(x => {sum += x; low=math.min(low,sum)}); 1-low }
}
