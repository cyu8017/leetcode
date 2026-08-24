// LeetCode 0379 - Design Phone Directory

// https://leetcode.com/problems/design-phone-directory/



import java.util.TreeSet



class PhoneDirectory(maxNumbers: Int) {

    private val available = TreeSet((0 until maxNumbers).toList())



    fun get(): Int {

        if (available.isEmpty()) {

            return -1

        }

        val number = available.first()

        available.remove(number)

        return number

    }



    fun check(number: Int): Boolean = available.contains(number)



    fun release(number: Int) {

        available.add(number)

    }

}
