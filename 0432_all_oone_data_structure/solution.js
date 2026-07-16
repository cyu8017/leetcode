// LeetCode 0432 - All O`one Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

class BucketNode {
    constructor(count = 0) {
        this.count = count;
        this.keys = new Set();
        this.prev = null;
        this.next = null;
    }
}

class AllOne {
    constructor() {
        this.head = new BucketNode();
        this.tail = new BucketNode();
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.keyNodes = new Map();
    }

    _insertAfter(anchor, node) {
        node.prev = anchor;
        node.next = anchor.next;
        anchor.next.prev = node;
        anchor.next = node;
    }

    _remove(node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    _ensureCountNode(count, after) {
        let current = after.next;
        while (current !== this.tail && current.count < count) {
            current = current.next;
        }
        if (current !== this.tail && current.count === count) {
            return current;
        }
        const bucket = new BucketNode(count);
        this._insertAfter(current.prev, bucket);
        return bucket;
    }

    inc(key) {
        if (this.keyNodes.has(key)) {
            const bucket = this.keyNodes.get(key);
            bucket.keys.delete(key);
            const nextBucket = this._ensureCountNode(bucket.count + 1, bucket);
            nextBucket.keys.add(key);
            this.keyNodes.set(key, nextBucket);
            if (!bucket.keys.size) this._remove(bucket);
            return;
        }

        const bucket = this._ensureCountNode(1, this.head);
        bucket.keys.add(key);
        this.keyNodes.set(key, bucket);
    }

    dec(key) {
        const bucket = this.keyNodes.get(key);
        bucket.keys.delete(key);
        if (bucket.count === 1) {
            this.keyNodes.delete(key);
        } else {
            const prevBucket = this._ensureCountNode(bucket.count - 1, this.head);
            prevBucket.keys.add(key);
            this.keyNodes.set(key, prevBucket);
        }
        if (!bucket.keys.size) this._remove(bucket);
    }

    getMaxKey() {
        const bucket = this.tail.prev;
        if (bucket === this.head) return "";
        return bucket.keys.values().next().value;
    }

    getMinKey() {
        const bucket = this.head.next;
        if (bucket === this.tail) return "";
        return bucket.keys.values().next().value;
    }
}

module.exports = { AllOne };
