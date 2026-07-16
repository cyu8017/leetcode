// LeetCode 0443 - String Compression
// https://leetcode.com/problems/string-compression/

object Solution {
  def compress(chars: Array[Char]): Int = {
    var write = 0
    var read = 0
    while (read < chars.length) {
      val char = chars(read)
      var count = 0
      while (read < chars.length && chars(read) == char) {
        read += 1
        count += 1
      }
      chars(write) = char
      write += 1
      if (count > 1) {
        for (digit <- count.toString) {
          chars(write) = digit
          write += 1
        }
      }
    }
    write
  }
}
