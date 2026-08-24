// LeetCode 0359 - Logger Rate Limiter

// https://leetcode.com/problems/logger-rate-limiter/



class Logger {

    private val lastPrinted = mutableMapOf<String, Int>()



    fun shouldPrintMessage(timestamp: Int, message: String): Boolean {

        val last = lastPrinted[message]

        if (last == null || timestamp - last >= 10) {

            lastPrinted[message] = timestamp

            return true

        }

        return false

    }

}
