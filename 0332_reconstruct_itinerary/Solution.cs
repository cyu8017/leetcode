// LeetCode 0332 - Reconstruct Itinerary

// https://leetcode.com/problems/reconstruct-itinerary/



using System.Collections.Generic;



public class Solution {

    public IList<string> FindItinerary(IList<IList<string>> tickets) {

        List<IList<string>> sortedTickets = new(tickets);

        sortedTickets.Sort((left, right) => {

            int compare = string.Compare(left[0], right[0], StringComparison.Ordinal);

            return compare != 0 ? compare : string.Compare(left[1], right[1], StringComparison.Ordinal);

        });

        sortedTickets.Reverse();



        Dictionary<string, Stack<string>> targets = new();

        foreach (IList<string> ticket in sortedTickets) {

            if (!targets.ContainsKey(ticket[0])) {

                targets[ticket[0]] = new Stack<string>();

            }

            targets[ticket[0]].Push(ticket[1]);

        }



        List<string> route = new();

        Visit("JFK", targets, route);

        route.Reverse();

        return route;

    }



    private void Visit(string airport, Dictionary<string, Stack<string>> targets, List<string> route) {

        if (targets.TryGetValue(airport, out Stack<string>? destinations)) {

            while (destinations.Count > 0) {

                Visit(destinations.Pop(), targets, route);

            }

        }

        route.Add(airport);

    }

}
