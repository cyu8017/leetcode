#include <unordered_map>
#include <vector>

class Cashier {
    int n, discount, count = 0;
    std::unordered_map<int, int> price;
public:
    Cashier(int n, int discount, std::vector<int>& products, std::vector<int>& prices) : n(n), discount(discount) {
        for (size_t i = 0; i < products.size(); ++i) price[products[i]] = prices[i];
    }

    double getBill(std::vector<int> product, std::vector<int> amount) {
        ++count;
        double total = 0;
        for (size_t i = 0; i < product.size(); ++i) total += price[product[i]] * amount[i];
        if (count % n == 0) return total * (100 - discount) / 100.0;
        return total;
    }
};
