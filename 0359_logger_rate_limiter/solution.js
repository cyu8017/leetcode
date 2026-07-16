// LeetCode 0359 - Logger Rate Limiter
class Logger {
    constructor() {
        this.lastPrinted = new Map();
    }

    shouldPrintMessage(timestamp, message) {
        if (!this.lastPrinted.has(message) || timestamp - this.lastPrinted.get(message) >= 10) {
            this.lastPrinted.set(message, timestamp);
            return true;
        }
        return false;
    }
}

module.exports = { Logger };
