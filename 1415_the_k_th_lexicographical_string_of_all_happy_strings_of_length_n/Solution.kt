// LeetCode 1415 - The k-th Lexicographical String of All Happy Strings of Length n
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

class Solution {
    fun getHappyString(n: Int, k: Int): String {
        val answer = ArrayList<String>()
        fun build(path: StringBuilder) {
            if (path.length == n) {
                answer.add(path.toString())
                return
            }
            for (char in "abc") {
                if (path.isEmpty() || path.last() != char) {
                    path.append(char)
                    build(path)
                    path.deleteCharAt(path.length - 1)
                }
            }
        }
        build(StringBuilder())
        return if (k <= answer.size) answer[k - 1] else ""
    }
}
