// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

class PeekingIterator {
    /**
     * @param {Iterator} iterator
     */
    constructor(iterator) {
        this.iterator = iterator;
        this.peeked = null;
        this.hasPeeked = false;
    }

    /**
     * @return {number}
     */
    peek() {
        if (!this.hasPeeked) {
            this.peeked = this.iterator.next();
            this.hasPeeked = true;
        }
        return this.peeked;
    }

    /**
     * @return {number}
     */
    next() {
        if (this.hasPeeked) {
            const result = this.peeked;
            this.peeked = null;
            this.hasPeeked = false;
            return result;
        }
        return this.iterator.next();
    }

    /**
     * @return {boolean}
     */
    hasNext() {
        return this.hasPeeked || this.iterator.hasNext();
    }
}

module.exports = { PeekingIterator };
