// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    struct TrieNode* next[26];
} TrieNode;

static TrieNode* newNode(void) {
    return (TrieNode*)calloc(1, sizeof(TrieNode));
}

static void freeTrie(TrieNode* node) {
    if (!node) return;
    for (int i = 0; i < 26; i++) freeTrie(node->next[i]);
    free(node);
}

int countDistinct(char* s) {
    TrieNode* root = newNode();
    int ans = 0;
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        TrieNode* node = root;
        for (int j = i; j < n; j++) {
            int c = s[j] - 'a';
            if (!node->next[c]) {
                node->next[c] = newNode();
                ans++;
            }
            node = node->next[c];
        }
    }
    freeTrie(root);
    return ans;
}
