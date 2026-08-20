// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

function groupThePeople(groupSizes: number[]): number[][] {
    const pending = new Map();
    const answer = [];
    for (let person = 0; person < groupSizes.length; person++) {
        const size = groupSizes[person];
        if (!pending.has(size)) pending.set(size, []);
        pending.get(size).push(person);
        if (pending.get(size).length === size) {
            answer.push(pending.get(size));
            pending.set(size, []);
        }
    }
    answer.sort((a, b) => (a.length - b.length) || a.toString().localeCompare(b.toString()));
    return answer;
}
