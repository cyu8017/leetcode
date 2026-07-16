// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

class Codec {
  def encode(strs: List[String]): String =
    strs.map(text => s"${text.length}#$text").mkString

  def decode(encoded: String): List[String] = {
    val result = scala.collection.mutable.ListBuffer.empty[String]
    var index = 0
    while (index < encoded.length) {
      val delimiter = encoded.indexOf('#', index)
      val length = encoded.substring(index, delimiter).toInt
      val start = delimiter + 1
      result += encoded.substring(start, start + length)
      index = start + length
    }
    result.toList
  }
}
