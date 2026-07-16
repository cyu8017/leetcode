// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

import java.util.Iterator;

class PeekingIterator implements Iterator<Integer> {
    private Iterator<Integer> iterator;
    private Integer peeked;
    private boolean hasPeeked;

    public PeekingIterator(Iterator<Integer> iterator) {
        this.iterator = iterator;
        this.hasPeeked = false;
    }

    public PeekingIterator(int[] nums) {
        this(new Iterator<Integer>() {
            private int index = 0;

            @Override
            public boolean hasNext() {
                return index < nums.length;
            }

            @Override
            public Integer next() {
                return nums[index++];
            }
        });
    }

    public int peek() {
        if (!hasPeeked) {
            peeked = iterator.next();
            hasPeeked = true;
        }
        return peeked;
    }

    @Override
    public Integer next() {
        if (hasPeeked) {
            int result = peeked;
            peeked = null;
            hasPeeked = false;
            return result;
        }
        return iterator.next();
    }

    @Override
    public boolean hasNext() {
        return hasPeeked || iterator.hasNext();
    }
}
