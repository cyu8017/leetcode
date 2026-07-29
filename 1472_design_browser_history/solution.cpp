#include <algorithm>
#include <string>
#include <vector>

class BrowserHistory {
    std::vector<std::string> history;
    int index = 0;
public:
    BrowserHistory(std::string homepage) : history{homepage} {}

    void visit(std::string url) {
        history.resize(index + 1);
        history.push_back(url);
        ++index;
    }

    std::string back(int steps) {
        index = std::max(0, index - steps);
        return history[index];
    }

    std::string forward(int steps) {
        index = std::min((int)history.size() - 1, index + steps);
        return history[index];
    }
};
