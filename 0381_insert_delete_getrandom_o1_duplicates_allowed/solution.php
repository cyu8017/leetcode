// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

class RandomizedCollection {
    /** @var int[] */
    private array $values = [];

    /** @var array<int, array<int, bool>> */
    private array $indices = [];

    /**
     * @param Integer $val
     * @return Boolean
     */
    function insert($val) {
        if (!isset($this->indices[$val])) {
            $this->indices[$val] = [];
        }
        $this->indices[$val][count($this->values)] = true;
        $this->values[] = $val;
        return count($this->indices[$val]) === 1;
    }

    /**
     * @param Integer $val
     * @return Boolean
     */
    function remove($val) {
        if (!isset($this->indices[$val]) || count($this->indices[$val]) === 0) {
            return false;
        }

        $index = array_key_first($this->indices[$val]);
        $lastIndex = count($this->values) - 1;
        $lastValue = $this->values[$lastIndex];
        $this->values[$index] = $lastValue;
        unset($this->indices[$lastValue][$lastIndex]);
        $this->indices[$lastValue][$index] = true;
        array_pop($this->values);
        unset($this->indices[$val][$index]);
        if (count($this->indices[$val]) === 0) {
            unset($this->indices[$val]);
        }
        return true;
    }

    /**
     * @return Integer
     */
    function getRandom() {
        return $this->values[count($this->values) - 1];
    }
}
