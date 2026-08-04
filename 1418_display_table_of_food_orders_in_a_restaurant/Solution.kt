// LeetCode 1418 - Display Table of Food Orders in a Restaurant
// https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

class Solution {
    fun displayTable(orders: List<List<String>>): List<List<String>> {
        val foods = sortedSetOf<String>()
        val tables = sortedSetOf<Int>()
        val counts = HashMap<Pair<Int, String>, Int>()
        for (order in orders) {
            val table = order[1].toInt()
            val food = order[2]
            foods.add(food)
            tables.add(table)
            val key = table to food
            counts[key] = counts.getOrDefault(key, 0) + 1
        }
        val foodList = foods.toList()
        val result = ArrayList<List<String>>()
        result.add(listOf("Table") + foodList)
        for (table in tables) {
            val row = ArrayList<String>()
            row.add(table.toString())
            for (food in foodList) {
                row.add(counts.getOrDefault(table to food, 0).toString())
            }
            result.add(row)
        }
        return result
    }
}
