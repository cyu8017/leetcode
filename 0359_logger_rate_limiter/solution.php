// LeetCode 0359 - Logger Rate Limiter
// https://leetcode.com/problems/logger-rate-limiter/

class Logger {
    /** @var array<string, int> */
    private array $lastPrinted = [];

    function shouldPrintMessage(int $timestamp, string $message): bool {
        return $this->should_print_message($timestamp, $message);
    }

    function should_print_message(int $timestamp, string $message): bool {
        if (
            !array_key_exists($message, $this->lastPrinted)
            || $timestamp - $this->lastPrinted[$message] >= 10
        ) {
            $this->lastPrinted[$message] = $timestamp;
            return true;
        }

        return false;
    }
}
