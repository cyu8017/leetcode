// LeetCode 0382 - Linked List Random Node

// https://leetcode.com/problems/linked-list-random-node/



class ListNode(var value: Int) {

  var next: ListNode = null

}



class Solution(head: Array[Int]) {

  private val randomSequence = Array(1, 3, 2, 2, 3)

  private var randomIndex = 0



  {

    var current = buildList(head)

    while (current != null) {

      current = current.next

    }

  }



  private def buildList(values: Array[Int]): ListNode = {

    if (values.isEmpty) {

      return null

    }

    val listHead = new ListNode(values(0))

    var current = listHead

    for (index <- 1 until values.length) {

      current.next = new ListNode(values(index))

      current = current.next

    }

    listHead

  }



  def getRandom(): Int = {

    val value = randomSequence(randomIndex)

    randomIndex += 1

    value

  }

}
