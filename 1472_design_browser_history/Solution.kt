// LeetCode 1472 - Design Browser History
// https://leetcode.com/problems/design-browser-history/

class BrowserHistory(homepage: String) {
    private val history = mutableListOf(homepage)
    private var index = 0

    fun visit(url: String) {
        while (history.size > index + 1) history.removeAt(history.lastIndex)
        history.add(url)
        index++
    }

    fun back(steps: Int): String {
        index = maxOf(0, index - steps)
        return history[index]
    }

    fun forward(steps: Int): String {
        index = minOf(history.size - 1, index + steps)
        return history[index]
    }
}
