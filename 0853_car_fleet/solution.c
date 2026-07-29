// LeetCode 0853 - Car Fleet
// https://leetcode.com/problems/car-fleet/

#include <stdlib.h>

typedef struct { int pos, spd; } Car;

static int cmp_car(const void* a, const void* b) {
    return ((const Car*)b)->pos - ((const Car*)a)->pos;
}

int carFleet(int target, int* position, int positionSize, int* speed, int speedSize) {
    (void)speedSize;
    Car* cars = (Car*)malloc((size_t)positionSize * sizeof(Car));
    for (int i = 0; i < positionSize; i++) cars[i] = (Car){position[i], speed[i]};
    qsort(cars, (size_t)positionSize, sizeof(Car), cmp_car);
    int fleets = 0;
    double max_time = 0.0;
    for (int i = 0; i < positionSize; i++) {
        double time = (double)(target - cars[i].pos) / cars[i].spd;
        if (time > max_time) {
            fleets++;
            max_time = time;
        }
    }
    free(cars);
    return fleets;
}
