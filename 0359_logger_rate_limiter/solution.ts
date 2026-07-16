export class Logger {
    private lastPrinted = new Map<string, number>();

    shouldPrintMessage(timestamp: number, message: string): boolean {
        if (!this.lastPrinted.has(message) || timestamp - this.lastPrinted.get(message)! >= 10) {
            this.lastPrinted.set(message, timestamp);
            return true;
        }
        return false;
    }
}
