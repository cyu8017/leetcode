// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

public class ParkingSystem {
    private readonly int[] spaces;

    public ParkingSystem(int big, int medium, int small) {
        spaces = new[] { 0, big, medium, small };
    }

    public bool AddCar(int carType) {
        if (spaces[carType] == 0) return false;
        spaces[carType]--;
        return true;
    }
}
