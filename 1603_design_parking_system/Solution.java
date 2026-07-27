// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

class ParkingSystem {
    private final int[] spaces;

    public ParkingSystem(int big, int medium, int small) {
        spaces = new int[] {0, big, medium, small};
    }

    public boolean addCar(int carType) {
        if (spaces[carType] == 0) return false;
        spaces[carType]--;
        return true;
    }
}
