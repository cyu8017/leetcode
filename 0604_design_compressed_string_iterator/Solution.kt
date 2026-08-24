// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/


class StringIterator(compressedString: String) {
    private val chars = ArrayList<Char>()
    private val counts = ArrayList<Int>()
    private var index = 0

    init {
        var i = 0
        val s = compressedString
        while (i < s.length) {
            val ch = s[i++]
            var count = 0
            while (i < s.length && s[i].isDigit()) {
                count = count * 10 + (s[i] - '0')
                i++
            }
            chars.add(ch)
            counts.add(count)
        }
    }

    fun next(): Char {
        if (!hasNext()) return ' '
        val ch = chars[index]
        counts[index] = counts[index] - 1
        if (counts[index] == 0) index++
        return ch
    }

    fun hasNext(): Boolean = index < chars.size
}
