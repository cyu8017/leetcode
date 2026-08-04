// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/

class Solution {
    fun reformatDate(date: String): String {
        val months = arrayOf(
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        )
        val parts = date.split(" ")
        val day = parts[0]
        val month = parts[1]
        val year = parts[2]
        var monthIndex = 0
        for (i in months.indices) {
            if (months[i] == month) {
                monthIndex = i + 1
                break
            }
        }
        val dayValue = day.substring(0, day.length - 2).toInt()
        return String.format("%s-%02d-%02d", year, monthIndex, dayValue)
    }
}
