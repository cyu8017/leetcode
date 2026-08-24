// LeetCode 0406 - Queue Reconstruction by Height

// https://leetcode.com/problems/queue-reconstruction-by-height/



class Solution {

    fun reconstructQueue(people: Array<IntArray>): Array<IntArray> {

        people.sortWith(compareByDescending<IntArray> { it[0] }.thenBy { it[1] })

        val queue = mutableListOf<IntArray>()



        for (person in people) {

            queue.add(person[1], person)

        }



        return queue.toTypedArray()

    }

}
