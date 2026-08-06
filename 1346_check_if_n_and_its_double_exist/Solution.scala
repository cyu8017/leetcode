import scala.collection.mutable

object Solution {
  def checkIfExist(arr: Array[Int]): Boolean = {
    val seen = mutable.Set.empty[Int]
    arr.exists(value => { val found = seen.contains(2 * value) || (value % 2 == 0 && seen.contains(value / 2)); seen += value; found })
  }
}
