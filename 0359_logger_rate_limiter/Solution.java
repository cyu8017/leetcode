// LeetCode 0359 - Logger Rate Limiter

// https://leetcode.com/problems/logger-rate-limiter/



import java.util.HashMap;

import java.util.Map;



class Logger {

    private final Map<String, Integer> lastPrinted = new HashMap<>();



    public Logger() {

    }



    public boolean shouldPrintMessage(int timestamp, String message) {

        if (!lastPrinted.containsKey(message)

            || timestamp - lastPrinted.get(message) >= 10) {

            lastPrinted.put(message, timestamp);

            return true;

        }

        return false;

    }

}
