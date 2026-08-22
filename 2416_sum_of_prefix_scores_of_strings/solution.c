// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    struct TrieNode* child[26];
    int cnt;
} TrieNode;

static TrieNode* newNode(void) { return (TrieNode*)calloc(1, sizeof(TrieNode)); }

static void freeTrie(TrieNode* n) {
    if (!n) return;
    for (int i = 0; i < 26; i++) freeTrie(n->child[i]);
    free(n);
}

int* sumPrefixScores(char** words, int wordsSize, int* returnSize) {
    TrieNode* root = newNode();
    for (int i = 0; i < wordsSize; i++) {
        TrieNode* cur = root;
        for (int j = 0; words[i][j]; j++) {
            int c = words[i][j] - 'a';
            if (!cur->child[c]) cur->child[c] = newNode();
            cur = cur->child[c];
            cur->cnt++;
        }
    }
    int* ans = (int*)malloc((size_t)wordsSize * sizeof(int));
    for (int i = 0; i < wordsSize; i++) {
        TrieNode* cur = root;
        int sum = 0;
        for (int j = 0; words[i][j]; j++) {
            cur = cur->child[words[i][j] - 'a'];
            sum += cur->cnt;
        }
        ans[i] = sum;
    }
    freeTrie(root);
    *returnSize = wordsSize;
    return ans;
}
