// LeetCode 0432 - All O`one Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

class BucketNode {
    count: number;
    keys: Set<string>;
    prev: BucketNode | null;
    next: BucketNode | null;

    constructor(count = 0) {
        this.count = count;
        this.keys = new Set();
        this.prev = null;
        this.next = null;
    }
}

export class AllOne {
    private head: BucketNode;
    private tail: BucketNode;
    private keyNodes: Map<string, BucketNode>;

    constructor() {
        this.head = new BucketNode();
        this.tail = new BucketNode();
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.keyNodes = new Map();
    }

    private _insertAfter(anchor: BucketNode, node: BucketNode): void {
        node.prev = anchor;
        node.next = anchor.next;
        anchor.next!.prev = node;
        anchor.next = node;
    }

    private _remove(node: BucketNode): void {
        node.prev!.next = node.next;
        node.next!.prev = node.prev;
    }

    private _ensureCountNode(count: number, after: BucketNode): BucketNode {
        let current = after.next!;
        while (current !== this.tail && current.count < count) {
            current = current.next!;
        }
        if (current !== this.tail && current.count === count) {
            return current;
        }
        const bucket = new BucketNode(count);
        this._insertAfter(current.prev!, bucket);
        return bucket;
    }

    inc(key: string): void {
        if (this.keyNodes.has(key)) {
            const bucket = this.keyNodes.get(key)!;
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

    dec(key: string): void {
        const bucket = this.keyNodes.get(key)!;
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

    getMaxKey(): string {
        const bucket = this.tail.prev!;
        if (bucket === this.head) return "";
        return bucket.keys.values().next().value as string;
    }

    getMinKey(): string {
        const bucket = this.head.next!;
        if (bucket === this.tail) return "";
        return bucket.keys.values().next().value as string;
    }
}
