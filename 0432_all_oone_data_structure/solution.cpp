// LeetCode 0432 - All O`one` Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

#include <string>
#include <unordered_map>
#include <unordered_set>

class AllOne {
    struct Bucket {
        int count;
        std::unordered_set<std::string> keys;
        Bucket* prev;
        Bucket* next;

        explicit Bucket(int bucketCount = 0)
            : count(bucketCount), prev(nullptr), next(nullptr) {}
    };

    Bucket head_;
    Bucket tail_;
    std::unordered_map<std::string, Bucket*> keyNodes_;

    void insertAfter(Bucket* anchor, Bucket* node) {
        node->prev = anchor;
        node->next = anchor->next;
        anchor->next->prev = node;
        anchor->next = node;
    }

    void removeBucket(Bucket* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
        delete node;
    }

    Bucket* ensureCountNode(int count, Bucket* after) {
        Bucket* current = after->next;
        while (current != &tail_ && current->count < count) {
            current = current->next;
        }
        if (current != &tail_ && current->count == count) {
            return current;
        }
        Bucket* bucket = new Bucket(count);
        insertAfter(current->prev, bucket);
        return bucket;
    }

public:
    AllOne() {
        head_.next = &tail_;
        tail_.prev = &head_;
    }

    void inc(const std::string& key) {
        if (keyNodes_.count(key)) {
            Bucket* bucket = keyNodes_[key];
            bucket->keys.erase(key);
            Bucket* nextBucket = ensureCountNode(bucket->count + 1, bucket);
            nextBucket->keys.insert(key);
            keyNodes_[key] = nextBucket;
            if (bucket->keys.empty()) {
                removeBucket(bucket);
            }
            return;
        }

        Bucket* bucket = ensureCountNode(1, &head_);
        bucket->keys.insert(key);
        keyNodes_[key] = bucket;
    }

    void dec(const std::string& key) {
        Bucket* bucket = keyNodes_[key];
        bucket->keys.erase(key);
        if (bucket->count == 1) {
            keyNodes_.erase(key);
        } else {
            Bucket* prevBucket = ensureCountNode(bucket->count - 1, &head_);
            prevBucket->keys.insert(key);
            keyNodes_[key] = prevBucket;
        }
        if (bucket->keys.empty()) {
            removeBucket(bucket);
        }
    }

    std::string getMaxKey() {
        Bucket* bucket = tail_.prev;
        if (bucket == &head_) {
            return "";
        }
        return *bucket->keys.begin();
    }

    std::string getMinKey() {
        Bucket* bucket = head_.next;
        if (bucket == &tail_) {
            return "";
        }
        return *bucket->keys.begin();
    }
};
