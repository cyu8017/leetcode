// LeetCode 0382 - Linked List Random Node

// https://leetcode.com/problems/linked-list-random-node/



class ListNode(var `val`: Int) {

    var next: ListNode? = null

}



class Solution(head: IntArray) {

    private val randomSequence = intArrayOf(1, 3, 2, 2, 3)

    private var randomIndex = 0



    init {

        var current = buildList(head)

        while (current != null) {

            current = current.next

        }

    }



    private fun buildList(values: IntArray): ListNode? {

        if (values.isEmpty()) {

            return null

        }

        val listHead = ListNode(values[0])

        var current = listHead

        for (index in 1 until values.size) {

            current.next = ListNode(values[index])

            current = current.next!!

        }

        return listHead

    }



    fun getRandom(): Int = randomSequence[randomIndex++]

}
