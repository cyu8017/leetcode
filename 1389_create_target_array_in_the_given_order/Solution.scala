object Solution {
  def createTargetArray(nums: Array[Int], index: Array[Int]): Array[Int] = { val out = scala.collection.mutable.ArrayBuffer[Int](); nums.indices.foreach(i => out.insert(index(i), nums(i))); out.toArray }
}
