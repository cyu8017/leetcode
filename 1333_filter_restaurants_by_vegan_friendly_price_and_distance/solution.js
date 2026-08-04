// LeetCode 1333 - Filter Restaurants By Vegan Friendly Price And Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

/**
 * @param {number[][]} restaurants
 * @param {number} veganFriendly
 * @param {number} maxPrice
 * @param {number} maxDistance
 * @return {number[]}
 */
var filterRestaurants = function(restaurants, veganFriendly, maxPrice, maxDistance) {
    const valid = restaurants.filter((row) => (!veganFriendly || row[2]) && row[3] <= maxPrice && row[4] <= maxDistance);
    valid.sort((a, b) => b[1] - a[1] || b[0] - a[0]);
    return valid.map((row) => row[0]);
};
