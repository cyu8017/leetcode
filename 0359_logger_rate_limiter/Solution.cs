// LeetCode 0359 - Logger Rate Limiter

// https://leetcode.com/problems/logger-rate-limiter/



using System.Collections.Generic;



public class Logger {

    private readonly Dictionary<string, int> lastPrinted = new();



    public Logger() {

    }



    public bool ShouldPrintMessage(int timestamp, string message) {

        if (!lastPrinted.ContainsKey(message)

            || timestamp - lastPrinted[message] >= 10) {

            lastPrinted[message] = timestamp;

            return true;

        }

        return false;

    }

}
