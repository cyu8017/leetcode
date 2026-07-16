// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    struct TrieNode* children[26];
    char* word;
} TrieNode;

static TrieNode* trieNodeCreate(void) {
    return calloc(1, sizeof(TrieNode));
}

static void trieFree(TrieNode* node) {
    if (!node) return;
    for (int i = 0; i < 26; ++i) trieFree(node->children[i]);
    free(node->word);
    free(node);
}

static void insertWord(TrieNode* root, char* word) {
    TrieNode* node = root;
    for (int i = 0; word[i]; ++i) {
        int index = word[i] - 'a';
        if (!node->children[index]) node->children[index] = trieNodeCreate();
        node = node->children[index];
    }
    node->word = strdup(word);
}

static void dfs(char** board, int boardSize, int* boardColSize, int row, int col, TrieNode* node, char** result, int* returnSize) {
    char c = board[row][col];
    TrieNode* next = node->children[c - 'a'];
    if (!next) return;
    if (next->word) {
        result[(*returnSize)++] = next->word;
        free(next->word);
        next->word = NULL;
    }
    board[row][col] = '#';
    if (row + 1 < boardSize && board[row + 1][col] != '#') dfs(board, boardSize, boardColSize, row + 1, col, next, result, returnSize);
    if (row - 1 >= 0 && board[row - 1][col] != '#') dfs(board, boardSize, boardColSize, row - 1, col, next, result, returnSize);
    if (col + 1 < boardColSize[row] && board[row][col + 1] != '#') dfs(board, boardSize, boardColSize, row, col + 1, next, result, returnSize);
    if (col - 1 >= 0 && board[row][col - 1] != '#') dfs(board, boardSize, boardColSize, row, col - 1, next, result, returnSize);
    board[row][col] = c;
    bool empty = true;
    for (int i = 0; i < 26; ++i) {
        if (next->children[i]) {
            empty = false;
            break;
        }
    }
    if (empty) node->children[c - 'a'] = NULL;
}

char** findWords(char** board, int boardSize, int* boardColSize, char** words, int wordsSize, int* returnSize) {
    TrieNode* root = trieNodeCreate();
    for (int i = 0; i < wordsSize; ++i) insertWord(root, words[i]);
    char** result = malloc((size_t)wordsSize * sizeof(char*));
    *returnSize = 0;
    for (int row = 0; row < boardSize; ++row) {
        for (int col = 0; col < boardColSize[row]; ++col) {
            dfs(board, boardSize, boardColSize, row, col, root, result, returnSize);
        }
    }
    trieFree(root);
    return result;
}
