// LeetCode 0146 - LRU Cache
// https://leetcode.com/problems/lru-cache/

class LRUCache {
  /**
   * @param {number} capacity
   */
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
    this.head = { key: 0, value: 0, prev: null, next: null };
    this.tail = { key: 0, value: 0, prev: this.head, next: null };
    this.head.next = this.tail;
  }

  /**
   * @param {{ prev: object, next: object }} node
   * @return {void}
   */
  remove(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
  }

  /**
   * @param {{ prev: object|null, next: object|null }} node
   * @return {void}
   */
  addToFront(node) {
    node.prev = this.head;
    node.next = this.head.next;
    this.head.next.prev = node;
    this.head.next = node;
  }

  /**
   * @param {number} key
   * @return {number}
   */
  get(key) {
    const node = this.cache.get(key);
    if (!node) return -1;
    this.remove(node);
    this.addToFront(node);
    return node.value;
  }

  /**
   * @param {number} key
   * @param {number} value
   * @return {void}
   */
  put(key, value) {
    const existing = this.cache.get(key);
    if (existing) {
      existing.value = value;
      this.remove(existing);
      this.addToFront(existing);
      return null;
    }

    if (this.cache.size === this.capacity) {
      const leastRecent = this.tail.prev;
      this.remove(leastRecent);
      this.cache.delete(leastRecent.key);
    }

    const node = { key, value, prev: null, next: null };
    this.cache.set(key, node);
    this.addToFront(node);
    return null;
  }
}

module.exports = { LRUCache };