// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
    bool placeWordInCrossword(vector<vector<char>>& board, string word) {
        int m = (int)board.size(), n = (int)board[0].size(), L = (int)word.size();
        auto match = [&](const string& cells) {
            if ((int)cells.size() != L) return false;
            bool ok1 = true, ok2 = true;
            for (int i = 0; i < L; i++) {
                if (cells[i] != ' ' && cells[i] != word[i]) ok1 = false;
                if (cells[i] != ' ' && cells[i] != word[L - 1 - i]) ok2 = false;
            }
            return ok1 || ok2;
        };
        for (int r = 0; r < m; r++) {
            int c = 0;
            while (c < n) {
                while (c < n && board[r][c] == '#') c++;
                int start = c;
                while (c < n && board[r][c] != '#') c++;
                if (c - start == L) {
                    string cells(board[r].begin() + start, board[r].begin() + c);
                    if (match(cells)) return true;
                }
            }
        }
        for (int c = 0; c < n; c++) {
            int r = 0;
            while (r < m) {
                while (r < m && board[r][c] == '#') r++;
                int start = r;
                while (r < m && board[r][c] != '#') r++;
                if (r - start == L) {
                    string cells;
                    for (int i = 0; i < L; i++) cells.push_back(board[start + i][c]);
                    if (match(cells)) return true;
                }
            }
        }
        return false;
    }
};
