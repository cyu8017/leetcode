// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

import java.util.TreeSet

class MovieRentingSystem(n: Int, entries: Array<IntArray>) {
    private val price = HashMap<Long, Int>()
    private val available = HashMap<Int, TreeSet<LongArray>>()
    private val rented = TreeSet<LongArray> { a, b ->
        when {
            a[0] != b[0] -> a[0].compareTo(b[0])
            a[1] != b[1] -> a[1].compareTo(b[1])
            else -> a[2].compareTo(b[2])
        }
    }
    private val availCmp = Comparator<LongArray> { a, b ->
        when {
            a[0] != b[0] -> a[0].compareTo(b[0])
            else -> a[1].compareTo(b[1])
        }
    }

    init {
        for (e in entries) {
            val shop = e[0]
            val movie = e[1]
            val p = e[2]
            price[key(shop, movie)] = p
            available.getOrPut(movie) { TreeSet(availCmp) }.add(longArrayOf(p.toLong(), shop.toLong()))
        }
    }

    private fun key(shop: Int, movie: Int): Long = (shop.toLong() shl 20) or movie.toLong()

    fun search(movie: Int): List<Int> {
        val set = available[movie] ?: return emptyList()
        return set.asSequence().take(5).map { it[1].toInt() }.toList()
    }

    fun rent(shop: Int, movie: Int) {
        val p = price[key(shop, movie)]!!
        available[movie]!!.remove(longArrayOf(p.toLong(), shop.toLong()))
        rented.add(longArrayOf(p.toLong(), shop.toLong(), movie.toLong()))
    }

    fun drop(shop: Int, movie: Int) {
        val p = price[key(shop, movie)]!!
        rented.remove(longArrayOf(p.toLong(), shop.toLong(), movie.toLong()))
        available.getOrPut(movie) { TreeSet(availCmp) }.add(longArrayOf(p.toLong(), shop.toLong()))
    }

    fun report(): List<List<Int>> =
        rented.asSequence().take(5).map { listOf(it[1].toInt(), it[2].toInt()) }.toList()
}
