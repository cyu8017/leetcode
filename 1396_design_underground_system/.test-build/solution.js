"use strict";
// LeetCode 1396: Design Underground System
class UndergroundSystem {
    constructor() {
        this.checkIns = new Map();
        this.routes = new Map();
    }
    checkIn(id, stationName, t) {
        this.checkIns.set(id, [stationName, t]);
    }
    checkOut(id, stationName, t) {
        const [start, time] = this.checkIns.get(id), key = `${start}|${stationName}`;
        const [total, count] = this.routes.get(key) || [0, 0];
        this.routes.set(key, [total + t - time, count + 1]);
        this.checkIns.delete(id);
    }
    getAverageTime(startStation, endStation) {
        const [total, count] = this.routes.get(`${startStation}|${endStation}`);
        return total / count;
    }
}
