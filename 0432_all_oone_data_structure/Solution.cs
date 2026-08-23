// LeetCode 0432 - All O`one Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

using System.Collections.Generic;
using System.Linq;

public class AllOne {
    private class Bucket {
        public int Count;
        public HashSet<string> Keys = new HashSet<string>();
        public Bucket Prev;
        public Bucket Next;

        public Bucket(int count = 0) {
            Count = count;
        }
    }

    private readonly Bucket head = new Bucket();
    private readonly Bucket tail = new Bucket();
    private readonly Dictionary<string, Bucket> keyNodes = new Dictionary<string, Bucket>();

    public AllOne() {
        head.Next = tail;
        tail.Prev = head;
    }

    private void InsertAfter(Bucket anchor, Bucket node) {
        node.Prev = anchor;
        node.Next = anchor.Next;
        anchor.Next.Prev = node;
        anchor.Next = node;
    }

    private void Remove(Bucket node) {
        node.Prev.Next = node.Next;
        node.Next.Prev = node.Prev;
    }

    private Bucket EnsureCountNode(int count, Bucket after) {
        Bucket current = after.Next;
        while (current != tail && current.Count < count) {
            current = current.Next;
        }
        if (current != tail && current.Count == count) {
            return current;
        }
        Bucket bucket = new Bucket(count);
        InsertAfter(current.Prev, bucket);
        return bucket;
    }

    public void Inc(string key) {
        if (keyNodes.TryGetValue(key, out Bucket bucket)) {
            bucket.Keys.Remove(key);
            Bucket nextBucket = EnsureCountNode(bucket.Count + 1, bucket);
            nextBucket.Keys.Add(key);
            keyNodes[key] = nextBucket;
            if (bucket.Keys.Count == 0) {
                Remove(bucket);
            }
            return;
        }

        bucket = EnsureCountNode(1, head);
        bucket.Keys.Add(key);
        keyNodes[key] = bucket;
    }

    public void Dec(string key) {
        Bucket bucket = keyNodes[key];
        bucket.Keys.Remove(key);
        if (bucket.Count == 1) {
            keyNodes.Remove(key);
        } else {
            Bucket prevBucket = EnsureCountNode(bucket.Count - 1, head);
            prevBucket.Keys.Add(key);
            keyNodes[key] = prevBucket;
        }
        if (bucket.Keys.Count == 0) {
            Remove(bucket);
        }
    }

    public string GetMaxKey() {
        Bucket bucket = tail.Prev;
        if (bucket == head) {
            return "";
        }
        return bucket.Keys.First();
    }

    public string GetMinKey() {
        Bucket bucket = head.Next;
        if (bucket == tail) {
            return "";
        }
        return bucket.Keys.First();
    }
}
