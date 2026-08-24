// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

class MyHashMap {
    private val data = HashMap<Int, Int>()

    fun put(key: Int, value: Int) { data[key] = value }

    fun get(key: Int): Int = data.getOrDefault(key, -1)

    fun remove(key: Int) { data.remove(key) }
}
