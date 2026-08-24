// LeetCode 0362 - Design Hit Counter

// https://leetcode.com/problems/design-hit-counter/



class HitCounter {

    private val hits = ArrayDeque<Int>()



    fun hit(timestamp: Int) {

        hits.addLast(timestamp)

    }



    fun getHits(timestamp: Int): Int {

        while (hits.isNotEmpty() && hits.first() <= timestamp - 300) {

            hits.removeFirst()

        }

        return hits.size

    }

}
