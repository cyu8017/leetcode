// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/


class Solution {
    fun nearestPalindromic(n: String): String {
        val length = n.length
        val number = n.toLong()
        val candidates = ArrayList<Long>()
        candidates.add(pow10(length - 1) - 1)
        candidates.add(pow10(length) + 1)
        val prefix = n.substring(0, (length + 1) / 2).toLong()
        for (half in prefix - 1..prefix + 1) {
            candidates.add(makePalindrome(half, length))
        }
        var best = -1L
        var bestDiff = Long.MAX_VALUE
        for (candidate in candidates) {
            if (candidate == number) continue
            val diff = kotlin.math.abs(candidate - number)
            if (diff < bestDiff || (diff == bestDiff && candidate < best)) {
                best = candidate
                bestDiff = diff
            }
        }
        return best.toString()
    }

    private fun makePalindrome(half: Long, length: Int): Long {
        val text = half.toString()
        val pal = StringBuilder(text)
        if (length % 2 == 0) {
            for (i in text.length - 1 downTo 0) pal.append(text[i])
        } else {
            for (i in text.length - 2 downTo 0) pal.append(text[i])
        }
        return pal.toString().toLong()
    }

    private fun pow10(exp: Int): Long {
        var value = 1L
        repeat(exp) { value *= 10 }
        return value
    }
}
