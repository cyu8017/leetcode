// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

#include <pthread.h>
#include <stdlib.h>

typedef struct {
    int greenRoad;
    pthread_mutex_t lock;
} TrafficLight;

TrafficLight* trafficLightCreate(void) {
    TrafficLight* obj = (TrafficLight*)malloc(sizeof(TrafficLight));
    obj->greenRoad = 1;
    pthread_mutex_init(&obj->lock, NULL);
    return obj;
}

void trafficLightCarArrived(
    TrafficLight* obj,
    int carId,
    int roadId,
    int direction,
    void (*turnGreen)(void),
    void (*crossCar)(void)
) {
    (void)carId;
    (void)direction;
    pthread_mutex_lock(&obj->lock);
    if (roadId != obj->greenRoad) {
        turnGreen();
        obj->greenRoad = roadId;
    }
    crossCar();
    pthread_mutex_unlock(&obj->lock);
}

void trafficLightFree(TrafficLight* obj) {
    if (!obj) return;
    pthread_mutex_destroy(&obj->lock);
    free(obj);
}
