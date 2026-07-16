// LeetCode 0341 - Flatten Nested List Iterator
// https://leetcode.com/problems/flatten-nested-list-iterator/

class NestedInteger {
    private $integer = null;
    private $list = [];

    function __construct($value = null) {
        if (is_int($value)) {
            $this->integer = $value;
        }
    }

    function isInteger() {
        return $this->integer !== null;
    }

    function getInteger() {
        return $this->integer ?? 0;
    }

    function getList() {
        return $this->list;
    }

    function add($item) {
        $this->list[] = $item;
    }
}

class NestedIterator {
    private array $stack = [];

    function __construct(array $nestedList) {
        for ($index = count($nestedList) - 1; $index >= 0; $index--) {
            $this->stack[] = [$nestedList[$index], 0];
        }
    }

    function next() {
        $this->prepareNext();
        $entry = array_pop($this->stack);
        return $entry[0]->getInteger();
    }

    function hasNext() {
        $this->prepareNext();
        return !empty($this->stack);
    }

    private function prepareNext(): void {
        while (!empty($this->stack)) {
            $current = $this->stack[count($this->stack) - 1][0];
            $index = $this->stack[count($this->stack) - 1][1];
            if ($current->isInteger()) {
                return;
            }

            $nested = $current->getList();
            if ($index >= count($nested)) {
                array_pop($this->stack);
                continue;
            }

            $this->stack[count($this->stack) - 1] = [$current, $index + 1];
            $this->stack[] = [$nested[$index], 0];
        }
    }
}
