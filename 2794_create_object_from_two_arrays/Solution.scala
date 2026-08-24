// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/

object Solution {
  def createObject(keysArr: Array[String], valuesArr: Array[Int]): scala.collection.mutable.Map[String, Int] = {
    val output = scala.collection.mutable.LinkedHashMap.empty[String, Int]
    val n = math.min(keysArr.length, valuesArr.length)
    var i = 0
    while (i < n) {
      if (!output.contains(keysArr(i))) output(keysArr(i)) = valuesArr(i)
      i += 1
    }
    output
  }
}
