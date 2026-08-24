// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

object Solution {
  def compactObject(obj: Array[Int]): Array[Int] = {
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < obj.length) {
      if (obj(i) != 0) out += obj(i)
      i += 1
    }
    out.toArray
  }
}
