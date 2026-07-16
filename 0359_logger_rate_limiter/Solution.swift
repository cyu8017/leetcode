// LeetCode 0359 - Logger Rate Limiter
// https://leetcode.com/problems/logger-rate-limiter/

class Logger {
    private var lastPrinted: [String: Int] = [:]

    init() {
    }

    func shouldPrintMessage(_ timestamp: Int, _ message: String) -> Bool {
        if lastPrinted[message] == nil || timestamp - lastPrinted[message]! >= 10 {
            lastPrinted[message] = timestamp
            return true
        }

        return false
    }
}
