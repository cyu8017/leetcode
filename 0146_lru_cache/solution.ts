// LeetCode 0146 - LRU Cache
// https://leetcode.com/problems/lru-cache/

class Node {
  key: number;
  value: number;
  prev: Node | null = null;
  next: Node | null = null;

  constructor(key = 0, value = 0) {
    this.key = key;
    this.value = value;
  }
}

export class LRUCache {
  private readonly capacity: number;
  private readonly cache = new Map<number, Node>();
  private readonly head = new Node();
  private readonly tail = new Node();

  constructor(capacity: number) {
    this.capacity = capacity;
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  private remove(node: Node): void {
    node.prev!.next = node.next;
    node.next!.prev = node.prev;
  }

  private addToFront(node: Node): void {
    node.prev = this.head;
    node.next = this.head.next;
    this.head.next!.prev = node;
    this.head.next = node;
  }

  get(key: number): number {
    const node = this.cache.get(key);
    if (!node) return -1;
    this.remove(node);
    this.addToFront(node);
    return node.value;
  }

  put(key: number, value: number): void {
    const existing = this.cache.get(key);
    if (existing) {
      existing.value = value;
      this.remove(existing);
      this.addToFront(existing);
      return;
    }

    if (this.cache.size === this.capacity) {
      const leastRecent = this.tail.prev!;
      this.remove(leastRecent);
      this.cache.delete(leastRecent.key);
    }

    const node = new Node(key, value);
    this.cache.set(key, node);
    this.addToFront(node);
  }
}