// LeetCode 0332 - Reconstruct Itinerary

// https://leetcode.com/problems/reconstruct-itinerary/



import java.util.ArrayDeque;

import java.util.ArrayList;

import java.util.Collections;

import java.util.Comparator;

import java.util.Deque;

import java.util.HashMap;

import java.util.List;

import java.util.Map;



class Solution {

    public List<String> findItinerary(List<List<String>> tickets) {

        List<List<String>> sortedTickets = new ArrayList<>(tickets);

        sortedTickets.sort(Comparator.comparing((List<String> ticket) -> ticket.get(0))

                .thenComparing(ticket -> ticket.get(1)));

        Collections.reverse(sortedTickets);



        Map<String, Deque<String>> targets = new HashMap<>();

        for (List<String> ticket : sortedTickets) {

            targets.computeIfAbsent(ticket.get(0), key -> new ArrayDeque<>()).addLast(ticket.get(1));

        }



        List<String> route = new ArrayList<>();

        visit("JFK", targets, route);

        Collections.reverse(route);

        return route;

    }



    private void visit(String airport, Map<String, Deque<String>> targets, List<String> route) {

        Deque<String> destinations = targets.get(airport);

        if (destinations != null) {

            while (!destinations.isEmpty()) {

                visit(destinations.removeLast(), targets, route);

            }

        }

        route.add(airport);

    }

}
