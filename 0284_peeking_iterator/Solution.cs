// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

public interface Iterator {
    int Next();
    bool HasNext();
}

public class PeekingIterator {
    private readonly Iterator iterator;
    private int? peeked;
    private bool hasPeeked;

    public PeekingIterator(Iterator iterator) {
        this.iterator = iterator;
        hasPeeked = false;
    }

    public int Peek() {
        if (!hasPeeked) {
            peeked = iterator.Next();
            hasPeeked = true;
        }
        return peeked.Value;
    }

    public int Next() {
        if (hasPeeked) {
            int result = peeked.Value;
            peeked = null;
            hasPeeked = false;
            return result;
        }
        return iterator.Next();
    }

    public bool HasNext() {
        return hasPeeked || iterator.HasNext();
    }
}
