export function findItinerary(tickets: string[][]): string[] {
    const targets = new Map<string, string[]>();
    for (const [source, destination] of tickets.sort().reverse()) {
        if (!targets.has(source)) targets.set(source, []);
        targets.get(source)!.push(destination);
    }

    const route: string[] = [];
    const visit = (airport: string): void => {
        while (targets.has(airport) && targets.get(airport)!.length) {
            visit(targets.get(airport)!.pop()!);
        }
        route.push(airport);
    };

    visit("JFK");
    return route.reverse();
}
