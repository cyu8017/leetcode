// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

import kotlin.random.Random

class Solution(n: Int, blacklist: IntArray) {
    private val size = n - blacklist.size
    private val mapping = HashMap<Int, Int>()
    private val rand = Random.Default

    init {
        val black = HashSet<Int>()
        for (b in blacklist) black.add(b)
        var white = size
        for (b in blacklist) {
            if (b < size) {
                while (black.contains(white)) white++
                mapping[b] = white++
            }
        }
    }

    fun pick(): Int {
        val index = rand.nextInt(size)
        return mapping.getOrDefault(index, index)
    }
}
