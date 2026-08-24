// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

export function canVisitAllRooms(rooms: number[][]): boolean {
    const seen = new Set([0]);
    const stack = [0];
    while (stack.length) {
        const room = stack.pop();
        for (const key of rooms[room]) {
            if (!seen.has(key)) {
                seen.add(key);
                stack.push(key);
            }
        }
    }
    return seen.size === rooms.length;
}
