// LeetCode 1452 - People Whose List of Favorite Companies Is Not a Subset of Another List
// https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

class Solution {
    fun peopleIndexes(favoriteCompanies: List<List<String>>): List<Int> {
        val sets = favoriteCompanies.map { it.toSet() }
        val answer = mutableListOf<Int>()
        for (i in sets.indices) {
            val s = sets[i]
            val isSubset = sets.indices.any { j -> i != j && sets[j].containsAll(s) }
            if (!isSubset) answer.add(i)
        }
        return answer
    }
}
