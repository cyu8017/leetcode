// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

class TopVotedCandidate {
    /**
     * @param {number[]} persons
     * @param {number[]} times
     */
    constructor(persons, times) {
        this.times = times;
        this.leaders = new Array(persons.length);
        const counts = new Map();
        let leader = -1;
        for (let i = 0; i < persons.length; i++) {
            counts.set(persons[i], (counts.get(persons[i]) || 0) + 1);
            if (leader === -1 || counts.get(persons[i]) >= counts.get(leader)) leader = persons[i];
            this.leaders[i] = leader;
        }
    }

    /**
     * @param {number} t
     * @return {number}
     */
    q(t) {
        let lo = 0, hi = this.times.length - 1, i = -1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (this.times[mid] <= t) {
                i = mid;
                lo = mid + 1;
            } else hi = mid - 1;
        }
        return this.leaders[i];
    }
}

module.exports = { TopVotedCandidate };
