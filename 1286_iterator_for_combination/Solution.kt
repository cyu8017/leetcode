// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator(characters: String, combinationLength: Int) {
    private val items: Array<String>
    private var index = 0

    init {
        val built = mutableListOf<String>()
        val path = CharArray(combinationLength)
        fun build(start: Int, depth: Int) {
            if (depth == combinationLength) {
                built.add(String(path))
                return
            }
            for (i in start until characters.length) {
                path[depth] = characters[i]
                build(i + 1, depth + 1)
            }
        }
        build(0, 0)
        items = built.toTypedArray()
    }

    fun next(): String = items[index++]

    fun hasNext(): Boolean = index < items.size
}
