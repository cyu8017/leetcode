#include <string>
#include <unordered_map>
#include <climits>
#include <vector>
#include <cmath>

class Solution {
    int distance(int a, int b) {
        if (a == 26) return 0;
        return std::abs(a / 6 - b / 6) + std::abs(a % 6 - b % 6);
    }
public:
    int minimumDistance(std::string word) {
        std::vector<int> letters;
        for (char ch : word) letters.push_back(ch - 'A');
        std::unordered_map<int, int> dp{{26, 0}};
        int previous = letters[0];
        for (size_t i = 1; i < letters.size(); ++i) {
            int current = letters[i];
            std::unordered_map<int, int> nxt;
            for (auto [free, cost] : dp) {
                int v1 = cost + distance(previous, current);
                if (!nxt.count(free) || nxt[free] > v1) nxt[free] = v1;
                int v2 = cost + distance(free, current);
                if (!nxt.count(previous) || nxt[previous] > v2) nxt[previous] = v2;
            }
            dp = std::move(nxt);
            previous = current;
        }
        int answer = INT_MAX;
        for (auto [_, cost] : dp) answer = std::min(answer, cost);
        return answer;
    }
};
