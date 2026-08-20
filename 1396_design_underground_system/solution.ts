// LeetCode 1396: Design Underground System

class UndergroundSystem {
    checkIns: any;
    routes: any;
    constructor() {

        this.checkIns = new Map();
        this.routes = new Map();
    }
    checkIn(id: any, stationName: any, t: any): any {

        this.checkIns.set(id, [stationName, t]);
    }
    checkOut(id: any, stationName: any, t: any): any {

        const [start, time] = this.checkIns.get(id), key = `${start}|${stationName}`;
        const [total, count] = this.routes.get(key) || [0, 0];
        this.routes.set(key, [total + t - time, count + 1]);
        this.checkIns.delete(id);
    }
    getAverageTime(startStation: any, endStation: any): any {

        const [total, count] = this.routes.get(`${startStation}|${endStation}`);
        return total / count;
    }
}
