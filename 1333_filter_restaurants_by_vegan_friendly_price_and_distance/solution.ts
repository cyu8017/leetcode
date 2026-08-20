// LeetCode 1333 - Filter Restaurants By Vegan Friendly Price And Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

function filterRestaurants(restaurants: number[][], veganFriendly: number, maxPrice: number, maxDistance: number): number[] {
    const valid = restaurants.filter((row: any): any => (!veganFriendly || row[2]) && row[3] <= maxPrice && row[4] <= maxDistance);
    valid.sort((a, b: any): any => b[1] - a[1] || b[0] - a[0]);
    return valid.map((row: any): any => row[0]);
}
