// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

class TextEditor {
    private val left = ArrayList<Char>()
    private val right = ArrayList<Char>()

    private fun suffix(): String {
        val start = maxOf(0, left.size - 10)
        val sb = StringBuilder()
        for (i in start until left.size) sb.append(left[i])
        return sb.toString()
    }

    constructor() {}

    fun addText(text: String) {
        for (c in text) left.add(c)
    }

    fun deleteText(k0: Int): Int {
        var k = k0
        var deleted = 0
        while (k > 0 && left.isNotEmpty()) {
            left.removeAt(left.size - 1)
            k--
            deleted++
        }
        return deleted
    }

    fun cursorLeft(k0: Int): String {
        var k = k0
        while (k > 0 && left.isNotEmpty()) {
            right.add(left.removeAt(left.size - 1))
            k--
        }
        return suffix()
    }

    fun cursorRight(k0: Int): String {
        var k = k0
        while (k > 0 && right.isNotEmpty()) {
            left.add(right.removeAt(right.size - 1))
            k--
        }
        return suffix()
    }
}
