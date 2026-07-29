#include <queue>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::string longestDiverseString(int a, int b, int c) {
        std::priority_queue<std::pair<int, char>> heap;
        if (a) heap.push({a, 'a'});
        if (b) heap.push({b, 'b'});
        if (c) heap.push({c, 'c'});
        std::string answer;
        while (!heap.empty()) {
            auto [count, ch] = heap.top(); heap.pop();
            int n = (int)answer.size();
            if (n >= 2 && answer[n - 1] == ch && answer[n - 2] == ch) {
                if (heap.empty()) break;
                auto [count2, ch2] = heap.top(); heap.pop();
                answer.push_back(ch2);
                if (count2 - 1) heap.push({count2 - 1, ch2});
                heap.push({count, ch});
            } else {
                answer.push_back(ch);
                if (count - 1) heap.push({count - 1, ch});
            }
        }
        return answer;
    }
};
