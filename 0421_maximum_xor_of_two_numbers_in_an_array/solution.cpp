// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int findMaximumXOR(std::vector<int>& nums) {
        int maximum = *std::max_element(nums.begin(), nums.end());
        int maxBit = 0;
        while ((1 << maxBit) <= maximum && maxBit < 31) {
            ++maxBit;
        }

        struct TrieNode {
            std::unordered_map<int, TrieNode*> children;
        };

        TrieNode root;
        for (int number : nums) {
            TrieNode* node = &root;
            for (int bit = maxBit - 1; bit >= 0; --bit) {
                int current = (number >> bit) & 1;
                if (!node->children.count(current)) {
                    node->children[current] = new TrieNode();
                }
                node = node->children[current];
            }
        }

        int best = 0;
        for (int number : nums) {
            TrieNode* node = &root;
            int candidate = 0;
            for (int bit = maxBit - 1; bit >= 0; --bit) {
                int current = (number >> bit) & 1;
                int target = 1 - current;
                if (node->children.count(target)) {
                    candidate |= 1 << bit;
                    node = node->children[target];
                } else {
                    node = node->children[current];
                }
            }
            best = std::max(best, candidate);
        }

        return best;
    }
};
