// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

class Encrypter(_keys: Array[Char], _values: Array[String], _dictionary: Array[String]) {
  private val enc = scala.collection.mutable.HashMap.empty[Char, String]
  private val cnt = scala.collection.mutable.HashMap.empty[String, Int]
  {
    var i = 0
    while (i < _keys.length) {
      enc(_keys(i)) = _values(i)
      i += 1
    }
    for (w <- _dictionary) {
      val e = encrypt(w)
      cnt(e) = cnt.getOrElse(e, 0) + 1
    }
  }

  def encrypt(word1: String): String = {
    val b = new StringBuilder
    var i = 0
    while (i < word1.length) {
      val c = word1.charAt(i)
      if (!enc.contains(c)) return ""
      b.append(enc(c))
      i += 1
    }
    b.toString
  }

  def decrypt(word2: String): Int = cnt.getOrElse(word2, 0)
}
