// LeetCode 1452 - People Whose List of Favorite Companies Is Not a Subset of Another List
// https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

class Solution {
    fun peopleIndexes(favoriteCompanies: List<List<String>>): List<Int> {
        val sets = favoriteCompanies.map { it.toSet() }
        return sets.indices.filter { i ->
            sets.indices.none { j -> i != j && sets[j].containsAll(sets[i]) }
        }
    }
}
