// LeetCode 0432 - All O`one` Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

class CountNode {
    public int $count;
    /** @var array<string, true> */
    public array $keys = [];
    public ?CountNode $prev = null;
    public ?CountNode $next = null;

    function __construct(int $count = 0) {
        $this->count = $count;
    }
}

class AllOne {
    private CountNode $head;
    private CountNode $tail;
    /** @var array<string, CountNode> */
    private array $keyNodes = [];

    function __construct() {
        $this->head = new CountNode();
        $this->tail = new CountNode();
        $this->head->next = $this->tail;
        $this->tail->prev = $this->head;
    }

    function inc(string $key): void {
        if (isset($this->keyNodes[$key])) {
            $bucket = $this->keyNodes[$key];
            unset($bucket->keys[$key]);
            $nextBucket = $this->ensureCountNode($bucket->count + 1, $bucket);
            $nextBucket->keys[$key] = true;
            $this->keyNodes[$key] = $nextBucket;
            if (count($bucket->keys) === 0) {
                $this->remove($bucket);
            }
            return;
        }

        $bucket = $this->ensureCountNode(1, $this->head);
        $bucket->keys[$key] = true;
        $this->keyNodes[$key] = $bucket;
    }

    function dec(string $key): void {
        $bucket = $this->keyNodes[$key];
        unset($bucket->keys[$key]);
        if ($bucket->count === 1) {
            unset($this->keyNodes[$key]);
        } else {
            $prevBucket = $this->ensureCountNode($bucket->count - 1, $this->head);
            $prevBucket->keys[$key] = true;
            $this->keyNodes[$key] = $prevBucket;
        }
        if (count($bucket->keys) === 0) {
            $this->remove($bucket);
        }
    }

    function getMaxKey(): string {
        $bucket = $this->tail->prev;
        if ($bucket === $this->head) {
            return "";
        }
        return array_key_first($bucket->keys);
    }

    function getMinKey(): string {
        $bucket = $this->head->next;
        if ($bucket === $this->tail) {
            return "";
        }
        return array_key_first($bucket->keys);
    }

    private function insertAfter(CountNode $anchor, CountNode $node): void {
        $node->prev = $anchor;
        $node->next = $anchor->next;
        $anchor->next->prev = $node;
        $anchor->next = $node;
    }

    private function remove(CountNode $node): void {
        $node->prev->next = $node->next;
        $node->next->prev = $node->prev;
    }

    private function ensureCountNode(int $count, CountNode $after): CountNode {
        $current = $after->next;
        while ($current !== $this->tail && $current->count < $count) {
            $current = $current->next;
        }
        if ($current !== $this->tail && $current->count === $count) {
            return $current;
        }

        $bucket = new CountNode($count);
        $this->insertAfter($current->prev, $bucket);
        return $bucket;
    }
}
