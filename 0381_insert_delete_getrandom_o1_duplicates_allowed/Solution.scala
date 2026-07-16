// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed

// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/



import scala.collection.mutable



class RandomizedCollection {

  private val values = mutable.ArrayBuffer.empty[Int]

  private val indicesByValue = mutable.Map.empty[Int, mutable.Set[Int]]



  def insert(value: Int): Boolean = {

    val indices = indicesByValue.getOrElseUpdate(value, mutable.Set.empty[Int])

    indices += values.length

    values += value

    indices.size == 1

  }



  def remove(value: Int): Boolean = {

    val indexSet = indicesByValue.get(value)

    if (indexSet.isEmpty || indexSet.get.isEmpty) {

      return false

    }



    val indices = indexSet.get

    val index = indices.head

    val lastIndex = values.length - 1

    val lastValue = values.last

    values(index) = lastValue

    indicesByValue(lastValue) -= lastIndex

    indicesByValue(lastValue) += index

    values.remove(lastIndex)

    indices -= index

    if (indices.isEmpty) {

      indicesByValue.remove(value)

    }

    true

  }



  def getRandom(): Int = values.last

}
