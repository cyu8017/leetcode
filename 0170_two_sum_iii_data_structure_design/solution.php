// LeetCode 0170 - Two Sum III - Data structure design
// https://leetcode.com/problems/two-sum-iii-data-structure-design/

class TwoSum {
    private array $counts = [];

    function add(int $number): void {
        $this->counts[$number] = ($this->counts[$number] ?? 0) + 1;
    }

    function find(int $value): bool {
        foreach ($this->counts as $number => $count) {
            $number = (int) $number;
            $complement = $value - $number;
            if ($complement === $number) {
                if ($count >= 2) return true;
            } elseif (isset($this->counts[$complement])) {
                return true;
            }
        }
        return false;
    }
}