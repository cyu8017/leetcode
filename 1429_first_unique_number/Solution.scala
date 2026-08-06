import scala.collection.mutable
class FirstUnique(nums: Array[Int]) {
  private val counts = mutable.Map.empty[Int, Int]
  private val unique = mutable.LinkedHashSet.empty[Int]
  nums.foreach(add)
  def showFirstUnique(): Int = unique.headOption.getOrElse(-1)
  def add(value: Int): Unit = {
    counts(value) = counts.getOrElse(value, 0) + 1
    if (counts(value) == 1) unique += value else unique -= value
  }
}
