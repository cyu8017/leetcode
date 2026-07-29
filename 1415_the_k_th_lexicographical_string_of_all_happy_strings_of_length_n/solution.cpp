#include <string>
#include <vector>

class Solution {
    std::vector<std::string> answer;
    int n;
    void build(std::string path) {
        if ((int)path.size() == n) { answer.push_back(path); return; }
        for (char ch : {'a', 'b', 'c'}) {
            if (path.empty() || path.back() != ch) build(path + ch);
        }
    }
public:
    std::string getHappyString(int n_, int k) {
        n = n_;
        build("");
        return k <= (int)answer.size() ? answer[k - 1] : "";
    }
};
