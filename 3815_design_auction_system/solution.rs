// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

use std::collections::{BinaryHeap, HashMap};

#[derive(Eq, PartialEq)]
struct Bid {
    amount: i32,
    user_id: i32,
}

impl Ord for Bid {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.amount
            .cmp(&other.amount)
            .then_with(|| self.user_id.cmp(&other.user_id))
    }
}

impl PartialOrd for Bid {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

pub struct AuctionSystem {
    bids: HashMap<i32, HashMap<i32, i32>>,
    heaps: HashMap<i32, BinaryHeap<Bid>>,
}

impl AuctionSystem {
    pub fn new() -> Self {
        Self {
            bids: HashMap::new(),
            heaps: HashMap::new(),
        }
    }

    pub fn add_bid(&mut self, user_id: i32, item_id: i32, bid_amount: i32) {
        self.bids
            .entry(item_id)
            .or_default()
            .insert(user_id, bid_amount);
        self.heaps
            .entry(item_id)
            .or_default()
            .push(Bid {
                amount: bid_amount,
                user_id,
            });
    }

    pub fn update_bid(&mut self, user_id: i32, item_id: i32, new_amount: i32) {
        self.add_bid(user_id, item_id, new_amount);
    }

    pub fn remove_bid(&mut self, user_id: i32, item_id: i32) {
        if let Some(m) = self.bids.get_mut(&item_id) {
            m.remove(&user_id);
        }
    }

    pub fn get_highest_bidder(&mut self, item_id: i32) -> i32 {
        let Some(h) = self.heaps.get_mut(&item_id) else {
            return -1;
        };
        while let Some(top) = h.peek() {
            if let Some(&amt) = self
                .bids
                .get(&item_id)
                .and_then(|m| m.get(&top.user_id))
            {
                if amt == top.amount {
                    return top.user_id;
                }
            }
            h.pop();
        }
        -1
    }
}
