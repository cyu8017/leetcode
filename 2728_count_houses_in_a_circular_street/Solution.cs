// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

public interface Street {
    void OpenDoor();
    void CloseDoor();
    bool IsDoorOpen();
    void MoveRight();
    void MoveLeft();
}

public class Solution {
    public int CountHouses(Street street, int k) {
        for (int i = 0; i < k; i++) {
            street.CloseDoor();
            street.MoveRight();
        }
        int ans = 0;
        for (;;) {
            ans++;
            street.OpenDoor();
            street.MoveRight();
            if (street.IsDoorOpen()) break;
        }
        return ans;
    }
}
