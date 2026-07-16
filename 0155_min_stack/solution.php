// LeetCode 0155 - Min Stack
// https://leetcode.com/problems/min-stack/

class MinStack {
    private array $values = [];
    private array $minimums = [];

    function push(int $val): void {
        $this->values[] = $val;
        $this->minimums[] = min($val, $this->minimums[count($this->minimums) - 1] ?? $val);
    }

    function pop(): void {
        array_pop($this->values);
        array_pop($this->minimums);
    }

    function top(): int {
        return $this->values[count($this->values) - 1];
    }

    function getMin(): int {
        return $this->minimums[count($this->minimums) - 1];
    }
}