// LeetCode 0379 - Design Phone Directory

// https://leetcode.com/problems/design-phone-directory/



import scala.collection.mutable



class PhoneDirectory(maxNumbers: Int) {

  private val available = {
    val set = mutable.SortedSet.empty[Int]
    for (index <- 0 until maxNumbers) {
      set += index
    }
    set
  }



  def get(): Int = {

    if (available.isEmpty) {

      return -1

    }

    val number = available.head

    available.remove(number)

    number

  }



  def check(number: Int): Boolean = available.contains(number)



  def release(number: Int): Unit = {

    available += number

  }

}
