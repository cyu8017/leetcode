#include <vector>

class ProductOfNumbers {
    std::vector<int> p{1};
public:
    ProductOfNumbers() {}

    void add(int num) {
        if (num == 0) p = {1};
        else p.push_back(p.back() * num);
    }

    int getProduct(int k) {
        if (k >= (int)p.size()) return 0;
        return p.back() / p[(int)p.size() - 1 - k];
    }
};
