// LeetCode 0332 - Reconstruct Itinerary
var findItinerary = function(tickets) {
    const targets = new Map();
    for (const [source, destination] of tickets.sort().reverse()) {
        if (!targets.has(source)) targets.set(source, []);
        targets.get(source).push(destination);
    }

    const route = [];
    const visit = (airport) => {
        while (targets.has(airport) && targets.get(airport).length) {
            visit(targets.get(airport).pop());
        }
        route.push(airport);
    };

    visit("JFK");
    return route.reverse();
};
