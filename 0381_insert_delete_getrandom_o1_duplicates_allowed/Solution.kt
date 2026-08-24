// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed

// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/



class RandomizedCollection {

    private val values = mutableListOf<Int>()

    private val indicesByValue = mutableMapOf<Int, MutableSet<Int>>()



    fun insert(`val`: Int): Boolean {

        val indices = indicesByValue.getOrPut(`val`) { mutableSetOf() }

        indices.add(values.size)

        values.add(`val`)

        return indices.size == 1

    }



    fun remove(`val`: Int): Boolean {

        val indices = indicesByValue[`val`] ?: return false

        if (indices.isEmpty()) {

            return false

        }



        val index = indices.first()

        val lastIndex = values.lastIndex

        val lastValue = values[lastIndex]

        values[index] = lastValue

        indicesByValue.getValue(lastValue).remove(lastIndex)

        indicesByValue.getValue(lastValue).add(index)

        values.removeAt(lastIndex)

        indices.remove(index)

        if (indices.isEmpty()) {

            indicesByValue.remove(`val`)

        }

        return true

    }



    fun getRandom(): Int = values.last()

}
