#include <algorithm>
#include <cctype>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> pathsWithMaxScore(std::vector<std::string>& board) {
        const int mod = 1000000007;
        int n = (int)board.size();
        std::vector<std::vector<int>> score(n, std::vector<int>(n, -1));
        std::vector<std::vector<int>> ways(n, std::vector<int>(n, 0));
        score[n - 1][n - 1] = 0;
        ways[n - 1][n - 1] = 1;
        for (int r = n - 1; r >= 0; --r) {
            for (int c = n - 1; c >= 0; --c) {
                if (board[r][c] == 'X' || (r == n - 1 && c == n - 1)) continue;
                int best = -1, count = 0;
                for (auto [nr, nc] : {std::pair{r + 1, c}, {r, c + 1}, {r + 1, c + 1}}) {
                    if (nr < n && nc < n && score[nr][nc] >= 0) {
                        if (score[nr][nc] > best) {
                            best = score[nr][nc];
                            count = ways[nr][nc];
                        } else if (score[nr][nc] == best) {
                            count = (count + ways[nr][nc]) % mod;
                        }
                    }
                }
                if (best >= 0) {
                    int add = std::isdigit(static_cast<unsigned char>(board[r][c])) ? board[r][c] - '0' : 0;
                    score[r][c] = best + add;
                    ways[r][c] = count;
                }
            }
        }
        return {std::max(score[0][0], 0), ways[0][0]};
    }
};
