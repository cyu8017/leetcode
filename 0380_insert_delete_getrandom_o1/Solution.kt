// LeetCode 0380 - Insert Delete GetRandom O(1)

// https://leetcode.com/problems/insert-delete-getrandom-o1/



class RandomizedSet {

    private val values = mutableListOf<Int>()

    private val indexByValue = mutableMapOf<Int, Int>()



    fun insert(`val`: Int): Boolean {

        if (indexByValue.containsKey(`val`)) {

            return false

        }

        indexByValue[`val`] = values.size

        values.add(`val`)

        return true

    }



    fun remove(`val`: Int): Boolean {

        if (!indexByValue.containsKey(`val`)) {

            return false

        }



        val index = indexByValue[`val`]!!

        val lastValue = values.last()

        values[index] = lastValue

        indexByValue[lastValue] = index

        values.removeAt(values.lastIndex)

        indexByValue.remove(`val`)

        return true

    }



    fun getRandom(): Int = values.random()

}
