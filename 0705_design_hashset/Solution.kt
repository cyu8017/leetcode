// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

class MyHashSet {
    private val data = HashSet<Int>()

    fun add(key: Int) { data.add(key) }

    fun remove(key: Int) { data.remove(key) }

    fun contains(key: Int): Boolean = data.contains(key)
}
