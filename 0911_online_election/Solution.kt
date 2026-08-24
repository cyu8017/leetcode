// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

class TopVotedCandidate(persons: IntArray, times: IntArray) {
    private val times = times
    private val leaders = IntArray(persons.size)

    init {
        val counts = HashMap<Int, Int>()
        var leader = -1
        for (i in persons.indices) {
            counts[persons[i]] = counts.getOrDefault(persons[i], 0) + 1
            if (leader == -1 || counts[persons[i]]!! >= counts[leader]!!) leader = persons[i]
            leaders[i] = leader
        }
    }

    fun q(t: Int): Int {
        var i = java.util.Arrays.binarySearch(times, t)
        if (i < 0) i = -i - 2
        return leaders[i]
    }
}
