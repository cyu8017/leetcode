// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

import java.util.TreeSet

class FoodRatings(foods: Array<String>, cuisines: Array<String>, ratings: IntArray) {
    private val cuisineOf = HashMap<String, String>()
    private val ratingOf = HashMap<String, Int>()
    private val heaps = HashMap<String, TreeSet<String>>()

    private val cmp = Comparator<String> { a, b ->
        val ra = ratingOf[a]!!
        val rb = ratingOf[b]!!
        if (ra != rb) rb.compareTo(ra) else a.compareTo(b)
    }

    init {
        for (i in foods.indices) {
            cuisineOf[foods[i]] = cuisines[i]
            ratingOf[foods[i]] = ratings[i]
            heaps.getOrPut(cuisines[i]) { TreeSet(cmp) }.add(foods[i])
        }
    }

    fun changeRating(food: String, newRating: Int) {
        val cuisine = cuisineOf[food]!!
        val set = heaps[cuisine]!!
        set.remove(food)
        ratingOf[food] = newRating
        set.add(food)
    }

    fun highestRated(cuisine: String): String = heaps[cuisine]!!.first()
}
