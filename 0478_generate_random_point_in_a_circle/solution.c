// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

#include <math.h>
#include <stdlib.h>

typedef struct {
    double radius;
    double x_center;
    double y_center;
} Solution;

Solution* solutionCreate(double radius, double x_center, double y_center) {
    Solution* obj = (Solution*)malloc(sizeof(Solution));
    obj->radius = radius;
    obj->x_center = x_center;
    obj->y_center = y_center;
    return obj;
}

double* solutionRandPoint(Solution* obj, int* retSize) {
    double* point = (double*)malloc(2 * sizeof(double));
    while (1) {
        double x = ((double)rand() / RAND_MAX) * 2.0 * obj->radius - obj->radius;
        double y = ((double)rand() / RAND_MAX) * 2.0 * obj->radius - obj->radius;
        if (x * x + y * y <= obj->radius * obj->radius) {
            point[0] = obj->x_center + x;
            point[1] = obj->y_center + y;
            break;
        }
    }
    *retSize = 2;
    return point;
}

void solutionFree(Solution* obj) {
    free(obj);
}
