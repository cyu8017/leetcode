#include <string>
#include <vector>

class Solution {
public:
    int minSteps(std::string s, std::string t) {
        std::vector<int> cnt(26, 0);
        for (char c : s) ++cnt[c - 'a'];
        for (char c : t) --cnt[c - 'a'];
        int answer = 0;
        for (int x : cnt) if (x > 0) answer += x;
        return answer;
    }
};
