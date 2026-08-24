// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

export function numRescueBoats(people: number[], limit: number): number {
    people.sort((a, b) => a - b);
    let i = 0, j = people.length - 1, boats = 0;
    while (i <= j) {
        if (people[i] + people[j] <= limit) i++;
        j--;
        boats++;
    }
    return boats;
}
