// LeetCode 0432 - All O`one Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class AllOne {
    private static class Bucket {
        int count;
        Set<String> keys = new HashSet<>();
        Bucket prev;
        Bucket next;

        Bucket(int count) {
            this.count = count;
        }
    }

    private final Bucket head = new Bucket(0);
    private final Bucket tail = new Bucket(0);
    private final Map<String, Bucket> keyNodes = new HashMap<>();

    public AllOne() {
        head.next = tail;
        tail.prev = head;
    }

    private void insertAfter(Bucket anchor, Bucket node) {
        node.prev = anchor;
        node.next = anchor.next;
        anchor.next.prev = node;
        anchor.next = node;
    }

    private void remove(Bucket node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private Bucket ensureCountNode(int count, Bucket after) {
        Bucket current = after.next;
        while (current != tail && current.count < count) {
            current = current.next;
        }
        if (current != tail && current.count == count) {
            return current;
        }
        Bucket bucket = new Bucket(count);
        insertAfter(current.prev, bucket);
        return bucket;
    }

    public void inc(String key) {
        if (keyNodes.containsKey(key)) {
            Bucket bucket = keyNodes.get(key);
            bucket.keys.remove(key);
            Bucket nextBucket = ensureCountNode(bucket.count + 1, bucket);
            nextBucket.keys.add(key);
            keyNodes.put(key, nextBucket);
            if (bucket.keys.isEmpty()) {
                remove(bucket);
            }
            return;
        }

        Bucket bucket = ensureCountNode(1, head);
        bucket.keys.add(key);
        keyNodes.put(key, bucket);
    }

    public void dec(String key) {
        Bucket bucket = keyNodes.get(key);
        bucket.keys.remove(key);
        if (bucket.count == 1) {
            keyNodes.remove(key);
        } else {
            Bucket prevBucket = ensureCountNode(bucket.count - 1, head);
            prevBucket.keys.add(key);
            keyNodes.put(key, prevBucket);
        }
        if (bucket.keys.isEmpty()) {
            remove(bucket);
        }
    }

    public String getMaxKey() {
        Bucket bucket = tail.prev;
        if (bucket == head) {
            return "";
        }
        return bucket.keys.iterator().next();
    }

    public String getMinKey() {
        Bucket bucket = head.next;
        if (bucket == tail) {
            return "";
        }
        return bucket.keys.iterator().next();
    }
}
