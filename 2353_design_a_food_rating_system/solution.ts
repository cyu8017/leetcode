// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

export class FoodRatings {
    constructor(foods: any, cuisines: any, ratings: any) {
        this.cuisineOf = new Map();
        this.ratingOf = new Map();
        this.heaps = new Map();
        for (let i = 0; i < foods.length; i++) {
            this.cuisineOf.set(foods[i], cuisines[i]);
            this.ratingOf.set(foods[i], ratings[i]);
            if (!this.heaps.has(cuisines[i])) this.heaps.set(cuisines[i], []);
            this.heaps.get(cuisines[i]).push(foods[i]);
        }
    }
    _cmp(a: any, b: any): any {
        const ra = this.ratingOf.get(a), rb = this.ratingOf.get(b);
        if (ra !== rb) return rb - ra;
        return a < b ? -1 : a > b ? 1 : 0;
    }
    changeRating(food: any, newRating: any): any {
        this.ratingOf.set(food, newRating);
    }
    highestRated(cuisine: any): any {
        const set = this.heaps.get(cuisine);
        set.sort((a, b) => this._cmp(a, b));
        return set[0];
    }
}
