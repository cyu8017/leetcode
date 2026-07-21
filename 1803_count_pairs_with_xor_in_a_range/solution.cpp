// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

#include <vector>

class Solution {
public:
    int countPairs(std::vector<int>& nums, int low, int high) {
        return countSmallerThan(nums, high + 1) - countSmallerThan(nums, low);
    }

private:
    struct TrieNode {
        int count = 0;
        TrieNode* children[2] = {nullptr, nullptr};
    };

    int countSmallerThan(const std::vector<int>& nums, int limit) {
        if (limit <= 0) {
            return 0;
        }
        TrieNode* root = new TrieNode();
        int total = 0;
        const int maxBit = 15;
        for (int num : nums) {
            total += query(root, num, limit, maxBit);
            insert(root, num, maxBit);
        }
        return total;
    }

    void insert(TrieNode* root, int num, int bit) {
        TrieNode* node = root;
        for (int i = bit; i >= 0; --i) {
            int b = (num >> i) & 1;
            if (!node->children[b]) {
                node->children[b] = new TrieNode();
            }
            node = node->children[b];
            node->count += 1;
        }
    }

    int query(TrieNode* root, int num, int limit, int bit) {
        if (!root || bit < 0) {
            return 0;
        }
        int numBit = (num >> bit) & 1;
        int limitBit = (limit >> bit) & 1;
        TrieNode* child = root->children[numBit];
        if (limitBit == 1) {
            int result = child ? child->count : 0;
            result += query(root->children[1 - numBit], num, limit, bit - 1);
            return result;
        }
        return query(child, num, limit, bit - 1);
    }
};
