#include <algorithm>
#include <vector>

class CustomStack {
    int maxSize;
    std::vector<int> a;
public:
    CustomStack(int maxSize) : maxSize(maxSize) {}

    void push(int x) {
        if ((int)a.size() < maxSize) a.push_back(x);
    }

    int pop() {
        if (a.empty()) return -1;
        int v = a.back(); a.pop_back();
        return v;
    }

    void increment(int k, int val) {
        for (int i = 0; i < std::min(k, (int)a.size()); ++i) a[i] += val;
    }
};
