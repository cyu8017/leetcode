// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

use std::collections::{BinaryHeap, HashMap};
use std::cmp::Reverse;

pub struct FoodRatings {
    cuisine_of: HashMap<String, String>,
    rating_of: HashMap<String, i32>,
    heaps: HashMap<String, BinaryHeap<(i32, Reverse<String>)>>,
}

impl FoodRatings {
    pub fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        let mut cuisine_of = HashMap::new();
        let mut rating_of = HashMap::new();
        let mut heaps: HashMap<String, BinaryHeap<(i32, Reverse<String>)>> = HashMap::new();
        for i in 0..foods.len() {
            cuisine_of.insert(foods[i].clone(), cuisines[i].clone());
            rating_of.insert(foods[i].clone(), ratings[i]);
            heaps
                .entry(cuisines[i].clone())
                .or_default()
                .push((ratings[i], Reverse(foods[i].clone())));
        }
        Self {
            cuisine_of,
            rating_of,
            heaps,
        }
    }

    pub fn change_rating(&mut self, food: String, new_rating: i32) {
        self.rating_of.insert(food.clone(), new_rating);
        let cuisine = self.cuisine_of[&food].clone();
        self.heaps
            .entry(cuisine)
            .or_default()
            .push((new_rating, Reverse(food)));
    }

    pub fn highest_rated(&mut self, cuisine: String) -> String {
        let h = self.heaps.get_mut(&cuisine).unwrap();
        loop {
            let (rating, Reverse(food)) = h.peek().unwrap().clone();
            if self.rating_of[&food] == rating {
                return food;
            }
            h.pop();
        }
    }
}
