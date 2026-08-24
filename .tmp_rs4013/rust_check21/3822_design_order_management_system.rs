// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

use std::collections::HashMap;

pub struct OrderManagementSystem {
    order_type_map: HashMap<i32, String>,
    price_map: HashMap<i32, i32>,
    t: HashMap<(String, i32), Vec<i32>>,
}

impl OrderManagementSystem {
    pub fn new() -> Self {
        Self {
            order_type_map: HashMap::new(),
            price_map: HashMap::new(),
            t: HashMap::new(),
        }
    }

    pub fn add_order(&mut self, order_id: i32, order_type: String, price: i32) {
        self.order_type_map.insert(order_id, order_type.clone());
        self.price_map.insert(order_id, price);
        self.t.entry((order_type, price)).or_default().push(order_id);
    }

    pub fn modify_order(&mut self, order_id: i32, new_price: i32) {
        let order_type = self.order_type_map[&order_id].clone();
        let old_price = self.price_map[&order_id];
        self.price_map.insert(order_id, new_price);
        if let Some(old_list) = self.t.get_mut(&(order_type.clone(), old_price)) {
            if let Some(i) = old_list.iter().position(|&id| id == order_id) {
                old_list.remove(i);
            }
        }
        self.t
            .entry((order_type, new_price))
            .or_default()
            .push(order_id);
    }

    pub fn cancel_order(&mut self, order_id: i32) {
        let order_type = self.order_type_map.remove(&order_id).unwrap();
        let price = self.price_map.remove(&order_id).unwrap();
        if let Some(list) = self.t.get_mut(&(order_type, price)) {
            if let Some(i) = list.iter().position(|&id| id == order_id) {
                list.remove(i);
            }
        }
    }

    pub fn get_orders_at_price(&self, order_type: String, price: i32) -> Vec<i32> {
        self.t.get(&(order_type, price)).cloned().unwrap_or_default()
    }
}
