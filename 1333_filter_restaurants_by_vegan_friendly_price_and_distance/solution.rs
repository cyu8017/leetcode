// LeetCode 1333 - Filter Restaurants by Vegan-Friendly, Price and Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

impl Solution {
    pub fn filter_restaurants(
        restaurants: Vec<Vec<i32>>,
        vegan_friendly: i32,
        max_price: i32,
        max_distance: i32,
    ) -> Vec<i32> {
        let mut valid: Vec<&Vec<i32>> = restaurants
            .iter()
            .filter(|row| {
                (vegan_friendly == 0 || row[2] == 1) && row[3] <= max_price && row[4] <= max_distance
            })
            .collect();
        valid.sort_by(|a, b| b[1].cmp(&a[1]).then(b[0].cmp(&a[0])));
        valid.into_iter().map(|row| row[0]).collect()
    }
}
