// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

#include <queue>
#include <string>
#include <unordered_map>
#include <vector>

class FoodRatings {
public:
    FoodRatings(std::vector<std::string>& foods, std::vector<std::string>& cuisines, std::vector<int>& ratings) {
        for (int i = 0; i < (int)foods.size(); i++) {
            cuisineOf[foods[i]] = cuisines[i];
            ratingOf[foods[i]] = ratings[i];
            heaps[cuisines[i]].push({ratings[i], foods[i]});
        }
    }

    void changeRating(std::string food, int newRating) {
        ratingOf[food] = newRating;
        heaps[cuisineOf[food]].push({newRating, food});
    }

    std::string highestRated(std::string cuisine) {
        auto& h = heaps[cuisine];
        while (true) {
            auto [rating, food] = h.top();
            if (ratingOf[food] == rating) return food;
            h.pop();
        }
    }

private:
    struct Item {
        int rating;
        std::string food;
        bool operator<(const Item& o) const {
            if (rating == o.rating) return food > o.food;
            return rating < o.rating;
        }
    };
    std::unordered_map<std::string, std::string> cuisineOf;
    std::unordered_map<std::string, int> ratingOf;
    std::unordered_map<std::string, std::priority_queue<Item>> heaps;
};
