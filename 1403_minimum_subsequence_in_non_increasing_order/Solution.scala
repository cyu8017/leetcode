object Solution {
  def minSubsequence(nums: Array[Int]): List[Int] = { val total=nums.sum; var sum=0; val out=scala.collection.mutable.ListBuffer[Int](); nums.sorted(Ordering.Int.reverse).foreach(x => if(sum <= total-sum) { out += x; sum += x }); out.toList }
}
