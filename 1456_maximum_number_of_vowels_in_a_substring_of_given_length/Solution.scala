object Solution {
  def maxVowels(s: String, k: Int): Int = {
    def isVowel(c: Char): Boolean = "aeiou".contains(c)
    var current = s.take(k).count(isVowel); var answer = current
    for (i <- k until s.length) { if (isVowel(s(i))) current += 1; if (isVowel(s(i - k))) current -= 1; answer = answer.max(current) }
    answer
  }
}
