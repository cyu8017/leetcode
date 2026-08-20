// LeetCode 1333 - Filter Restaurants by Vegan-Friendly, Price and Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

class Solution {
    func filterRestaurants(_ restaurants: [[Int]], _ veganFriendly: Int, _ maxPrice: Int, _ maxDistance: Int) -> [Int] {
        var valid = restaurants.filter {
            (veganFriendly == 0 || $0[2] == 1) && $0[3] <= maxPrice && $0[4] <= maxDistance
        }
        valid.sort { ($0[1], $0[0]) > ($1[1], $1[0]) }
        return valid.map { $0[0] }
    }
}
