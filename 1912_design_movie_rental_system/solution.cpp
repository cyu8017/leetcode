// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

#include <map>
#include <set>
#include <tuple>
#include <vector>

class MovieRentingSystem {
    std::map<std::pair<int, int>, int> price;
    std::map<int, std::set<std::pair<int, int>>> available;
    std::set<std::tuple<int, int, int>> rented;

public:
    MovieRentingSystem(int n, std::vector<std::vector<int>>& entries) {
        (void)n;
        for (auto& e : entries) {
            int shop = e[0], movie = e[1], p = e[2];
            price[{shop, movie}] = p;
            available[movie].insert({p, shop});
        }
    }

    std::vector<int> search(int movie) {
        std::vector<int> res;
        auto it = available.find(movie);
        if (it == available.end()) return res;
        for (auto& [p, shop] : it->second) {
            res.push_back(shop);
            if ((int)res.size() == 5) break;
        }
        return res;
    }

    void rent(int shop, int movie) {
        int p = price[{shop, movie}];
        available[movie].erase({p, shop});
        rented.insert({p, shop, movie});
    }

    void drop(int shop, int movie) {
        int p = price[{shop, movie}];
        rented.erase({p, shop, movie});
        available[movie].insert({p, shop});
    }

    std::vector<std::vector<int>> report() {
        std::vector<std::vector<int>> res;
        for (auto& [p, shop, movie] : rented) {
            res.push_back({shop, movie});
            if ((int)res.size() == 5) break;
        }
        return res;
    }
};
