// LeetCode 0362 - Design Hit Counter
// https://leetcode.com/problems/design-hit-counter/

class HitCounter {
    /** @var int[] */
    private array $hits = [];

    function hit(int $timestamp): void {
        $this->hits[] = $timestamp;
    }

    function getHits(int $timestamp): int {
        return $this->get_hits($timestamp);
    }

    function get_hits(int $timestamp): int {
        while (count($this->hits) > 0 && $this->hits[0] <= $timestamp - 300) {
            array_shift($this->hits);
        }
        return count($this->hits);
    }
}
