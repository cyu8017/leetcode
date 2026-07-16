// LeetCode 0380 - Insert Delete GetRandom O(1)

// https://leetcode.com/problems/insert-delete-getrandom-o1/



import scala.collection.mutable

import scala.util.Random



class RandomizedSet {

  private val values = mutable.ArrayBuffer.empty[Int]

  private val indexByValue = mutable.Map.empty[Int, Int]

  private val random = new Random()



  def insert(value: Int): Boolean = {

    if (indexByValue.contains(value)) {

      return false

    }

    indexByValue(value) = values.length

    values += value

    true

  }



  def remove(value: Int): Boolean = {

    if (!indexByValue.contains(value)) {

      return false

    }



    val index = indexByValue(value)

    val lastValue = values.last

    values(index) = lastValue

    indexByValue(lastValue) = index

    values.remove(values.length - 1)

    indexByValue.remove(value)

    true

  }



  def getRandom(): Int = values(random.nextInt(values.length))

}
