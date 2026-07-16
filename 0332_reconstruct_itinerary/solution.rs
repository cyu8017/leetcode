// LeetCode 0332 - Reconstruct Itinerary
// https://leetcode.com/problems/reconstruct-itinerary/

use std::collections::HashMap;

impl Solution {
    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
        let mut sorted_tickets = tickets;
        sorted_tickets.sort();
        sorted_tickets.reverse();

        let mut targets: HashMap<String, Vec<String>> = HashMap::new();
        for ticket in sorted_tickets {
            targets
                .entry(ticket[0].clone())
                .or_default()
                .push(ticket[1].clone());
        }

        let mut route = Vec::new();
        fn visit(airport: &str, targets: &mut HashMap<String, Vec<String>>, route: &mut Vec<String>) {
            while let Some(next) = targets.get_mut(airport).and_then(|destinations| destinations.pop()) {
                visit(&next, targets, route);
            }
            route.push(airport.to_string());
        }

        visit("JFK", &mut targets, &mut route);
        route.reverse();
        route
    }
}
