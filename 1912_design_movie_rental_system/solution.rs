// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

use std::collections::{BTreeSet, HashMap};

pub struct MovieRentingSystem {
    price: HashMap<(i32, i32), i32>,
    available: HashMap<i32, BTreeSet<(i32, i32)>>, // (price, shop)
    rented: BTreeSet<(i32, i32, i32)>,             // (price, shop, movie)
}

impl MovieRentingSystem {
    pub fn new(_n: i32, entries: Vec<Vec<i32>>) -> Self {
        let mut price = HashMap::new();
        let mut available: HashMap<i32, BTreeSet<(i32, i32)>> = HashMap::new();
        for e in entries {
            let shop = e[0];
            let movie = e[1];
            let p = e[2];
            price.insert((shop, movie), p);
            available.entry(movie).or_default().insert((p, shop));
        }
        Self {
            price,
            available,
            rented: BTreeSet::new(),
        }
    }

    pub fn search(&self, movie: i32) -> Vec<i32> {
        self.available
            .get(&movie)
            .map(|set| set.iter().take(5).map(|&(_, shop)| shop).collect())
            .unwrap_or_default()
    }

    pub fn rent(&mut self, shop: i32, movie: i32) {
        let p = self.price[&(shop, movie)];
        if let Some(set) = self.available.get_mut(&movie) {
            set.remove(&(p, shop));
        }
        self.rented.insert((p, shop, movie));
    }

    pub fn drop(&mut self, shop: i32, movie: i32) {
        let p = self.price[&(shop, movie)];
        self.rented.remove(&(p, shop, movie));
        self.available.entry(movie).or_default().insert((p, shop));
    }

    pub fn report(&self) -> Vec<Vec<i32>> {
        self.rented
            .iter()
            .take(5)
            .map(|&(_, shop, movie)| vec![shop, movie])
            .collect()
    }
}
