// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

class ListIterator {
    /** @var int[] */
    private $values;
    /** @var int */
    private $index;

    /**
     * @param Integer[] $values
     */
    function __construct($values) {
        $this->values = $values;
        $this->index = 0;
    }

    /**
     * @return Integer
     */
    function next() {
        $value = $this->values[$this->index];
        $this->index++;
        return $value;
    }

    /**
     * @return Boolean
     */
    function hasNext() {
        return $this->index < count($this->values);
    }
}

class PeekingIterator {
    /** @var ListIterator */
    private $iterator;
    /** @var Integer|null */
    private $peeked;
    /** @var Boolean */
    private $hasPeeked;

    /**
     * @param ListIterator $iterator
     */
    function __construct($iterator) {
        $this->iterator = $iterator;
        $this->peeked = null;
        $this->hasPeeked = false;
    }

    /**
     * @return Integer
     */
    function peek() {
        if (!$this->hasPeeked) {
            $this->peeked = $this->iterator->next();
            $this->hasPeeked = true;
        }
        return $this->peeked;
    }

    /**
     * @return Integer
     */
    function next() {
        if ($this->hasPeeked) {
            $result = $this->peeked;
            $this->peeked = null;
            $this->hasPeeked = false;
            return $result;
        }
        return $this->iterator->next();
    }

    /**
     * @return Boolean
     */
    function hasNext() {
        return $this->hasPeeked || $this->iterator->hasNext();
    }
}
