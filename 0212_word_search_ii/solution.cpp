// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

#include <array>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
    struct TrieNode {
        std::array<TrieNode*, 26> children{};
        std::string word;
    };

    std::vector<std::vector<char>> board;
    int rows = 0;
    int cols = 0;
    std::unordered_set<std::string> result;

    void dfs(int row, int col, TrieNode* node) {
        char c = board[row][col];
        TrieNode* next = node->children[c - 'a'];
        if (!next) {
            return;
        }
        if (!next->word.empty()) {
            result.insert(next->word);
            next->word.clear();
        }
        board[row][col] = '#';
        if (row + 1 < rows && board[row + 1][col] != '#') dfs(row + 1, col, next);
        if (row - 1 >= 0 && board[row - 1][col] != '#') dfs(row - 1, col, next);
        if (col + 1 < cols && board[row][col + 1] != '#') dfs(row, col + 1, next);
        if (col - 1 >= 0 && board[row][col - 1] != '#') dfs(row, col - 1, next);
        board[row][col] = c;
        bool empty = true;
        for (TrieNode* child : next->children) {
            if (child) {
                empty = false;
                break;
            }
        }
        if (empty) {
            node->children[c - 'a'] = nullptr;
        }
    }

public:
    std::vector<std::string> findWords(std::vector<std::vector<char>>& board, std::vector<std::string>& words) {
        TrieNode root;
        for (const std::string& word : words) {
            TrieNode* node = &root;
            for (char c : word) {
                TrieNode*& child = node->children[c - 'a'];
                if (!child) {
                    child = new TrieNode();
                }
                node = child;
            }
            node->word = word;
        }

        this->board = board;
        rows = static_cast<int>(board.size());
        cols = static_cast<int>(board[0].size());

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                dfs(row, col, &root);
            }
        }
        return std::vector<std::string>(result.begin(), result.end());
    }
};
