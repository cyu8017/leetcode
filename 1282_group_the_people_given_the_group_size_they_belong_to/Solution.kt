// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution {
    fun groupThePeople(groupSizes: IntArray): List<List<Int>> {
        val pending = mutableMapOf<Int, MutableList<Int>>()
        val answer = mutableListOf<List<Int>>()
        for (person in groupSizes.indices) {
            val size = groupSizes[person]
            val bucket = pending.getOrPut(size) { mutableListOf() }
            bucket.add(person)
            if (bucket.size == size) {
                answer.add(bucket.toList())
                pending[size] = mutableListOf()
            }
        }
        return answer.sortedWith(compareBy({ it.size }, { it.toString() }))
    }
}
