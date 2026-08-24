// LeetCode 0332 - Reconstruct Itinerary

// https://leetcode.com/problems/reconstruct-itinerary/



class Solution {

    fun findItinerary(tickets: List<List<String>>): List<String> {

        val targets = mutableMapOf<String, ArrayDeque<String>>()

        for ((source, destination) in tickets.sorted().asReversed()) {

            targets.getOrPut(source) { ArrayDeque() }.addLast(destination)

        }



        val route = mutableListOf<String>()

        visit("JFK", targets, route)

        return route.asReversed()

    }



    private fun visit(airport: String, targets: MutableMap<String, ArrayDeque<String>>, route: MutableList<String>) {

        val destinations = targets[airport]

        if (destinations != null) {

            while (destinations.isNotEmpty()) {

                visit(destinations.removeLast(), targets, route)

            }

        }

        route.add(airport)

    }

}
