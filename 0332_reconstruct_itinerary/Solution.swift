// LeetCode 0332 - Reconstruct Itinerary
// https://leetcode.com/problems/reconstruct-itinerary/

class Solution {
    func findItinerary(_ tickets: [[String]]) -> [String] {
        var targets: [String: [String]] = [:]
        let sortedTickets = tickets.sorted {
            if $0[0] != $1[0] {
                return $0[0] < $1[0]
            }
            return $0[1] < $1[1]
        }
        for ticket in sortedTickets.reversed() {
            targets[ticket[0], default: []].append(ticket[1])
        }

        var route: [String] = []

        func visit(_ airport: String) {
            while !(targets[airport]?.isEmpty ?? true) {
                visit(targets[airport]!.removeLast())
            }
            route.append(airport)
        }

        visit("JFK")
        return route.reversed()
    }
}
